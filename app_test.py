import unittest
import app

class MyTestCase(unittest.TestCase):
    def test_login(self):
        try:
            app.login()
        except:
            print("An error occured.")
        else:
            print("Ready to go")


if __name__ == '__main__':
    unittest.main()
