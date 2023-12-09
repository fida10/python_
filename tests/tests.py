import unittest
from io import StringIO
from unittest.mock import patch
from src.ans import math_quiz


class TestMathQuiz(unittest.TestCase):

    # First wrong, then correct
    @patch('builtins.input', side_effect=['9', '7'])
    def test_correct_answer(self, input_mock):
        with patch('sys.stdout', new_callable=StringIO) as stdout_mock:
            math_quiz()
            output = stdout_mock.getvalue()
            self.assertIn('Wrong answer, try again!', output)
            self.assertIn('Correct!', output)


if __name__ == '__main__':
    unittest.main()
