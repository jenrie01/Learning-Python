import unittest
import te_main


class TestGame(unittest.TestCase):
    def setUp(self):
        print('About to run a test!')

    def test_correct_guess(self):
        '''To test when the guess is correct'''
        answer = 5
        test_param = 5
        result = te_main.guessing_game(answer, test_param)
        self.assertTrue(result)

    def test_wrong_guess(self):
        '''To test when the guess is wrong'''
        answer = 5
        test_param = 6
        result = te_main.guessing_game(answer, test_param)
        self.assertFalse(result)

    def test_not_in_range(self):
        '''To test when the guess is not within the range of 1-10'''
        answer = 5
        test_param = 12
        result = te_main.guessing_game(answer, test_param)
        self.assertEqual(result, 'hey bozo, I said 1~10')

    def test_value_error(self):
        '''To test when the guess is Value Error'''
        answer = 5
        test_param = 'asdasd'
        result = te_main.guessing_game(answer, test_param)
        self.assertIsInstance(result, ValueError)

    def test_zero_error(self):
        '''To test when the guess is Zero Value'''
        answer = 5
        test_param = 0
        result = te_main.guessing_game(answer, test_param)
        self.assertEqual(result, 'hey bozo, I said 1~10')

    def test_none(self):
        '''To test when the guess is None/Empty'''
        answer = 5
        test_param = ''
        result = te_main.guessing_game(answer, test_param)
        self.assertIsInstance(result, ValueError)


if __name__ == '__main__':
    unittest.main()
