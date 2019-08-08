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

    def __inner_get_frame(self):
        ret, frame = self.__video.read()
        if ret:
            ret, encimg = cv2.imencode('.jpg', frame)
            return encimg.tostring()
        else:
            return b''

    def get_frame(self):
        frame = self.__inner_get_frame()
        if not frame:
            self.__video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frame = self.__inner_get_frame()
        return frame


class RtspCamera(Mp4Camera):
    def __init__(self, url):
        super(RtspCamera, self).__init__(url)
