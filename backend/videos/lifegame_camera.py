from random import randint

import cv2
import numpy as np

from .base_camera import BaseCamera


class LifeGameCamera(BaseCamera):
    BASE_SIZE = 10

    def __init__(self, size=70, img_proc_list=[]):
        super().__init__(img_proc_list)
        self.__size = size
        self.__matrix = [[False if randint(0, 2) else True for x in range(size)] for y in range(size)]
        self.__count = 0
        self.__image = self.__draw_image(self.__matrix)

    def __get_around_points(self, x, y):
        def __inner(index, size):
            if index < 0:
                return size + index
            if index >= size:
                return index - size
            return index
        points = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
        points = [(__inner(x, self.__size), __inner(y, self.__size)) for x, y in points]
        return points

    def __update_matrix(self):
        new_matrix = [[False for x in range(self.__size)] for y in range(self.__size)]
        for x in range(self.__size):
            for y in range(self.__size):
                points = self.__get_around_points(x, y)
                life_count = len([True for x, y in points if self.__matrix[y][x]])
                if self.__matrix[y][x]:
                    new_matrix[y][x] = False if life_count <= 1 or 4 <= life_count else True
                else:
                    new_matrix[y][x] = True if life_count == 3 else False
        self.__matrix = new_matrix

    def __draw_image(self, matrix):
        image = np.full((self.__size * LifeGameCamera.BASE_SIZE, self.__size * LifeGameCamera.BASE_SIZE, 3), 255, dtype=np.uint8)
        for y, row in enumerate(self.__matrix):
            for x, value in enumerate(row):
                if not value:
                    continue
                pos1 = (x * LifeGameCamera.BASE_SIZE, y * LifeGameCamera.BASE_SIZE)
                pos2 = (pos1[0] + LifeGameCamera.BASE_SIZE - 1, pos1[1] + LifeGameCamera.BASE_SIZE - 1)
                cv2.rectangle(image, pos1, pos2, (152, 72, 136), thickness=-1)
        return image

    def get_frame(self):
        self.__count += 1
        if self.__count == 10:
            self.__update_matrix()
            self.__image = self.__draw_image(self.__matrix)
            self.__count = 0
        image = self._execute_img_proc(self.__image)
        ret, encimg = cv2.imencode('.jpg', image)
        return encimg.tostring()
