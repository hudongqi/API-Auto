import unittest


class Test_trade(unittest.TestCase):

    def setUp(self) -> None:
        print('start')

    def tearDown(self) -> None:
        print('end')

    def test_now(self):
        now = True
        self.assertTrue(now), '不是现货'


