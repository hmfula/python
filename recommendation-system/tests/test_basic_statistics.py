from unittest import TestCase
from utils.manhattan import calculate_mean, calculate_median

__author__ = 'harry'


class TestBasicStatistics(TestCase):
    def setUp(self):
        pass

    def test_calculate_mean(self):
        test_data = [1, 2, 3]
        expected_mean = 2
        actual_mean = calculate_mean(test_data)
        self.assertEquals(expected_mean, actual_mean)

    def test_calculate_median(self):
        test_data = [1, 2, 5, 10, 3]
        expected_median = 3
        actual_median = calculate_median(test_data)
        print actual_median
        self.assertEquals(expected_median, actual_median)
