from image_process.dummy import DummyProcess
from image_process.facial import AnimeFaceRecognition, RealFaceRecognition
from image_process.trimming import TrimmingProcess


def create_image_processes(config):
    processes = []
    if config['REAL_FACE_IMG_PROC']:
        processes.append(RealFaceRecognition())
    if config['ANIME_FACE_IMG_PROC']:
        processes.append(AnimeFaceRecognition())
    elif config['TRIMMING_IMG_PROC']:
        processes.append(TrimmingProcess(800, 450))
    elif config['DUMMY_IMG_PROC']:
        interval = config['VIDEO_INTERVAL']
        processes.append(DummyProcess(interval))
    else:
        pass
    return processes
