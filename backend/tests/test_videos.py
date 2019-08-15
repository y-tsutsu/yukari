from unittest import TestCase, main

from app.factory import create_app


class TestApi(TestCase):
    def setUp(self):
        self.__app = create_app(__name__, '../../frontend/dist/').test_client()

    def tearDown(self):
        pass

    def test_video_route(self):
        res = self.__app.get('/video')
        self.assertEqual(308, res.status_code)


if __name__ == '__main__':
    main()
