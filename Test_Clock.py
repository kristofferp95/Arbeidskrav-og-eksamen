from clock import Clock
import unittest

class Test_Clock(unittest.TestCase):
    def setUp(self):
        self.__clock = Clock()

    def test_inc_sec_from_default_values(self):
        self.__clock.inc_sec()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0000:00:00:01")

    def test_inc_min_from_default_values(self):
        self.__clock.inc_min()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0000:00:01:00")

    def test_inc_sec_from_midnight_jan(self):
        self.__clock = Clock(31, 1, 2021, 23, 59, 59)
        self.__clock.inc_sec()
        self.assertEqual(self.__clock.clock_as_string(), "01:02:2021:00:00:00")

    def test_for_false_leapyear1(self):
        self.__clock = Clock(28, 2, 2021, 23, 59, 59)
        self.__clock.inc_sec()
        self.assertEqual(self.__clock.clock_as_string(), "01:03:2021:00:00:00")
    
    def test_for_false_leapyear2(self):
        self.__clock = Clock(28, 2, 1800, 23, 59, 5)
        self.__clock.inc_min()
        self.assertEqual(self.__clock.clock_as_string(), "01:03:1800:00:00:05")
    
    def test_for_leapyear1(self):
        self.__clock = Clock(28, 2, 2020, 23, 59, 59)
        self.__clock.inc_sec()
        self.assertEqual(self.__clock.clock_as_string(), "29:02:2020:00:00:00")

    def test_for_leapyear2(self):
        self.__clock = Clock(28, 2, 2000, 23, 32, 48)
        self.__clock.inc_hour()
        self.assertEqual(self.__clock.clock_as_string(), "29:02:2000:00:32:48")
    
    def test_from_midnight_december_to_january(self):
        self.__clock = Clock(31, 12, 2021, 23, 59, 59)
        self.__clock.inc_sec()
        self.assertEqual(self.__clock.clock_as_string(), "01:01:2022:00:00:00")

    def test_from_1900th_to_2000(self):
        self.__clock = Clock(4, 5, 1999, 14, 2, 40)
        self.__clock.inc_year()
        self.assertEqual(self.__clock.clock_as_string(), "04:05:2000:14:02:40")

    def test_from_one_hour_before_midnight(self):
        self.__clock = Clock(24, 3, 2021, 23, 2, 55)
        self.__clock.inc_hour()
        self.assertEqual(self.__clock.clock_as_string(), "25:03:2021:00:02:55")

    def test_from_december_to_january(self):
        self.__clock = Clock(21, 12, 2021, 15, 42, 39)
        self.__clock.inc_month()
        self.assertEqual(self.__clock.clock_as_string(), "21:01:2022:15:42:39")


def main():
    if __name__ == '__main__':
        unittest.main()

main()