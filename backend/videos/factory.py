from .camera import JpgCamera, Mp4Camera, RtspCamera, WebCamera


def create_camera(config, img_proc):
    if config['RTSP_CAMERA']:
        return RtspCamera(config['RTSP_URL'], img_proc)
    elif config['WEB_CAMERA']:
        return WebCamera(config['WEB_CAM_ID'], img_proc)
    elif config['MP4_CAMERA']:
        return Mp4Camera(config['MP4_FILE'], img_proc)
    else:
        return JpgCamera([f'./videos/sample/sample{i:02}.jpg' for i in range(1, 4)], img_proc)
