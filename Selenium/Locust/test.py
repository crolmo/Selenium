from Locust.LocustRunner import LocustRunner
from locust import HttpUser, task, between
from locust.log import setup_logging

setup_logging("INFO", None)


class User(HttpUser):
    wait_time = between(1, 3)
    host = "https://music.163.com"

    @task(1)
    def Music_home(self):
        self.client.get("/")

    @task(2)
    def Music_Leaderboard(self):
        self.client.get("/#/discover/toplist")

    @task(1)
    def Music_MyMusic(self):
        self.client.get("/#/my/")


if __name__ == '__main__':
    LocustRunner().runlocust([User],10)