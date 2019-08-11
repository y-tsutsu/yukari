from time import sleep, time

from flask import Blueprint, Response, current_app

from image_process.image_process import DummyProcess

from .camera import JpgCamera, Mp4Camera, RtspCamera

video_bp = Blueprint('video', __name__, url_prefix='/video')


def gen(camera, interval):
    while True:
        s = time()
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
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

    img_proc = DummyProcess(interval) if config['DUMMY_IMG_PROC'] else None

    if config['RTSP_CAMERA']:
        camera = RtspCamera('rtsp://user:pass@192.168.0.100/live1.sdp', img_proc)
    elif config['MP4_CAMERA']:
        camera = Mp4Camera('./videos/sample/sample.mp4', img_proc)
    else:
        camera = JpgCamera([f'./videos/sample/sample{i:02}.jpg' for i in range(1, 4)], img_proc)

    return Response(gen(camera, interval), mimetype='multipart/x-mixed-replace; boundary=frame')
