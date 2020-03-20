from os import environ
from unittest import TestCase, main

from notification.line import LineNotify


class TestLine(TestCase):
    def setUp(self):
        token = environ['LINE_ACCESS_TOKEN']
        self.__line = LineNotify(token)

    def tearDown(self):
        pass

    def test_send_message(self):
        status_code = self.__line.send_message('test message!!')
        self.assertEqual(status_code, 200)


if __name__ == '__main__':
    main()
