#coding=utf-8

import time
from public.common import mytest
from public.pages import UtomarketRegisterPage
from public.pages import UtomarketIndexPage
from public.common import datainfo
from config.config import ConfigDate


class TestRegister(mytest.MyTest):
    """utomarket注册页面"""
    def test_register_errorcode(self):
        """输入错误的验证码注册"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_register = u_index.click_register_btn()
        u_register.input_email(ConfigDate.res_email)
        u_register.get_code()
        u_register.captcha()
        text = u_register.get_code_text()
        self.assertIn('验证码已经发送至您的邮箱，请注意查收', text)
        u_register.input_code('3202')
        u_register.input_nickname(ConfigDate.res_nickname)
        u_register.input_pw('q5310543')
        u_register.input_confirm_pw('q5310543')
        u_register.click_area()
        u_register.select_country('中国')
        u_register.click_box()
        u_register.click_res_btn()
        text = u_register.get_code_text()
        self.assertEqual('验证码错误或已失效', text)

    def test_register(self):
        """正常注册"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_register = u_index.click_register_btn()
        u_register.input_email(ConfigDate.res_email)
        u_register.get_code()
        u_register.captcha()
        text = u_register.get_code_text()
        self.assertIn('验证码已经发送至您的邮箱，请注意查收', text)
        u_register.input_code('3201')
        u_register.input_nickname(ConfigDate.res_nickname)
        u_register.input_pw('q5310543')
        u_register.input_confirm_pw('q5310543')
        u_register.click_area()
        u_register.select_country('中国')
        u_register.click_box()
        u_register.click_res_btn()
        pass_div = u_register.register_pass()
        self.assertTrue(pass_div, msg='查找注册成功标签识别失败')

    def test_register_email_air(self):
        """不输入邮箱直接点击获取验证码"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_register = u_index.click_register_btn()
        u_register.input_email('')
        u_register.get_code()
        text = u_register.get_mail_text()
        self.assertEqual('请输入邮箱地址！', text)

    def test_register_email_error(self):
        """输入错误格式邮箱点击获取验证码"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_register = u_index.click_register_btn()
        u_register.input_email('5646578@')
        u_register.get_code()
        text = u_register.get_mail_text()
        self.assertEqual('邮箱地址格式错误', text)

    def test_register_email_old(self):
        """输入已注册邮箱点击获取验证码"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_register = u_index.click_register_btn()
        u_register.input_email(ConfigDate.res_email)
        u_register.get_code()
        u_register.captcha()
        time.sleep(1)
        text = u_register.get_mail_text()
        self.assertEqual('该邮箱已被注册，请更换其他邮箱', text)

    def test_register_nickname_air(self):
        """不输入用户名"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_register = u_index.click_register_btn()
        u_register.input_nickname('')
        u_register.click_box()
        time.sleep(1)
        text = u_register.get_mail_text()
        self.assertEqual('请输入2-8个字符，设置后不可更改！', text)

    def test_register_nickname_error(self):
        """输入错误格式的用户名"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_register = u_index.click_register_btn()
        for i in ConfigDate.error_nickname:
            u_register.input_nickname(i)
            u_register.click_box()
            time.sleep(1)
            text = u_register.get_mail_text()
            self.assertEqual('用户名只能包含 2~8位的字母，数字，下划线，减号', text)
            u_register.window_f5()

