from unittest import TestCase, main

from app.factory import create_app


class TestApp(TestCase):
    def setUp(self):
        self.__app = create_app(__name__, '../../frontend/dist/').test_client()

    def tearDown(self):
        pass

    def test_spa_route(self):
        rv = self.__app.get('/')
        self.assertEqual(200, rv.status_code)
        rv = self.__app.get('/spam/')
        self.assertEqual(200, rv.status_code)
        rv = self.__app.get('/spam/ham/')
        self.assertEqual(200, rv.status_code)
        rv = self.__app.get('/spam/ham/egg/')
        self.assertEqual(200, rv.status_code)


if __name__ == '__main__':
    main()
