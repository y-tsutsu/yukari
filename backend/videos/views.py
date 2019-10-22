from logging import Formatter, StreamHandler, getLogger
from time import sleep, time

from flask import Blueprint, Response, current_app

from image_process.factory import create_image_processes

from .factory import create_camera

logger = getLogger(__name__)
handler = StreamHandler()
handler.setFormatter(Formatter('%(levelname)s: %(message)s'))
logger.addHandler(handler)

video = Blueprint('video', __name__, url_prefix='/video')


def gen(camera, interval):
    while True:
        s = time()
        frame = camera.get_frame()
        yield b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'
        e = time()
        sleep_time = interval - (e - s)
        if 0 < sleep_time:
            sleep(sleep_time)
        else:
            logger.warn(f'@@@ sleep time is minus value. {sleep_time * 1000} msec')


@video.route('/')
def video_feed():
    config = current_app.config
    interval = config['VIDEO_INTERVAL_SEC']

    img_proc_list = create_image_processes(config)
    camera = create_camera(config, img_proc_list)

    return Response(gen(camera, interval), mimetype='multipart/x-mixed-replace; boundary=frame')
