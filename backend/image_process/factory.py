from .dummy import DummyProcess
from .facial import DelayFacialRecognition, FacialRecognition
from .trimming import TrimmingProcess


def create_image_processes(config):
    processes = []
    if config['REAL_FACE_IMG_PROC']:
        processes.append(FacialRecognition('haarcascades/haarcascade_frontalface_alt.xml'))
    if config['ANIME_FACE_IMG_PROC']:
        processes.append(FacialRecognition('haarcascades/lbpcascade_animeface.xml'))
    if config['DELAY_REAL_FACE_IMG_PROC']:
        processes.append(DelayFacialRecognition('haarcascades/haarcascade_frontalface_alt.xml'))
    if config['DELAY_ANIME_FACE_IMG_PROC']:
        processes.append(DelayFacialRecognition('haarcascades/lbpcascade_animeface.xml'))
    if config['TRIMMING_IMG_PROC']:
        processes.append(TrimmingProcess(800, 450))
    if config['DUMMY_IMG_PROC']:
        interval = config['VIDEO_INTERVAL_SEC']
        processes.append(DummyProcess(interval))
    return processes
