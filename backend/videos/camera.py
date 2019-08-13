from abc import ABCMeta, abstractmethod
from time import time

import cv2
import numpy as np


class BaseCamera(metaclass=ABCMeta):
    def __init__(self, img_proc_list):
        self.__img_proc_list = img_proc_list

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
    def __init__(self, filename, img_proc_list=[]):
        super().__init__(img_proc_list)
        self.__video = cv2.VideoCapture(filename)

    def __inner_get_frame(self):
        ret, frame = self.__video.read()
        if not ret:
            self.__video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.__video.read()
        return ret, frame if ret else b''

    def get_frame(self):
        ret, frame = self.__inner_get_frame()
        if not ret:
            return frame
        frame = self._execute_img_proc(frame)
        ret, encimg = cv2.imencode('.jpg', frame)
        return encimg.tostring()


class Mp4Camera(VideoCaptureCamera):
    def __init__(self, filename, img_proc_list=[]):
        super().__init__(filename, img_proc_list)


class RtspCamera(VideoCaptureCamera):
    def __init__(self, url, img_proc_list=[]):
        super().__init__(url, img_proc_list)


class WebCamera(VideoCaptureCamera):
    def __init__(self, cam_id, img_proc_list=[]):
        super().__init__(cam_id, img_proc_list)
