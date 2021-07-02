import unittest
from Base import request_respond


class Test_api(unittest.TestCase):


    def setUp(self):
        print('start')


    def tear_down(self):
        print('end')

    def test_login(self):
        a = 1+1
        self.assertEqual(a,1),'不等'

    def test_accout(self):
        b = 'TRUE'
        self.assertTrue(b)

    def test_code(self):
        a = request_respond.RequestBase('POST').get_respond_body()
        self.assertEqual(int(a['code']),300),'没找对'

