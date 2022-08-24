from unittest.mock import patch, Mock
from my_calendar import get_holidays, requests as mcr
from requests.exceptions import Timeout
import unittest
import my_calendar


class TestCalendar(unittest.TestCase):
    def test_misspelling(self):
        calendar = Mock(spec=my_calendar)
        calendar.get_holidays()
        with self.assertRaises(AttributeError):
            calendar.get_holidayss()

    @patch('my_calendar.requests', autospec=True)
    def test_get_holidays_timeout(self, mocked_requests):
        mocked_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

    @patch('my_calendar.requests.get', side_effect=Timeout, autospec=True)
    def test_get_holidays_timeout_3(self, mocked_requests):
        with self.assertRaises(Timeout):
            get_holidays()

    def test_get_holidays_timeout2(self):
        with patch('my_calendar.requests', autospec=True) as mocked_requests:
            mocked_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()

    def test_get_holidays_timeout_obj_get(self):
        with patch.object(mcr, 'get', side_effect=Timeout, autospec=True):
            with self.assertRaises(Timeout):
                get_holidays()

    @patch.object(mcr, 'get', side_effect=Timeout, autospec=True)
    def test_get_holidays_timeout_obj_get_2(self, mcr_get):
        with self.assertRaises(Timeout):
            get_holidays()


if __name__ == '__main__':
    unittest.main()
