import logging


class SeleniumLog(object):

    def __init__(self,name):
        self.logger = logging.getLogger(__name__)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(processName)s - %(lineno)d - %(levelname)s - %(message)s')
        hd = logging.FileHandler(filename=name, mode='a', encoding='utf-8', delay=False)
        hd.setFormatter(self.formatter)
        self.logger.addHandler(hd)

    def debug(self,info):
        self.logger.setLevel(logging.DEBUG)
        return self.logger.debug(info)

    def error(self,info):
        self.logger.setLevel(logging.ERROR)
        return self.logger.error(info)

    def info(self,info):
        self.logger.setLevel(logging.INFO)
        return self.logger.info(info)

    def warning(self,info):
        self.logger.setLevel(logging.WARNING)
        return self.logger.warning(info)

