from abc import ABCMeta, abstractmethod


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
