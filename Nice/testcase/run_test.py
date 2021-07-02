import unittest
import HTMLTestRunnerCN
# import test_
from Base import create_file
from Base import connection_email

'''
suite待执行测试用例集
'''
def suite():
    suit = unittest.TestSuite()
    loder = unittest.TestLoader()
    suit1 = loder.discover('/Users/hudongqi/PycharmProjects/Nice/testcase', pattern='test*.py')
    # suit2 = loder.loadTestsFromTestCase(test_.Test_api)
    # suit3 = loder.loadTestsFromModule(test_)
    # suit4 = loder.loadTestsFromNames(
    #     ['test_.Test_api.test_login', 'test_.Test_api.test_accout', 'test_.Test_trade.test_now'])
    suit.addTest(suit1)
    return suit

'''
生成html格式报告
'''
def make_html():
    res_file = create_file.make_file()
    with open(res_file, 'wb') as fp:
        runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='业务流程执行报告', verbosity=2, description='测试测试',
                                                 tester='hudongqi')
        runner.run(suite())
    return res_file

'''
发邮件
'''
def send_email():
    res1_file = make_html()
    print(res1_file)
    with open(res1_file, 'r') as fh:
        html_content = fh.read()

    msg = html_content

    em = connection_email.Send_email()
    em.send_html('hudongqi@163.com',msg)

if __name__ == '__main__':
    make_html()