import unittest
from DZ3.config import ACTION
from DZ3.server import client_msg_validation


class TestServer(unittest.TestCase):

    def test_client_msg_validation(self):
        test_fail = {
            'response': 400,
            'error': 'Bad Request'
        }
        test_pass = {'response': 200}
        self.assertEqual(client_msg_validation({'action': ACTION, 'time': 123}), test_pass)
        self.assertEqual(client_msg_validation({'action': 'aasd', 'time': 123}), test_fail)
        self.assertEqual(client_msg_validation({'action': ACTION}), test_fail)
        self.assertEqual(client_msg_validation({'time': 123}), test_fail)

