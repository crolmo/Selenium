import traceback
from PageObjects.pageObjects import Page
from Common.seleniumobj import check_keys


class MusicHome(Page):

    def run(self):
        self.logger.info("开始执行测试：{}".format(MusicHome.__name__))
        for operate_info in self.config["testcase"]:
            try:
                check_info = check_keys(operate_info)
                if check_info:
                    for info in check_info:
                        self.logger.error(info)
                    continue
                else:
                    info = self.operate(operate_info)
                    for element in info:
                        print(element)
            except Exception as e:
                self.logger.error(e)
                self.logger.error(traceback.format_exc())
        self.logger.info("测试结束:{}".format(MusicHome.__name__))
        return True


if __name__ == '__main__':
    test = MusicHome(path="Config/MusicHome.yaml")
    test.run()