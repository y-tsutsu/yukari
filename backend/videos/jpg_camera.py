from time import time

import cv2
import numpy as np

from .base_camera import BaseCamera


class JpgCamera(BaseCamera):
    def __init__(self, files, img_proc_list=[]):
        super().__init__(img_proc_list)
        self.__frames = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in files]

    def get_frame(self):
        jpg = np.copy(self.__frames[int(time()) % 3])
        jpg = self._execute_img_proc(jpg)
        ret, encimg = cv2.imencode('.jpg', jpg)
        return encimg.tostring()
