import unittest
import datetime
import sys
sys.path.insert(1, "..")
from wevbox.fn import hashtime


class test_Fn(unittest.TestCase):

    def test_hashtime_return_string(self):
        self.assertTrue(isinstance(hashtime(), str))

    def test_hashtime_expected_string(self):
        expected = "20200820-084622"
        working_date = datetime.datetime(2020, 8, 20, 8, 46, 22)
        returned_string = hashtime(working_date)
        self.assertEqual(expected, returned_string)

    def test_hashtime_expected_string_2(self):
        expected = "20200801-100122"
        working_date = datetime.datetime(2020, 8, 1, 10, 1, 22)
        returned_string = hashtime(working_date)
        self.assertEqual(expected, returned_string)
