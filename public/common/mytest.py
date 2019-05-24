#coding=utf-8

import unittest
from public.common import pyselenium
from config import globalparam, config
from public.common.log import Log

from public.pages import UtomarketIndexPage, UtomarketLoginPage

class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser)
        self.dr.max_window()
        self.dr.open(config.url)
        self.logger.info('打开{}'.format(config.url))

    def tearDown(self):
        self.dr.quit()
        self.logger.info('###############################  End  ###############################')

class MyUserCenterTest:
    pass


class MyWalletTest:
    pass


class MyLoginedTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser)
        self.dr.max_window()
        self.dr.open(config.url)
        self.logger.info('打开{}'.format(config.url))
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_login = u_index.click_login_btn()
        u_login.login(config.username, '3201')



    def tearDown(self):
        self.dr.quit()
        self.logger.info('###############################  End  ###############################')