from src.Checker import Checker
import unittest
from datetime import datetime
from unittest.mock import Mock


class test_Checker(unittest.TestCase):
    def setUp(self):
        self.temp = Checker()

    def test_remainder_before_17(self):
        self.temp.env.getTime = Mock(name='getTime')
        self.temp.env.getTime.return_value = datetime(2021, 11, 1, 16, 15, 10, 222222)
        self.temp.resetWav()
        self.temp.remainder()
        self.assertFalse(self.temp.check_wav())

    def test_remainder_after_17(self):
        self.temp.env.getTime = Mock(name='getTime')
        self.temp.env.getTime.return_value = datetime(2021, 11, 1, 17, 15, 10, 222222)
        self.temp.resetWav()
        self.temp.remainder()
        self.assertTrue(self.temp.check_wav())
