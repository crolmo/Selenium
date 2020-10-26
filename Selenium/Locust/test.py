from Locust.LocustRunner import LocustRunner
from locust import HttpUser, task, between
from locust.log import setup_logging

setup_logging("INFO", None)


class User(HttpUser):
    wait_time = between(1, 3)
    host = "https://docs.locust.io"

    @task
    def my_task(self):
        self.client.get("/")


if __name__ == '__main__':
    LocustRunner().runlocust([User],10)