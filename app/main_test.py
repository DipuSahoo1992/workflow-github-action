from main import get_env, reversed_random_string
import os
import unittest


class TestMain(unittest.TestCase):
    def test_rever_string(self):
        random_string = "hello"
        reversd_random = "olleh"
        self.assertEqual(reversd_random, reversed_random_string(random_string))


    def test_get_env(self):
        self.assertEqual('dev', get_env())




if __name__ == '__main__':
    unittest.main()


    