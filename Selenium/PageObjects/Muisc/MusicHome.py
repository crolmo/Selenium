import traceback
import time
from PageObjects.pageObjects import Page
from Common.seleniumobj import check_keys


class MusicHome(Page):

    def run(self):
        self.logger.info("开始执行测试：{}".format(MusicHome.__name__))
        error_info = ""
        for doperate in self.config["testcase"]:
            time.sleep(1)
            try:
                check_info = check_keys(doperate)
                if check_info:
                    for info in check_info:
                        self.logger.error(info)
                    continue
                else:
                    info = self.operate(doperate)
            except Exception as e:
                error_info = e
                self.logger.error(e)
                self.logger.error(traceback.format_exc())
        self.logger.info("测试结束:{}".format(MusicHome.__name__))
        if error_info:
            return False
        else:
            return True


if __name__ == '__main__':
    test = MusicHome(path="Config/MusicHome.yaml")
    test.run()