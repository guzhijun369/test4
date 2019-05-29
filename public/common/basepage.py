# coding=utf-8
import time
from public.common.captcha import get_track
import cv2
from urllib import request
import numpy as np
from public.common.log import Log
logger = Log()


class Page(object):
    """
    This is a base page class for Page Object.
    """

    def __init__(self, selenium_driver):
        self.dr = selenium_driver

    def captcha(self):
        """滑动验证"""
        time.sleep(3)
        self.dr.switch_to_frame('id->tcaptcha_iframe')
        time.sleep(3)
        slide_btn = self.dr.get_element('id->tcaptcha_drag_thumb')
        times = 1
        y = self.getPic()
        while True:
            track = get_track(y)[6:]
            self.dr.drag_and_x(slide_btn, track, times)
            alert = self.dr.element_exist('id->tcaptcha_note')
            if alert and times < 10:
                y += 6
                times += 1
                time.sleep(2)
            elif alert and times >= 10:
                distance = 188
                times = 1
                time.sleep(2)
            else:
                # self.dr.switch_to_default_content()  # 验证成功后跳回最外层页面
                break

    def getPic(self):
        # 用于找到登录图片的大图
        bigimg = self.dr.get_element("id->slideBg").get_attribute("src")
        # 用来找到登录图片的小滑块
        smallimg = self.dr.get_element("id->slideBlock").get_attribute("src")
        # print(smallimg + '\n')
        # print(bigimg)
        # 背景大图命名
        backimg = "./img/backimg.png"
        # 滑块命名
        slideimg = "./img/slideimg.png"
        # 下载背景大图保存到本地
        request.urlretrieve(bigimg, backimg)
        # 下载滑块保存到本地
        request.urlretrieve(smallimg, slideimg)
        # 获取图片并灰度化
        block = cv2.imread(slideimg, 0)
        template = cv2.imread(backimg, 0)
        # 二值化后的图片名称
        blockName = "./img/block.jpg"
        templateName = "./img/template.jpg"
        # 将二值化后的图片进行保存
        cv2.imwrite(blockName, block)
        cv2.imwrite(templateName, template)
        block = cv2.imread(blockName)
        block = cv2.cvtColor(block, cv2.COLOR_RGB2GRAY)
        block = abs(255 - block)
        cv2.imwrite(blockName, block)
        block = cv2.imread(blockName)
        template = cv2.imread(templateName)
        # 获取偏移量
        result = cv2.matchTemplate(block, template,
                                   cv2.TM_CCOEFF_NORMED)  # 查找block在template中的位置，返回result是一个矩阵，是每个点的匹配结果
        x, y = np.unravel_index(result.argmax(), result.shape)
        # print("x方向的偏移", int(y * 0.4 + 18), 'x:', x, 'y:', y)
        logger.info('x的值是{}'.format(x))
        logger.info('y的值是{}'.format(y))
        return y*0.4+18

    def popup(self):
        """操作成功弹窗"""
        notice = self.dr.element_exist('css->.ant-message-custom-content>span')

        return notice
