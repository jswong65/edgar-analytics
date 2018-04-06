import sys
sys.path.append('../')

import unittest
import datetime
from session import Session

class TestSession(unittest.TestCase):
    """
    Unit test for Session class
    """

    def setUp(self):
        self.session_1 = Session("1.1.1.1", datetime.datetime(2017, 12, 31, 23, 59, 59))
        self.session_2 = Session("128.128.128.128", datetime.datetime(2018, 1, 1, 0, 0, 0)) 

    def test_ip(self):  

        self.assertEqual(self.session_1.ip, "1.1.1.1")
        self.assertEqual(self.session_2.ip, "128.128.128.128")

    def test_init_time(self):

        self.assertEqual(self.session_1.init_time, datetime.datetime(2017, 12, 31, 23, 59, 59))
        self.assertEqual(self.session_2.init_time, datetime.datetime(2018, 1, 1, 0, 0, 0))

    def test_last_request_time(self):

        self.assertEqual(self.session_1.last_request_time, datetime.datetime(2017, 12, 31, 23, 59, 59))
        self.assertEqual(self.session_2.last_request_time, datetime.datetime(2018, 1, 1, 0, 0, 0))

        self.session_1.last_request_time = datetime.datetime(2017, 1, 1, 00, 00, 00)
        self.session_2.last_request_time = datetime.datetime(2018, 12, 31, 23, 59, 59)

        self.assertEqual(self.session_1.last_request_time, datetime.datetime(2017, 1, 1, 00, 00, 00))
        self.assertEqual(self.session_2.last_request_time, datetime.datetime(2018, 12, 31, 23, 59, 59))

    def test_count(self): 

        self.assertEqual(self.session_1.count, 1)
        self.assertEqual(self.session_2.count, 1)

        self.session_1.increment_count()
        self.session_2.increment_count()
        self.session_2.increment_count()

        self.assertEqual(self.session_1.count, 2)
        self.assertEqual(self.session_2.count, 3)

    def test_get_output(self):
        """
        test get_output function
        """
        init_time_1 = datetime.datetime(2017, 12, 31, 23, 59, 59)
        init_time_2 = datetime.datetime(2018, 1, 1, 0, 0, 0)
        last_request_time_1 = datetime.datetime(2018, 1, 1, 1, 1, 1)
        last_request_time_2 = datetime.datetime(2018, 1, 1, 3, 4, 5)
        
        session_1 = Session("1.1.1.1", init_time_1)
        session_2 = Session("128.128.128.128", init_time_2) 

        session_1.last_request_time = last_request_time_1
        session_2.last_request_time = last_request_time_2

        output_1 = "{},{},{},{},{}\n".format(
                                "1.1.1.1",
                                init_time_1.strftime('%Y-%m-%d %H:%M:%S'),
                                last_request_time_1.strftime('%Y-%m-%d %H:%M:%S'),
                                int((last_request_time_1- init_time_1).total_seconds()) + 1,
                                1
                                )

        output_2 = "{},{},{},{},{}\n".format(
                                "128.128.128.128",
                                init_time_2.strftime('%Y-%m-%d %H:%M:%S'),
                                last_request_time_2.strftime('%Y-%m-%d %H:%M:%S'),
                                int((last_request_time_2- init_time_2).total_seconds()) + 1,
                                1
                                )

        self.assertEqual(session_1.get_output(), output_1)
        self.assertEqual(session_2.get_output(), output_2)

if __name__ == '__main__':
    unittest.main()