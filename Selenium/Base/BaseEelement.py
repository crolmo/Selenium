# -*- coding: utf-8 -*-

from selenium import webdriver
from Common.seleniumobj import *


class Element(object):

    def __init__(self,browser="Chrome"):
        self.driver_path = select_driver(browser)
        self.driver = webdriver.Chrome(self.driver_path)

    def element_operate(self,operate):
        element_info = get_element_info(self.driver, operate)
        return element_info

    def driver_operate(self,operate):
        element_info = get_driver_info(self.driver, operate)
        return element_info

    def mouse_operate(self, operate):
        element_info = get_mouse_info(self.driver, operate)
        return element_info

    def get_element_info(self, operate):
        element_info = get_element(self.driver, operate)
        return element_info