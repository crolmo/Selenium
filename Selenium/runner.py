import unittest
from Common.HTMLTestRunner import HTMLTestRunner


from Base.BaseRunner import SeleniumRunner
from TestCase.HomePagetest import HomePagetest


def runnerCaseApp():
    suite = unittest.TestSuite()
    suite.addTest(SeleniumRunner.Runseleiumcase(HomePagetest))

    fp = open("Report/result.html", "wb")
    runner = HTMLTestRunner(stream=fp,
                title = "测试报告",
                description = "测试用例")
    runner.run(suite)
    fp.close()


if __name__ == '__main__':
    runnerCaseApp()