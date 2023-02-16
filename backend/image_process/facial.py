from copy import deepcopy
from os.path import dirname, join
from queue import Queue
from threading import Thread

import cv2

from models.character import CharacterTable

from .base import BaseImageProcess


def calc_scale(width):
    scaled_width = 300
    return scaled_width / width


class FacialRecognition(BaseImageProcess):
    def __init__(self, filename, interval):
        xml_name = join(dirname(__file__), filename)
        self.__classifier = cv2.CascadeClassifier(xml_name)
        self.__dummy_row = [(i, 0, 0, 0, 0) for i in range(1, 4)]
        self.__db_update_count = 0
        self.DB_UPDATE_INTERVAL_COUNT = int(0.5 / interval * (2 / 3))

    def execute(self, image):
        height, width, _ = image.shape
        scale = calc_scale(width)
        resize_image = cv2.resize(image, dsize=None, fx=scale, fy=scale)
        gray_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.equalizeHist(gray_image)
        min_ = min(height, width) // 15
        faces = self.__classifier.detectMultiScale(gray_image, minSize=(min_, min_))

        rows = []
        for i, (x, y, w, h) in enumerate(faces):
            x = int(x / scale)
            y = int(y / scale)
            w = int(w / scale)
            h = int(h / scale)
            cv2.rectangle(image, (x, y), (x + w, y + h), color=(122, 64, 236), thickness=2)
            rows.append((i + 1, int(x), int(y), int(w), int(h)))

        if self.DB_UPDATE_INTERVAL_COUNT <= self.__db_update_count:
            rows += self.__dummy_row[len(rows):]
            CharacterTable.update_positons(rows[:3])
            self.__db_update_count = 0
        else:
            self.__db_update_count += 1

        return image


class DelayFacialRecognition(BaseImageProcess):
    def __init__(self, filename):
        xml_name = join(dirname(__file__), filename)
        self.__classifier = cv2.CascadeClassifier(xml_name)
        self.__dummy_row = [(i, 0, 0, 0, 0) for i in range(1, 4)]
        self.__prepare_queue = Queue()
        self.__prepare_thread = Thread(target=self.__prepare_worker, args=(self.__prepare_queue,))
        self.__prepare_thread.daemon = True
        self.__prepare_thread.start()
        self.__prepare_rows = []
        self.__image = None
        self.__rows = []

    def __prepare_worker(self, queue):
        while True:
            image = queue.get()
            height, width, _ = image.shape
            scale = calc_scale(width)
            resize_image = cv2.resize(image, dsize=None, fx=scale, fy=scale)
            gray_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)
            gray_image = cv2.equalizeHist(gray_image)
            min_ = int(min(height * scale, width * scale) / 15)
            faces = self.__classifier.detectMultiScale(gray_image, minSize=(min_, min_))

            self.__prepare_rows.clear()
            for i, (x, y, w, h) in enumerate(faces):
                self.__prepare_rows.append((i + 1, int(x / scale), int(y / scale), int(w / scale), int(h / scale)))

            queue.task_done()

    def execute(self, image):
        if image is self.__image:
            self.__prepare_queue.join()
            self.__image = None
            self.__rows = deepcopy(self.__prepare_rows)

        for i, x, y, w, h in self.__rows:
            cv2.rectangle(image, (x, y), (x + w, y + h), color=(122, 64, 236), thickness=2)

        self.__rows += self.__dummy_row[len(self.__rows):]
        CharacterTable.update_positons_async(self.__rows[:3])

        return image

    def prepare(self, image):
        if self.__image is not None:
            return
        self.__image = image
        self.__prepare_queue.put(image)
