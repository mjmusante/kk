#! /usr/bin/python

import unittest

class TestBasicExistents(unittest.TestCase):

    def test_question_class_exists(self):
        q = Question()
        self.assertIsNotNone(q)

if __name__ == "__main__":
    unittest.main()
