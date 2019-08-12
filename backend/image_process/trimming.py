from .base import BaseImageProcess


class TrimmingProcess(BaseImageProcess):
    def __init__(self, ratio_w, ratio_h):
        self.ratio_w = ratio_w
        self.ratio_h = ratio_h

    def execute(self, image):
        height, width, _ = image.shape
        if self.ratio_w < self.ratio_h:
            w = int(height * (self.ratio_w / self.ratio_h))
            top = 0
            bottom = height
            left = (width - w) // 2
            right = width - ((width - w) // 2)
        else:
            h = int(width * (self.ratio_h / self.ratio_w))
            top = (height - h) // 2
            bottom = height - ((height - h) // 2)
            left = 0
            right = width

        return image[top:bottom, left:right]
