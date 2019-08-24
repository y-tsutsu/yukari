from unittest import TestCase, main

from image_process.dummy import DummyProcess
from image_process.facial import DelayFacialRecognition, FacialRecognition
from image_process.factory import create_image_processes
from image_process.trimming import TrimmingProcess
from yukari import create_app


class TestImageProcess(TestCase):
    def setUp(self):
        app = create_app(__name__, '../../frontend/dist/')
        app.config['REAL_FACE_IMG_PROC'] = False
        app.config['ANIME_FACE_IMG_PROC'] = False
        app.config['DELAY_REAL_FACE_IMG_PROC'] = False
        app.config['DELAY_ANIME_FACE_IMG_PROC'] = False
        app.config['TRIMMING_IMG_PROC'] = False
        app.config['DUMMY_IMG_PROC'] = False
        self.__config = app.config

    def tearDown(self):
        pass

    def test_image_process_factory(self):
        processes = create_image_processes(self.__config)
        self.assertEqual(0, len(processes))

        self.__config['REAL_FACE_IMG_PROC'] = True
        processes = create_image_processes(self.__config)
        self.assertEqual(1, len(processes))
        self.assertTrue(isinstance(processes[0], FacialRecognition))

        self.__config['ANIME_FACE_IMG_PROC'] = True
        processes = create_image_processes(self.__config)
        self.assertEqual(2, len(processes))
        self.assertTrue(isinstance(processes[0], FacialRecognition))
        self.assertTrue(isinstance(processes[1], FacialRecognition))

        self.__config['DELAY_REAL_FACE_IMG_PROC'] = True
        processes = create_image_processes(self.__config)
        self.assertEqual(3, len(processes))
        self.assertTrue(isinstance(processes[0], FacialRecognition))
        self.assertTrue(isinstance(processes[1], FacialRecognition))
        self.assertTrue(isinstance(processes[2], DelayFacialRecognition))

        self.__config['DELAY_ANIME_FACE_IMG_PROC'] = True
        processes = create_image_processes(self.__config)
        self.assertEqual(4, len(processes))
        self.assertTrue(isinstance(processes[0], FacialRecognition))
        self.assertTrue(isinstance(processes[1], FacialRecognition))
        self.assertTrue(isinstance(processes[2], DelayFacialRecognition))
        self.assertTrue(isinstance(processes[3], DelayFacialRecognition))

        self.__config['TRIMMING_IMG_PROC'] = True
        processes = create_image_processes(self.__config)
        self.assertEqual(5, len(processes))
        self.assertTrue(isinstance(processes[0], FacialRecognition))
        self.assertTrue(isinstance(processes[1], FacialRecognition))
        self.assertTrue(isinstance(processes[2], DelayFacialRecognition))
        self.assertTrue(isinstance(processes[3], DelayFacialRecognition))
        self.assertTrue(isinstance(processes[4], TrimmingProcess))

        self.__config['DUMMY_IMG_PROC'] = True
        processes = create_image_processes(self.__config)
        self.assertEqual(6, len(processes))
        self.assertTrue(isinstance(processes[0], FacialRecognition))
        self.assertTrue(isinstance(processes[1], FacialRecognition))
        self.assertTrue(isinstance(processes[2], DelayFacialRecognition))
        self.assertTrue(isinstance(processes[3], DelayFacialRecognition))
        self.assertTrue(isinstance(processes[4], TrimmingProcess))
        self.assertTrue(isinstance(processes[5], DummyProcess))


if __name__ == '__main__':
    main()
