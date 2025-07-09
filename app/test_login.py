from dao import load_user_data,auth_user
import unittest

class TestLogin(unittest.TestCase):
    def test_success(self):
        self.assertTrue(auth_user("huy", 123))  

    def test_failure(self):
        self.assertFalse(auth_user('huy', 122))

if __name__ == '__main__':
    unittest.main()