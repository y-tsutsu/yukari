from .camera import (DelayMp4Camera, DelayRtspCamera, DelayWebCamera,
                     JpgCamera, Mp4Camera, RtspCamera, WebCamera)


def create_camera(config, img_proc_list):
    if config['RTSP_CAMERA']:
        return RtspCamera(config['RTSP_URL'], img_proc_list)
    elif config['WEB_CAMERA']:
        return WebCamera(config['WEB_CAM_ID'], img_proc_list)
    elif config['MP4_CAMERA']:
        return Mp4Camera(config['MP4_FILE'], img_proc_list)
    elif config['DELAY_RTSP_CAMERA']:
        return DelayRtspCamera(config['DELAY_COUNT'], config['MP4_FILE'], img_proc_list)
    elif config['DELAY_WEB_CAMERA']:
        return DelayWebCamera(config['DELAY_COUNT'], config['MP4_FILE'], img_proc_list)
    elif config['DELAY_MP4_CAMERA']:
        return DelayMp4Camera(config['DELAY_COUNT'], config['MP4_FILE'], img_proc_list)
    else:
        return JpgCamera([f'./videos/sample/sample{i:02}.jpg' for i in range(1, 4)], img_proc_list)
