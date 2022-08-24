from unittest.mock import patch
from my_calendar import requests, get_holidays
from requests.exceptions import Timeout
import unittest


class TestCalendar(unittest.TestCase):

    @patch.object(requests, 'get', side_effect=Timeout)
    def test_get_holidays_timeout(self):
        with self.assertRaises(Timeout):
            get_holidays()

if __name__ == '__main__':
    unittest.main()
        