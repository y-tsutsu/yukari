from os import remove
from os.path import dirname, join
from unittest import TestCase, main

from models.character import CharacterTable
from yukari import create_app


class TestApi(TestCase):
    TEST_DB_FILENAME = 'yukari_test.db'

    def setUp(self):
        app = create_app(__name__, '../../frontend/dist/')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{TestApi.TEST_DB_FILENAME}'
        CharacterTable.init_db(app)
        self.__app = app.test_client()

    def tearDown(self):
        db_filename = join(dirname(__file__), TestApi.TEST_DB_FILENAME)
        remove(db_filename)

    def test_api_route(self):
        res = self.__app.get('/api/characters')
        self.assertEqual(200, res.status_code)
        self.assertTrue(res.is_json)

        res = self.__app.post('/api/characters')
        self.assertEqual(404, res.status_code)

        res = self.__app.put('/api/characters')
        self.assertEqual(404, res.status_code)

        res = self.__app.delete('/api/characters')
        self.assertEqual(404, res.status_code)

    def test_api_json(self):
        res = self.__app.get('/api/characters')
        self.assertGreaterEqual(len(res.json), 3)
        for x in res.json:
            self.assertTrue('name' in x)
            self.assertTrue('cv' in x)
            self.assertTrue('note' in x)
            self.assertTrue('pos' in x)


if __name__ == '__main__':
    main()
