from uuid import uuid4

from locust import HttpUser, task


class MyUser(HttpUser):
    @task
    def my_task(self):
        self.client.post("/api/", data={"payload": uuid4().hex})
