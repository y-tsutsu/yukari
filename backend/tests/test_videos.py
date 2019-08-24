from unittest import TestCase, main

from videos.factory import create_camera
from videos.jpg_camera import JpgCamera
from videos.lifegame_camera import LifeGameCamera
from videos.vcap_camera import DelayVideoCaptureCamera, VideoCaptureCamera
from yukari import create_app


class TestVideo(TestCase):
    def setUp(self):
        app = create_app(__name__, '../../frontend/dist/')
        app.config['RTSP_CAMERA'] = False
        app.config['WEB_CAMERA'] = False
        app.config['MP4_CAMERA'] = False
        app.config['DELAY_RTSP_CAMERA'] = False
        app.config['DELAY_WEB_CAMERA'] = False
        app.config['DELAY_MP4_CAMERA'] = False
        app.config['LIFE_GAME_CAMERA'] = False
        app.config['JPG_CAMERA'] = False
        self.__app = app.test_client()
        self.__config = app.config

    def tearDown(self):
        pass

    def test_video_route(self):
        res = self.__app.get('/video')
        self.assertEqual(308, res.status_code)

    def test_video_factory(self):
        camera = create_camera(self.__config, None)
        self.assertTrue(isinstance(camera, JpgCamera))

        self.__config['JPG_CAMERA'] = True
        camera = create_camera(self.__config, None)
        self.assertTrue(isinstance(camera, JpgCamera))

        self.__config['LIFE_GAME_CAMERA'] = True
        camera = create_camera(self.__config, None)
        self.assertTrue(isinstance(camera, LifeGameCamera))

        self.__config['DELAY_MP4_CAMERA'] = True
        camera = create_camera(self.__config, None)
        self.assertTrue(isinstance(camera, DelayVideoCaptureCamera))

        self.__config['MP4_CAMERA'] = True
        camera = create_camera(self.__config, None)
        self.assertTrue(isinstance(camera, VideoCaptureCamera))


if __name__ == '__main__':
    main()
