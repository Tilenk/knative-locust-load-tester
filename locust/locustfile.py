from locust import HttpUser, task


class SimpleLoadTest(HttpUser):

    @task
    def index(self):
        self.client.get("/?sleep=100&prime=10000&bloat=50")