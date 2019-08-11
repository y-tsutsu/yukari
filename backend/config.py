class BaseConfig:
    RTSP_CAMERA = False
    MP4_CAMERA = True
    JPG_CAMERA = False

    DUMMY_IMG_PROC = True

    VIDEO_INTERVAL = 0.033
    RTSP_URL = 'rtsp://user:pass@192.168.0.100/live1.sdp'
    MP4_FILE = './videos/sample/sample.mp4'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///yukari.db'
