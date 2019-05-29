#coding=utf-8

import time
from public.common import mytest
from public.pages import UtomarketLoginPage
from public.pages import UtomarketIndexPage
from public.common import datainfo
from config import config


class TestLogin(mytest.MyTest):
    """utomarket登录测试"""
    def _login_ok(self, account, pw):
        """封装登录"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_login = u_index.click_login_btn()
        u_login.input_account(account)
        u_login.input_password(pw)
        u_login.click_login_btn()
        u_login.captcha()

    def test_login_ok(self):
        """正常登录"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_login = u_index.click_login_btn()
        u_login.login(config.username, '3201')
        result = self.dr.get_title()
        self.assertIn('P2P交易 - 乌托市场(TEST)', result)

    # def test_login_account_error(self):
    #     """正确账号错误密码登录"""
    #     u_index = UtomarketIndexPage.IndexPage(self.dr)
    #     u_login = u_index.click_login_btn()
    #     u_login.login(config.username_error, '3202')
    #     text = u_login.error_span_text()
    #     self.assertIn('错误', text)
    #
    # def test_login_air(self):
    #     """不输入账号密码直接登录"""
    #     u_index = UtomarketIndexPage.IndexPage(self.dr)
    #     u_login = u_index.click_login_btn()
    #     u_login.input_account('')
    #     u_login.input_password('')
    #     u_login.click_login_btn()
    #     texts = u_login.error_div_texts()
    #     self.assertListEqual(texts, ['请输入账户名！', '请输入密码！'])

    # def _login(self, account, pw, text=''):
    #     """封装登录的函数"""
    #     utomarketpage = UtomarketLoginPage.Login(self.dr)
    #     utomarketpage.into_utomarket_page()
    #     utomarketpage.login(account, pw)
    #     utomarketpage.go_captcha(188)
    #     if not text:
    #         # self.dr.assertIn_now('https://otc.utomarket.com/#/trade/index', self.dr.get_url())
    #         self.assertIn('https://otctest.utomarket.com/#/trade/index', self.dr.get_url())
    #     else:
    #         # self.dr.assertIn_now(text, utomarketpage.error_text())
    #         self.assertIn(text, utomarketpage.error_text())
    #     self.dr.quit()
    #
    # def test_login(self):
    #     """正常登录"""
    #     utomarketpage = UtomarketLoginPage.Login(self.dr)
    #     # utomarketpage.into_utomarket_page()
    #     utomarketpage.login('test128', '3201')
    #     utomarketpage.go_captcha(188)
    #     self.assertIn('https://otctest.utomarket.com/#/trade/index', self.dr.get_url())
    #     self.dr.quit()
    # def test_login_excel(self):
    #     """使用数据驱动,进行三次登录测试"""
    #     datas = datainfo.get_xls_to_dict('searKey.xlsx', 'Sheet1')
    #     for data in datas:
    #         pw = data['pw']
    #         if isinstance(pw, str):
    #             self._login(data['account'], pw, data['text'])
    #         else:
    #             int_str = str(int(pw))
    #             self._login(data['account'], int_str, data['text'])



