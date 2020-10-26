import unittest
from Base.BaseRunner import SeleniumRunner
from TestCase.MusicHometest import MusicHometest


def runnerCaseApp():
    suite = unittest.TestSuite()
    suite.addTest(SeleniumRunner.Runseleiumcase(MusicHometest))
    SeleniumRunner.ReportRunner(suite,path="Report/{}.html".format(MusicHometest.__name__),title="测试报告",description="测试Home页面")


if __name__ == '__main__':
    runnerCaseApp()