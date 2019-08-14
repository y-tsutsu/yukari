from abc import ABCMeta, abstractmethod
from collections import deque
from time import time

import cv2
import numpy as np


class BaseCamera(metaclass=ABCMeta):
    def __init__(self, img_proc_list):
        self.__img_proc_list = img_proc_list

    def _prepare_img_proc(self, image):
        for img_proc in self.__img_proc_list:
            img_proc.prepare(image)

    def _execute_img_proc(self, image):
        for img_proc in self.__img_proc_list:
            image = img_proc.execute(image)
        return image

    @abstractmethod
    def get_frame(self):
        pass


class JpgCamera(BaseCamera):
    def __init__(self, files, img_proc_list=[]):
        super().__init__(img_proc_list)
        self.__frames = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in files]

    def get_frame(self):
        jpg = np.copy(self.__frames[int(time()) % 3])
        jpg = self._execute_img_proc(jpg)
        ret, encimg = cv2.imencode('.jpg', jpg)
        return encimg.tostring()


class VideoCaptureCamera(BaseCamera):
    def __init__(self, source, img_proc_list=[]):
        super().__init__(img_proc_list)
        self._video = cv2.VideoCapture(source)

    def _inner_get_frame(self):
        ret, frame = self._video.read()
        if not ret:
            self._video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self._video.read()
        return ret, frame

    def get_frame(self):
        ret, frame = self._inner_get_frame()
        if not ret:
            return frame
        frame = self._execute_img_proc(frame)
        ret, encimg = cv2.imencode('.jpg', frame)
        return encimg.tostring()


class DelayVideoCaptureCamera(VideoCaptureCamera):
    def __init__(self, delay_count, source, img_proc_list=[]):
        super().__init__(source, img_proc_list)
        self.__prepare_image = None
        self.__image_queue = deque()
        for _ in range(delay_count):
            ret, frame = self._inner_get_frame()
            self.__image_queue.append(frame)

    def get_frame(self):
        ret, frame = self._inner_get_frame()
        self.__image_queue.append(frame)
        if self.__prepare_image is None:
            self.__prepare_image = frame
            self._prepare_img_proc(frame)

        frame = self.__image_queue.popleft()
        if isinstance(frame, bytes):
            return frame
        self.__prepare_image = None if frame is self.__prepare_image else self.__prepare_image

        frame = self._execute_img_proc(frame)

        ret, encimg = cv2.imencode('.jpg', frame)
        return encimg.tostring()
