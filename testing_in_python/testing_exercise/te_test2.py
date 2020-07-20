import unittest
import te_main


class TestGame(unittest.TestCase):
    def setUp(self):
        print('About to run a test!')

    def test_0(self):
        '''To test when normal'''
        answer = 5
        test_param = 5
        result = te_main.guessing_game(answer, test_param)
        self.assertTrue(result)

    def test_1(self):
        '''To test if not 1-10'''
        answer = 5
        test_param = 12
        result = te_main.guessing_game(answer, test_param)
        self.assertEqual(result, 'hey bozo, I said 1~10')

    def test_2(self):
        '''To test if Value Error'''
        answer = 5
        test_param = 'asdasd'
        result = te_main.guessing_game(answer, test_param)
        self.assertIsInstance(result, ValueError)

    def test_3(self):
        '''To test if Zero Value'''
        answer = 5
        test_param = 0
        result = te_main.guessing_game(answer, test_param)
        self.assertEqual(result, 'hey bozo, I said 1~10')

    def test_4(self):
        '''To test if None'''
        answer = 5
        test_param = ''
        result = te_main.guessing_game(answer, test_param)
        self.assertIsInstance(result, ValueError)


if __name__ == '__main__':
    unittest.main()
