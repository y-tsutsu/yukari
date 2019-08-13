from os.path import dirname, join

import cv2

from models.character import CharacterTable

from .base import BaseImageProcess


class FacialRecognition(BaseImageProcess):
    def __init__(self, filename):
        xml_name = join(dirname(__file__), filename)
        self.__classifier = cv2.CascadeClassifier(xml_name)
        self.__dummy_row = [(i, 0, 0, 0, 0) for i in range(1, 4)]

    def execute(self, image):
        rows = []

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.equalizeHist(gray_image)
        faces = self.__classifier.detectMultiScale(gray_image)

        for i, (x, y, w, h) in enumerate(faces):
            cv2.rectangle(image, (x, y), (x + w, y + h), color=(122, 64, 236), thickness=2)
            rows.append((i + 1, int(x), int(y), int(w), int(h)))

        rows += self.__dummy_row[len(rows):]
        CharacterTable.update_positons(rows[:3])

        return image


class RealFaceRecognition(FacialRecognition):
    def __init__(self):
        super().__init__('haarcascade_frontalface_default.xml')


class AnimeFaceRecognition(FacialRecognition):
    def __init__(self):
        super().__init__('lbpcascade_animeface.xml')
