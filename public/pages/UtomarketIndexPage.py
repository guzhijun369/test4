from public.common import basepage
from public.pages import UtomarketRegisterPage
from public.pages import UtomarketLoginPage
import time


class IndexPage(basepage.Page):

    def click_login_btn(self):
        """点击顶部登录按钮"""
        time.sleep(2)
        self.dr.click("link_text->登录")
        return UtomarketLoginPage.Login(self.dr)

    def click_register_btn(self):
        """点击顶部注册按钮"""
        time.sleep(2)
        self.dr.click("xpath->//span[contains(text(), '注 册')]//..")
        return UtomarketRegisterPage.Register(self.dr)