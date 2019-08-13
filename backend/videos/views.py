from time import sleep, time

from flask import Blueprint, Response, current_app

from image_process.factory import create_image_processes

from .factory import create_camera

video_bp = Blueprint('video', __name__, url_prefix='/video')


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
            print(f'@@@ sleep time is minus value. {sleep_time}')


@video_bp.route('/')
def video_feed():
    config = current_app.config
    interval = config['VIDEO_INTERVAL']

    img_proc_list = create_image_processes(config)
    camera = create_camera(config, img_proc_list)

    return Response(gen(camera, interval), mimetype='multipart/x-mixed-replace; boundary=frame')
