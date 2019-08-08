from time import sleep

from flask import Blueprint, Response

from image_process.image_process import DummyProcess

from .camera import JpgCamera, Mp4Camera, RtspCamera

video_bp = Blueprint('video', __name__, url_prefix='/video')


def gen(camera):
    from yukari import config
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        sleep(config['VIDEO_INTERVAL'])


@video_bp.route('/')
def video_feed():
    from yukari import config

    if config['RTSP_CAMERA']:
        camera = RtspCamera('rtsp://user:pass@192.168.0.100/live1.sdp', DummyProcess())
    elif config['MP4_CAMERA']:
        camera = Mp4Camera('./videos/sample/sample.mp4', DummyProcess())
    else:
        camera = JpgCamera([f'./videos/sample/sample{i:02}.jpg' for i in range(1, 4)], DummyProcess())

    return Response(gen(camera), mimetype='multipart/x-mixed-replace; boundary=frame')
