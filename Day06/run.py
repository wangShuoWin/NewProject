from HTMLTestRunner import HTMLTestRunner
from BSTestRunner import BSTestRunner
from Day06 import Test
import os
import time
import unittest
#################HTMLTestRunner
suite = unittest.TestSuite()
suite.addTest(Test.TestDayMon('testDay'))
suite.addTest(Test.TestDayMon('testMon'))
report_dir = './report'
now_time = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now_time + 'test_report.html'
report_file =os.path.join(report_name)
f = open(report_file,'wb')
runner = HTMLTestRunner(stream=f,title=u'测试报告111',description=u'ceshishsihsishsi',verbosity=2)
runner.run(suite)



############BSTestRunner
# # 用例所在路径
# test_dir = os.getcwd() #返回当前工作目录
#
# # 加载测试用例
# discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
#
# if __name__ == '__main__':
#     # 测试报告存放路径
#     report_dir ='./report'
#     if not os.path.isdir(report_dir):
#         os.mkdir(report_dir)
#     # 定义报告的文命名方式
#     now = time.strftime('%Y-%m-%d',time.localtime(time.time()))
#     report_name = report_dir + '/' + now + 'result.html'
#
#    # 运行用例并生成报告
#     with open(report_name,'wb')as f:
#         runer = BSTestRunner(stream=f,title="Test Report",description="Test case result")
#         runer.run(discover)
