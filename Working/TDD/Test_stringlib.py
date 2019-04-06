import unittest
import stringlib


class Test_stringlib(unittest.TestCase):

    def test_str_length_general1(self):
        self.assertEqual(3, stringlib.str_length("abc"))

    def test_str_length_general2(self):
        self.assertEqual(6, stringlib.str_length("abc123"))

    def test_str_length_corner(self):
        self.assertEqual(0, stringlib.str_length(""))

    def test_str_length_unusual(self):
        self.assertEqual("", stringlib.str_length(1))