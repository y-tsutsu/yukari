from abc import ABCMeta, abstractmethod
from time import time

import cv2


class BaseCamera(metaclass=ABCMeta):
    def __init__(self, img_proc):
        self._img_proc = img_proc

    def _execute_img_proc(self, image):
        if self._img_proc:
            self._img_proc.execute(image)

    @abstractmethod
    def get_frame(self):
        pass


class JpgCamera(BaseCamera):
    def __init__(self, files, img_proc=None):
        super(JpgCamera, self).__init__(img_proc)
        self.__frames = [open(file, 'rb').read() for file in files]

    def get_frame(self):
        return self.__frames[int(time()) % 3]


class Mp4Camera(BaseCamera):
    def __init__(self, filename, img_proc=None):
        super(Mp4Camera, self).__init__(img_proc)
        self.__video = cv2.VideoCapture(filename)

    def __inner_get_frame(self):
        ret, frame = self.__video.read()
        if ret:
            self._execute_img_proc(frame)
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
    def __init__(self, url, img_proc=None):
        super(RtspCamera, self).__init__(url, img_proc)
