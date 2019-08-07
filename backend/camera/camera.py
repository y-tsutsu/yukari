from abc import ABCMeta, abstractmethod
from time import time

import cv2


class BaseCamera(metaclass=ABCMeta):
    @abstractmethod
    def get_frame(self):
        pass


class JpgCamera(BaseCamera):
    def __init__(self, files):
        self.__frames = [open(file, 'rb').read() for file in files]

    def get_frame(self):
        return self.__frames[int(time()) % 3]


class Mp4Camera(BaseCamera):
    def __init__(self, filename):
        self.__video = cv2.VideoCapture(filename)

    def get_frame(self):
        ret, frame = self.__video.read()
        ret, encimg = cv2.imencode('.jpg', frame)
        return encimg.tostring()
