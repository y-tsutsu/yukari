from time import sleep

from flask import Blueprint, Response

from .camera import JpgCamera, Mp4Camera

camera_bp = Blueprint('camera', __name__, url_prefix='/camera')


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
