from image_process.dummy import DummyProcess
from image_process.facial import DelayFacialRecognition, FacialRecognition
from image_process.trimming import TrimmingProcess


def create_image_processes(config):
    processes = []
    if config['REAL_FACE_IMG_PROC']:
        processes.append(FacialRecognition('haarcascade_frontalface_default.xml'))
    if config['ANIME_FACE_IMG_PROC']:
        processes.append(FacialRecognition('lbpcascade_animeface.xml'))
    if config['DELAY_REAL_FACE_IMG_PROC']:
        processes.append(DelayFacialRecognition('haarcascade_frontalface_default.xml'))
    if config['DELAY_ANIME_FACE_IMG_PROC']:
        processes.append(DelayFacialRecognition('lbpcascade_animeface.xml'))
    if config['TRIMMING_IMG_PROC']:
        processes.append(TrimmingProcess(800, 450))
    if config['DUMMY_IMG_PROC']:
        interval = config['VIDEO_INTERVAL']
        processes.append(DummyProcess(interval))
    return processes
