import time
from locust import HttpUser, task, between


# * This class inherits from HttpUser which gives each user a client attribute, which is an instance of HttpSession, that can be used to make HTTP requests to the target system
# * locust will create instance of this class for every user it simulates (running within their own geen gevent thread)
class QuickStartUser(HttpUser):
    # Simulated users wait between x..y after each task is executed. Three build-ins constant, between, constant_pacing
    wait_time = between(1, 3)

    # * For every running user, Locust creates a greenlet(micro-thread), that will call @task methods.
    # * Tasks are picked at random, but you can give them different weighting.When a task has finished executing, the User will then sleep during it’s wait time.  After it’s wait time it’ll pick a new task and keep repeating that.
    # ! only methods decorated with @task will be picked
    @task
    def hello_world(self):
        self.client.get("helloworld")
