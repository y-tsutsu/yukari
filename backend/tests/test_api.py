from unittest import TestCase, main

from app.factory import create_app
from models.character import CharacterTable


class TestApi(TestCase):
    def setUp(self):
        app = create_app(__name__, '../../frontend/dist/')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        CharacterTable.init_db(app)
        self.__app = app.test_client()

    def tearDown(self):
        pass

    def test_api_route(self):
        res = self.__app.get('/api/infos')
        self.assertEqual(200, res.status_code)
        self.assertTrue(res.is_json)

    def test_api_json(self):
        res = self.__app.get('/api/infos')
        self.assertGreaterEqual(len(res.json), 3)
        for x in res.json:
            self.assertTrue('name' in x)
            self.assertTrue('cv' in x)
            self.assertTrue('note' in x)
            self.assertTrue('pos' in x)


if __name__ == '__main__':
    main()
