import unittest
from DZ3.client import create_msg, server_response_cval
from DZ3.config import ACTION


class TestClient(unittest.TestCase):

    def test_crate_msg(self):
        test = create_msg(ACTION, 'fantom')
        test['time'] = 123
        self.assertEqual(test, {"action": ACTION, "time": 123, "user": {"account_name": 'fantom'}})

    def test_server_response_cval(self):
        self.assertEqual(server_response_cval({'response': 200}), '200 : OK')
        self.assertEqual(server_response_cval({'response': 400, 'error': 'Bad Request'}), '400 : Bad Request')
        self.assertRaises(ValueError, server_response_cval, {'error': 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
