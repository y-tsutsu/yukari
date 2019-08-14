class BaseConfig:
    RTSP_CAMERA = False
    WEB_CAMERA = False
    MP4_CAMERA = True
    DELAY_RTSP_CAMERA = False
    DELAY_WEB_CAMERA = False
    DELAY_MP4_CAMERA = False
    JPG_CAMERA = False

    REAL_FACE_IMG_PROC = False
    ANIME_FACE_IMG_PROC = False
    DELAY_REAL_FACE_IMG_PROC = False
    DELAY_ANIME_FACE_IMG_PROC = False
    TRIMMING_IMG_PROC = False
    DUMMY_IMG_PROC = False

    VIDEO_INTERVAL_SEC = 0.033
    RTSP_URL = 'rtsp://user:pass@192.168.0.100/live1.sdp'
    MP4_FILE = './videos/sample/sample.mp4'
    JPG_FILES = [f'./videos/sample/sample{i:02}.jpg' for i in range(1, 4)]
    WEB_CAM_ID = 0
    DELAY_COUNT = 10

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///yukari.db'
