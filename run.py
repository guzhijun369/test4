#coding=utf-8

import unittest
import HTMLTestRunner
import time
from test4.config import globalparam
from UItestframework.public.common import sendmail

def run():
    test_dir = './testcase'
    with open(reportname,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)
    time.sleep(3)
    # 发送邮件
    mail = sendmail.SendMail()
    mail.send()

if __name__ == '__main__':
    run()