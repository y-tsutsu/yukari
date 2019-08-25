from unittest import TestCase, main

from yukari import create_app


class TestSpa(TestCase):
    def setUp(self):
        self.__app = create_app(__name__, '../../frontend/dist/').test_client()

    def tearDown(self):
        pass

    def test_spa_route(self):
        res = self.__app.get('/')
        self.assertEqual(200, res.status_code)
        res = self.__app.get('/spam/')
        self.assertEqual(200, res.status_code)
        res = self.__app.get('/spam/ham/')
        self.assertEqual(200, res.status_code)
        res = self.__app.get('/spam/ham/egg/')
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    main()
