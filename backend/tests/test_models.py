from os import remove
from os.path import dirname, join
from time import sleep
from unittest import TestCase, main

from models.character import CharacterTable
from models.database import init_db
from yukari import create_app


class TestCharacter(TestCase):
    TEST_DB_FILENAME = 'yukari_test.db'

    def setUp(self):
        app = create_app(__name__, '../../frontend/dist/')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{TestCharacter.TEST_DB_FILENAME}'
        init_db(app)

    def tearDown(self):
        pass

    def test_character_01(self):
        expect = [
            {'name': '野々原 ゆずこ', 'cv': '大久保 瑠美', 'note': '天真爛漫な性格で元気で無邪気な少女。いたずら好きでよく唯にしており、また奇妙な言動や発想も多い。しかし、成績は優秀で、時々急に真面目になることもある。'},
            {'name': '日向 縁', 'cv': '種田 梨沙', 'note': '家はお金持ち。天然でほんわかとしているが、時々勘が鋭いこともある。'},
            {'name': '櫟井 唯', 'cv': '津田 美波', 'note': '情報処理部の部員3人の中では一番の常識人でしっかり者。サバサバとした性格で言動もやや男性的であり、毎回暴走しがちなゆずこと天然な縁に対するツッコミ役でもある。高校2年から胸が急成長している。'}
        ]
        characters = CharacterTable.get_characters_all()

        self.assertEqual(len(characters), len(expect))
        for c, e in zip(characters, expect):
            self.assertEqual(c['name'], e['name'])
            self.assertEqual(c['cv'], e['cv'])
            self.assertEqual(c['x'], 0)
            self.assertEqual(c['y'], 0)
            self.assertEqual(c['width'], 0)
            self.assertEqual(c['height'], 0)

    def test_character_02(self):
        pk = 1
        CharacterTable.update_positon(pk, 1, 2, 3, 4)
        character = CharacterTable.get_characters_all()[pk - 1]
        self.assertEqual(character['x'], 1)
        self.assertEqual(character['y'], 2)
        self.assertEqual(character['width'], 3)
        self.assertEqual(character['height'], 4)

        CharacterTable.update_positon_async(pk, 10, 20, 30, 40)
        sleep(0.1)
        character = CharacterTable.get_characters_all()[pk - 1]
        self.assertEqual(character['x'], 10)
        self.assertEqual(character['y'], 20)
        self.assertEqual(character['width'], 30)
        self.assertEqual(character['height'], 40)

    def test_character_03(self):
        CharacterTable.update_positons([(2, 11, 22, 33, 44), (3, 111, 222, 333, 444)])
        characters = CharacterTable.get_characters_all()[1:3]
        self.assertEqual(characters[0]['x'], 11)
        self.assertEqual(characters[0]['y'], 22)
        self.assertEqual(characters[0]['width'], 33)
        self.assertEqual(characters[0]['height'], 44)
        self.assertEqual(characters[1]['x'], 111)
        self.assertEqual(characters[1]['y'], 222)
        self.assertEqual(characters[1]['width'], 333)
        self.assertEqual(characters[1]['height'], 444)

        CharacterTable.update_positons_async([(2, 111, 222, 333, 444), (3, 11, 22, 33, 44)])
        sleep(0.1)
        characters = CharacterTable.get_characters_all()[1:3]
        self.assertEqual(characters[0]['x'], 111)
        self.assertEqual(characters[0]['y'], 222)
        self.assertEqual(characters[0]['width'], 333)
        self.assertEqual(characters[0]['height'], 444)
        self.assertEqual(characters[1]['x'], 11)
        self.assertEqual(characters[1]['y'], 22)
        self.assertEqual(characters[1]['width'], 33)
        self.assertEqual(characters[1]['height'], 44)


if __name__ == '__main__':
    main()
