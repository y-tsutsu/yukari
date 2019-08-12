from image_process.animeface import AnimeFaceProcess
from image_process.dummy import DummyProcess
from image_process.trimming import TrimmingProcess


def create_image_process(config):
    interval = config['VIDEO_INTERVAL']
    if config['ANIME_FACE_IMG_PROC']:
        return AnimeFaceProcess()
    elif config['TRIMMING_IMG_PROC']:
        return TrimmingProcess(800, 450)
    elif config['DUMMY_IMG_PROC']:
        return DummyProcess(interval)
    else:
        return None
