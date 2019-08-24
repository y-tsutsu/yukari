from collections import deque

import cv2

from .base_camera import BaseCamera


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
