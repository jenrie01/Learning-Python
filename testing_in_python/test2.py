import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        '''You can also put 1 line comment w/docstring'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'asdsadas'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = ''
        result = main.do_stuff(test_param)
        # self.assertIsNone(result)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_param = 0
        result = main.do_stuff(test_param)
        # self.assertIsNone(result)
        self.assertEqual(result, 'please enter a number')

    def tearDown(self):
        print('cleaning up')


# python3 -m unittest (runs all the test)
# python3 -m unittest -v(which test are ok and failed)
if __name__ == '__main__':
    unittest.main()
