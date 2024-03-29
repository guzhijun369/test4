#coding=utf-8

from public.common import basepage
import time
from . import UtomarketRegisterPage


class Login(basepage.Page):

    def input_account(self, account):
        """输入账号"""
        self.dr.clear_type('id->account', account)

    def input_password(self, pw):
        """输入密码"""
        self.dr.clear_type('id->password', pw)

    def click_login_btn(self):
        """点击登录按钮"""
        time.sleep(1.5)
        self.dr.click("xpath->//span[contains(text(), '登 录')]//..")

    def click_forget_password(self):
        """点击忘记密码按钮"""
        self.dr.click("link_text->忘记密码")

    def error_span_text(self):
        """获取错误文案"""
        error_text = self.dr.get_text('class->ant-alert-message')

        return error_text

    def error_div_texts(self):
        """获取错误文案div,复数"""
        time.sleep(1)
        error_texts = self.dr.get_elements('class->ant-form-explain')
        texts = []
        for i in error_texts:
            texts.append(i.text)

        return texts

    def combo_window(self):
        """获取验证弹窗"""
        result = self.dr.element_exist("xpath->//div[text()='身份验证']")

        return result

    def get_code(self):
        """密码错误三次后点击获取验证码"""
        self.dr.click("xpath->//span[contains(text(), '获取验证码')]//..")

    def click_combobox(self):
        """点击验证方式"""
        self.dr.click("xpath->//div[@role='combobox']")

    def pik_type(self, way):
        """选择验证类型"""
        self.dr.click("xpath->//li[contains(text(), '{}')]".format(way))

    def input_code(self, code):
        """输入验证码"""
        self.dr.type('id->code', code)

    def click_fixe(self):
        """点击确定"""
        self.dr.click("xpath->//span[contains(text(), '确 定')]//..")

    def banned_window(self):
        """封禁弹窗"""
        banned_text = self.dr.get_text("class->ant-confirm-title")

        return banned_text

    def register_a(self):
        """点击注册账户按钮"""
        self.dr.click("link_text->注册账户")

    def get_pop_error(self):
        """获取操作失败弹窗"""
        text = self.popup_error()

        return text

    def return_register_page(self):
        """输出注册页面对象"""
        return UtomarketRegisterPage.Register(self.dr)

    def verify_identity_process(self, code, types):
        """验证身份流程"""
        self.click_combobox()
        time.sleep(1)
        self.pik_type(types)
        self.get_code()
        time.sleep(2)
        self.input_code(code)
        self.click_fixe()

    def login(self, account, pw):
        """输入账号密码点击登录"""
        self.input_account(account)
        self.input_password(pw)
        self.click_login_btn()
        self.captcha()
        time.sleep(1)
    #
    # def go_captcha(self, distance):
    #     self.dr.captcha(distance)
    #
    # def error_text(self):
    #     error_span_text = self.dr.get_text('class->ant-alert-message')
    #
    #     return error_span_text
