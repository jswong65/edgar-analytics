import unittest
import datetime
from utils import convert_datetime, time_diff

class TestUtils(unittest.TestCase):
    
    def test_convert_datetime(self):
        # test the first second of an year
        dt = convert_datetime("2017-01-01", "00:00:00")
        self.assertEqual(datetime.datetime(2017,1,1,0,0,0), dt)
        # test the last second of an year
        dt = convert_datetime("2017-12-31", "23:59:59")
        self.assertEqual(datetime.datetime(2017,12,31,23,59,59), dt)
        # test with a randomly selected time
        dt = convert_datetime("2017-10-10", "23:00:30")
        self.assertEqual(datetime.datetime(2017,10,10,23,00,30), dt)
        # test with a randomly selected time
        dt = convert_datetime("2018-03-31", "09:20:59")
        self.assertEqual(datetime.datetime(2018,3,31,9,20,59), dt)


    def test_time_diff(self):
        # test difference in seconds
        dt1 = convert_datetime("2017-01-01", "00:00:00")
        dt2 = convert_datetime("2017-01-01", "00:00:02")
        self.assertEqual(2, time_diff(dt1, dt2))
        # test difference in minutes
        dt1 = convert_datetime("2017-01-01", "00:00:00")
        dt2 = convert_datetime("2017-01-01", "00:01:02")
        self.assertEqual(62, time_diff(dt1, dt2))
        # test difference in hours
        dt1 = convert_datetime("2017-01-01", "01:12:00")
        dt2 = convert_datetime("2017-01-01", "03:23:02")
        self.assertEqual(7862, time_diff(dt1, dt2))
        # test difference in days
        dt1 = convert_datetime("2017-01-01", "01:12:00")
        dt2 = convert_datetime("2017-01-02", "03:23:02")
        self.assertEqual(94262, time_diff(dt1, dt2))


if __name__ == '__main__':
    unittest.main()

    