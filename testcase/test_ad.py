import time
from public.common import mytest
from public.pages import UtomarketLoginPage
from public.pages import UtomarketIndexPage
from public.common import datainfo


class TestLogin(mytest.MyLoginedTest):
    """utomarket登录测试"""
    def test_get_title(self):
        """封装登录"""
        print(self.dr.get_title())