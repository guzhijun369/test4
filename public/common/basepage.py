# coding=utf-8
import time
from UItestframework.public.common.captcha import get_track


class Page(object):
    """
    This is a base page class for Page Object.
    """

    def __init__(self, selenium_driver):
        self.dr = selenium_driver

    def captcha(self, distance):
        """滑动验证"""
        time.sleep(3)
        self.dr.switch_to_frame('id->tcaptcha_iframe')
        time.sleep(3)
        slide_btn = self.dr.get_element('id->tcaptcha_drag_thumb')
        times = 1
        while True:
            track = get_track(distance)[6:]
            self.dr.drag_and_x(slide_btn, track, times)
            alert = self.dr.element_exist('id->tcaptcha_note')
            if alert and times < 10:
                distance += 6
                times += 1
                time.sleep(2)
            elif alert and times >= 10:
                distance = 188
                times = 1
                time.sleep(2)
            else:
                # self.dr.switch_to_default_content()  # 验证成功后跳回最外层页面
                break

    def popup(self):
        """操作成功弹窗"""
        notice = self.dr.element_exist('css->.ant-message-custom-content>span')

        return notice
