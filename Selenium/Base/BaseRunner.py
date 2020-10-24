import unittest


class SeleniumRunner(unittest.TestCase):

    def __init__(self, methodName='runTest',param=None):
        super(SeleniumRunner, self).__init__(methodName)

    @staticmethod
    def Runseleiumcase(testcase_class, param=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_class(name, param=param))
        return suite