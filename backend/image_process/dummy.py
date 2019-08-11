import cv2

from models.character import CharacterTable

from .base import BaseImageProcess


class DummyProcess(BaseImageProcess):
    def __init__(self, interval):
        self.__db_update_count = 0
        self.__move_count = 0
        self.DB_UPDATE_INTERVAL_COUNT = int(0.5 / interval * (2 / 3))

    def execute(self, image):
        height, width, _ = image.shape
        rows = []

        x = self.__move_count
        y = self.__move_count * height // width
        w = width // 5
        h = height // 5
        cv2.rectangle(image, (x, y), (x + w, y + h), color=(122, 64, 236), thickness=2)
        rows.append((1, x, y, w, h))

        x = (width - w) - self.__move_count
        cv2.rectangle(image, (x, y), (x + w, y + h), color=(194, 87, 126), thickness=2)
        rows.append((2, x, y, w, h))

        x = (width - w) // 2
        cv2.rectangle(image, (x, y), (x + w, y + h), color=(88, 238, 255), thickness=2)
        rows.append((3, x, y, w, h))

        if self.DB_UPDATE_INTERVAL_COUNT <= self.__db_update_count:
            CharacterTable.update_positons(rows)
            self.__db_update_count = 0
        else:
            self.__db_update_count += 1

        if height < y + h:
            self.__move_count = 0
        else:
            self.__move_count += 1
