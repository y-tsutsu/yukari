from .jpg_camera import JpgCamera
from .vcap_camera import DelayVideoCaptureCamera, VideoCaptureCamera


def create_camera(config, img_proc_list):
    if config['RTSP_CAMERA']:
        return VideoCaptureCamera(config['RTSP_URL'], img_proc_list)
    elif config['WEB_CAMERA']:
        return VideoCaptureCamera(config['WEB_CAM_ID'], img_proc_list)
    elif config['MP4_CAMERA']:
        return VideoCaptureCamera(config['MP4_FILE'], img_proc_list)
    elif config['DELAY_RTSP_CAMERA']:
        return DelayVideoCaptureCamera(config['DELAY_COUNT'], config['RTSP_URL'], img_proc_list)
    elif config['DELAY_WEB_CAMERA']:
        return DelayVideoCaptureCamera(config['DELAY_COUNT'], config['WEB_CAM_ID'], img_proc_list)
    elif config['DELAY_MP4_CAMERA']:
        return DelayVideoCaptureCamera(config['DELAY_COUNT'], config['MP4_FILE'], img_proc_list)
    else:
        return JpgCamera(config['JPG_FILES'], img_proc_list)
