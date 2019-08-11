from image_process.dummy import DummyProcess


def create_image_process(config):
    interval = config['VIDEO_INTERVAL']
    if config['DUMMY_IMG_PROC']:
        return DummyProcess(interval)
    else:
        return None
