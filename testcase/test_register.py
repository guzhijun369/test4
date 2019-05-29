#coding=utf-8

import time
from public.common import mytest
from public.pages import UtomarketRegisterPage
from public.pages import UtomarketIndexPage
from public.common import datainfo
from config import config


class TestRegister(mytest.MyTest):
    """utomarket注册页面"""
    def test_register(self):
        """正常注册"""
        u_index = UtomarketIndexPage.IndexPage(self.dr)
        u_register = u_index.click_register_btn()
        u_register.input_email(config.res_email)
        u_register.get_code()
        u_register.captcha()
        u_register.input_code('3201')
        u_register.input_nickname(config.res_nickname)
        u_register.input_pw('q5310543')
        u_register.input_confirm_pw('q5310543')
        u_register.click_area()
        u_register.select_country('中国')
        u_register.click_box()
        u_register.click_res_btn()
        pass_div = u_register.register_pass()
        self.assertTrue(pass_div, msg='查找注册成功标签识别失败')
