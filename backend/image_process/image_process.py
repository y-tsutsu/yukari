from abc import ABCMeta, abstractmethod

import cv2

from models.character import update_positons


class BaseImageProcess(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, image):
        pass


class DummyProcess(BaseImageProcess):
    def __init__(self):
        self.__count = 0

    def execute(self, image):
        height, width, _ = image.shape
        rows = []

        x = self.__count
        y = self.__count * height // width
        w = width // 5
        h = height // 5
        cv2.rectangle(image, (x, y), (x + w, y + h), color=(122, 64, 236), thickness=2)
        rows.append((1, x, y, w, h))

        x = (width - w) - self.__count
        cv2.rectangle(image, (x, y), (x + w, y + h), color=(194, 87, 126), thickness=2)
        rows.append((2, x, y, w, h))

        x = (width - w) // 2
        cv2.rectangle(image, (x, y), (x + w, y + h), color=(88, 238, 255), thickness=2)
        rows.append((3, x, y, w, h))

        update_positons(rows)

        if height < y + h:
            self.__count = 0
        else:
            self.__count += 1
