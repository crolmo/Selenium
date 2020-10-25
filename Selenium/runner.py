import unittest
from Common.HTMLTestRunner import HTMLTestRunner


from Base.BaseRunner import SeleniumRunner
from TestCase.HomePagetest import HomePagetest


def runnerCaseApp():
    suite = unittest.TestSuite()
    suite.addTest(SeleniumRunner.Runseleiumcase(HomePagetest))
    SeleniumRunner.ReportRunner(suite,path="Report/result.html",title="测试报告",description="测试Home页面")


if __name__ == '__main__':
    runnerCaseApp()