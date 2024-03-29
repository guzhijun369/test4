#coding=utf-8

from public.common import basepage
import time


class Register(basepage.Page):

    def input_email(self, email):
        """输入邮箱"""
        self.dr.type('id->email', email)

    def get_code(self):
        """点击获取验证码"""
        self.dr.click("xpath->//span[contains(text(), '获取验证码')]//..")

    def input_code(self, code):
        """输入验证码"""
        self.dr.type('id->verify_code', code)

    def input_nickname(self, nickname):
        """输入用户名"""
        self.dr.clear_type('id->nickname', nickname)

    def input_pw(self, pw):
        """输入密码"""
        self.dr.type('id->password', pw)

    def input_confirm_pw(self, pw):
        """输入确认密码"""
        self.dr.type('id->confirm', pw)

    def click_area(self):
        """点击弹出国家下拉菜单"""
        self.dr.click("xpath->//div[contains(text(), '国家/地区')]//..")

    def select_country(self, country):
        """选择国家"""
        self.dr.click("xpath->//li[contains(text(), '{}')]".format(country))

    def click_box(self):
        """勾选同意"""
        self.dr.click('class->ant-checkbox')

    def click_res_btn(self):
        """点击注册"""
        self.dr.click("class->ant-btn-primary")

    def get_mail_text(self):
        """获取邮箱格式错误提示"""
        text = self.dr.get_text("class->ant-form-explain")

        return text

    def get_code_text(self):
        """获取验证码成功提现文案"""
        text = self.dr.get_text("class->ant-form-explain")

        return text

    def register_pass(self):
        """获取注册成功标识"""
        pass_div = self.dr.element_exist("xpath->//div[contains(text(), '注册成功')]")

        return pass_div

    def click_team_service(self):
        """点击服务条款"""
        self.dr.click("xpath->//a[contains(text(), '\"服务条款\"')]")

    def click_isclaimer(self):
        """点击免责声明"""
        self.dr.click("xpath->//a[contains(text(), '\"免责声明\"')]")

    def get_window(self):
        """获取点击弹窗"""
        title_text = self.dr.get_text("css->.ant-modal-title>span")

        return title_text

    def click_login_a(self):
        """点击使用已有账号登录"""
        self.dr.click("link_text->使用已有账户登录")

    def window_f5(self):
        """刷新注册页面"""
        self.dr.F5()
        time.sleep(1)

    # def into_utomarket_page(self):
    #    """打开乌托注册页面"""
    #    self.dr.open('https://otctest.utomarket.com/#/user/register')
    #
    # def get_captcha(self, distance, email):
    #     """输入邮箱点击获取验证码"""
    #     time.sleep(5)
    #     self.dr.type('id->email', email)
    #     self.dr.click("xpath->//span[contains(text(), '获取验证码')]//..")
    #     time.sleep(3)
    #     self.dr.captcha(distance)
    #
    # def register(self, code, nickname, password, country):
    #     """填写字段进行注册"""
    #     self.dr.type('id->verify_code', code)
    #     self.dr.type('id->nickname', nickname)
    #     self.dr.type('id->password', password)
    #     self.dr.type('id->confirm', password)
    #     self.dr.click("xpath->//div[contains(text(), '国家/地区')]//..")
    #     time.sleep(2)
    #     self.dr.click("xpath->//li[contains(text(), '{}')]".format(country))
    #     self.dr.click('class->ant-checkbox')
    #     self.dr.click("class->ant-btn-primary")
    #     time.sleep(3)
    #
    # def register_pass(self):
    #     """获取注册成功标识"""
    #     pass_div = self.dr.get_element("xpath->//div[contains(text(), '注册成功')]")
    #
    #     return pass_div