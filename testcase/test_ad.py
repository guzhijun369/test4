import time
from UItestframework.public.common import mytest
from UItestframework.public.pages import UtomarketLoginPage
from UItestframework.public.pages import UtomarketIndexPage
from UItestframework.public.common import datainfo


class TestLogin(mytest.MyLoginedTest):
    """utomarket登录测试"""
    def test_get_title(self):
        """封装登录"""
        print(self.dr.get_title())