from abc import ABCMeta, abstractmethod

import numpy as np


class BaseImageProcess(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, image: np.ndarray):
        pass

    def prepare(self, image: np.ndarray):
        pass
