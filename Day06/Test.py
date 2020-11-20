import unittest
from Day06.Count import Setting
import requests
import json

class TestDayMon(unittest.TestCase):

    def setUp(self):
        self.app = Setting()

    def testDay(self):
        self.app.Respone01()
        res = self.app.Respone01()
        req = ('操作成功',200)
        self.assertEqual(req,res)

    def testMon(self):
        self.app.Respone02()
        res = self.app.Respone02()
        req = ('操作成功',200)
        self.assertEqual(req, res)

    def tearDown(self):
        pass





if __name__ == '__main__':
    unittest.main()
