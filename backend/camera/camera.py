from time import sleep, time

import cv2
from flask import Blueprint, Response

camera_bp = Blueprint('camera', __name__, url_prefix='/camera')


class JpgCamera():
    def __init__(self, files):
        self.__frames = [open(file, 'rb').read() for file in files]

    def get_frame(self):
        return self.__frames[int(time()) % 3]


class Mp4Camera():
    def __init__(self, filename):
        self.__video = cv2.VideoCapture(filename)

    def get_frame(self):
        ret, frame = self.__video.read()
        ret, encimg = cv2.imencode('.jpg', frame)
        return encimg.tostring()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        sleep(0.033)


@camera_bp.route('/')
def video_feed():
    from yukari import config

    if config['MP4_CAMERA']:
        camera = Mp4Camera('./camera/sample/sample.mp4')
    else:
        camera = JpgCamera([f'./camera/sample/sample{i:02}.jpg' for i in range(1, 4)])

    return Response(gen(camera), mimetype='multipart/x-mixed-replace; boundary=frame')
