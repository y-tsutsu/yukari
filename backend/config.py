class BaseConfig:
    RTSP_CAMERA = False
    MP4_CAMERA = True
    JPG_CAMERA = False

    VIDEO_INTERVAL = 0.033

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///yukari.db'
