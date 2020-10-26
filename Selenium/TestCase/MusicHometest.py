from PageObjects.Muisc.MusicHome import MusicHome
from Base.BaseRunner import SeleniumRunner


class MusicHometest(SeleniumRunner):

    def test_MusicHome(self):
        test = MusicHome(path="Config/MusicHome.yaml")
        info = test.run()
        self.assertTrue(info)

    @classmethod
    def setUpClass(cls):
        super(MusicHometest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(MusicHometest, cls).tearDownClass()