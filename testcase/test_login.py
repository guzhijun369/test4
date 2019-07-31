#coding=utf-8

import time
from public.common import mytest
from public.pages import UtomarketLoginPage
from public.pages import UtomarketIndexPage
from public.common import datainfo
from config.config import ConfigDate


class TestLogin(mytest.MyTest):
    """utomarket登录模块"""

    def test_login_ok(self):
        """正常登录"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_login = u_index.click_login_btn()
        u_login.login(ConfigDate.username, '3201')
        result = self.dr.get_title()
        self.assertIn('P2P交易 - 乌托市场(TEST)', result)

    def test_login_account_error(self):
        """正确账号错误密码登录"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_login = u_index.click_login_btn()
        u_login.login(ConfigDate.username_error, '3202')
        text = u_login.error_span_text()
        self.assertIn('错误', text)
        self.assertIn('机会尝试登录', text)
    def test_login_air(self):
        """不输入账号密码直接登录"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_login = u_index.click_login_btn()
        u_login.input_account('')
        u_login.input_password('')
        u_login.click_login_btn()
        texts = u_login.error_div_texts()
        self.assertListEqual(texts, ['请输入账户名！', '请输入密码！'])

    def test_jump_page(self):
        """登录页注册页面相互跳转"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_login = u_index.click_login_btn()
        time.sleep(3)
        u_login.register_a()
        u_res = u_login.return_register_page()
        reg_url = self.dr.get_url()
        self.assertIn('/user/register', reg_url)
        u_res.click_login_a()
        login_url = self.dr.get_url()
        self.assertIn('/user/login', login_url)

    def test_error_three(self):
        """密码错误四次"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_login = u_index.click_login_btn()
        for i in range(3):
            u_login.login(ConfigDate.pw_error_three, '3202')
            errors = str(5 - i)
            time.sleep(1)
            error_text = u_login.error_span_text()
            self.assertIn(errors, error_text)
        u_login.login(ConfigDate.pw_error_three, '3202')
        combo_window = u_login.combo_window()
        self.assertTrue(combo_window, msg="验证弹窗不存在")

    def test_error_six_email(self):
        """密码错误六次——>邮箱验证"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_login = u_index.click_login_btn()
        for i in range(3):
            u_login.login(ConfigDate.pw_error_six_email, '3202')
            errors = str(5 - i)
            time.sleep(1)
            error_text = u_login.error_span_text()
            self.assertIn(errors, error_text)
        for j in range(2):
            u_login.login(ConfigDate.pw_error_six_email, '3202')
            u_login.verify_identity_process("3201", "邮箱验证 ")
            errors_next = str(2 - j)
            time.sleep(1.5)
            error_text_next = u_login.error_span_text()
            self.assertIn(errors_next, error_text_next)
        u_login.login(ConfigDate.pw_error_six_email, '3202')
        u_login.verify_identity_process("3201", "邮箱验证 ")
        title = u_login.banned_window()
        self.assertIn("账号冻结通知", title)

    def test_error_six_phone(self):
        """密码错误六次——>手机验证"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_login = u_index.click_login_btn()
        for i in range(3):
            u_login.login(ConfigDate.pw_error_six_phone, '3202')
            errors = str(5 - i)
            time.sleep(1)
            error_text = u_login.error_span_text()
            self.assertIn(errors, error_text)
        for j in range(2):
            u_login.login(ConfigDate.pw_error_six_phone, '3202')
            u_login.verify_identity_process("3201", "手机验证 ")
            errors_next = str(2 - j)
            time.sleep(1.5)
            error_text_next = u_login.error_span_text()
            self.assertIn(errors_next, error_text_next)
        u_login.login(ConfigDate.pw_error_six_phone, '3202')
        u_login.verify_identity_process("3201", "手机验证 ")
        title = u_login.banned_window()
        self.assertIn("账号冻结通知", title)

    def test_error_three_true(self):
        """密码错误三次后密码正确"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_login = u_index.click_login_btn()
        for i in range(3):
            u_login.login(ConfigDate.pw_error_four_true, '3202')
            errors = str(5 - i)
            time.sleep(1)
            error_text = u_login.error_span_text()
            self.assertIn(errors, error_text)
        u_login.login(ConfigDate.pw_error_four_true, '3201')
        u_login.verify_identity_process("3201", "邮箱验证 ")
        time.sleep(2)
        result = self.dr.get_title()
        self.assertIn('P2P交易 - 乌托市场(TEST)', result)

    def test_login_error(self):
        """密码错误三次后验证错误"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_login = u_index.click_login_btn()
        for i in range(3):
            u_login.login(ConfigDate.login_error, '3202')
            errors = str(5 - i)
            time.sleep(1)
            error_text = u_login.error_span_text()
            self.assertIn(errors, error_text)
        u_login.login(ConfigDate.login_error, '3201')
        u_login.verify_identity_process("3202", "邮箱验证 ")
        time.sleep(1)
        pop_text = u_login.get_pop_error()
        self.assertIn('验证码错误或已失效', pop_text)

    def test_login_exist(self):
        """不存在的账号登录"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_login = u_index.click_login_btn()
        u_login.login(ConfigDate.username_exist, '3202')
        text = u_login.error_span_text()
        self.assertIn('错误', text)
        self.assertNotIn('机会尝试登录', text)



