from PageObjects.HomePage.HomePage import HomePage
from Base.BaseRunner import SeleniumRunner


class HomePagetest(SeleniumRunner):

    def test_HomePage(self):
        test = HomePage(path="Config/HomePage.yaml")
        info = test.run()
        self.assertTrue(info)

    @classmethod
    def setUpClass(cls):
        super(HomePagetest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomePagetest, cls).tearDownClass()