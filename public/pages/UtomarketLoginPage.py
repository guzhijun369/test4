#coding=utf-8

from public.common import basepage
import time


class Login(basepage.Page):

    def input_account(self, account):
        """输入账号"""
        self.dr.type('id->account', account)

    def input_password(self, pw):
        """输入密码"""
        self.dr.type('id->password', pw)

    def click_login_btn(self):
        """点击登录按钮"""
        self.dr.click("xpath->//span[contains(text(), '登 录')]//..")

    def click_forget_password(self):
        """点击忘记密码按钮"""
        self.dr.click("link_text->忘记密码")

    def login(self, account, pw):
         """输入账号密码点击登录"""
         self.input_account(account)
         self.input_password(pw)
         time.sleep(2)
         self.click_login_btn()
         self.captcha(188)
    #
    # def go_captcha(self, distance):
    #     self.dr.captcha(distance)
    #
    # def error_text(self):
    #     error_span_text = self.dr.get_text('class->ant-alert-message')
    #
    #     return error_span_text
