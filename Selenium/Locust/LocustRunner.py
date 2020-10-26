import gevent
from locust.env import Environment
from locust.env import Environment
from locust.stats import stats_printer, stats_history


class LocustRunner(object):

    def runlocust(self,user,user_count):
    # setup Environment and Runner
        env = Environment(user_classes=user)
        env.create_local_runner()

        # start a WebUI instance
        env.create_web_ui("127.0.0.1", 8089)

        # start a greenlet that periodically outputs the current stats
        gevent.spawn(stats_printer(env.stats))

        # start a greenlet that save current stats to history
        gevent.spawn(stats_history, env.runner)

        # start the test
        env.runner.start(user_count, spawn_rate=10)

        # in 60 seconds stop the runner
        gevent.spawn_later(60, lambda: env.runner.quit())

        # wait for the greenlets
        env.runner.greenlet.join()

        # stop the web server for good measures
        env.web_ui.stop()