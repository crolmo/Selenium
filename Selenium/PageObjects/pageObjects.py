import os
from Common.utils import load_yaml,abs_path
from Base.Baselog import SeleniumLog
from Base.BaseEelement import Element
from Common.seleniumobj import check_keys


class Page(object):

    def __init__(self,path):
        config_path = abs_path(os.path.join("../",path))
        self.config = load_yaml(config_path)
        self.driver = Element()
        log_name = self.config["log_name"]
        log_path = abs_path(os.path.join('../log',log_name+".log"))
        self.logger = SeleniumLog(log_path)

    def operate(self,operate):
        info = ""
        if operate["mathod"] == "driver":
            info = self.driver.driver_operate(operate)
        elif operate["mathod"] == "mouse":
            info = self.driver.mouse_operate(operate)
        elif operate["mathod"] == "element":
            info = self.driver.element_operate(operate)
        elif operate["mathod"] == "get_element":
            info = self.driver.get_element_info(operate)
        return info

