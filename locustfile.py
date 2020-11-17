import time
from locust import HttpUser, task, between

# こうしないと、「httpアクセスは非推奨」という趣旨のログが大量に出る…
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class QuickstartUser(HttpUser):
    wait_time = between(5,7)

    @task(1)
    def index_abe_page(self):
        self.client.get("/contents/01070030")

    @task(1)
    def index_souri_page(self):
        self.client.get("/contents/00152860")

    # ランダムに実行されるタスクに重みづけが可能。@task({weight})
    @task(1)
    def view_item(self):
        for item_id in range(3):
            self.client.get(f"/theme/search/{item_id+1}", name="/thema")
            time.sleep(5)
    # @task
    # def test(self):
    #     a = 10
    #     self.client.get("/contents/01070030", name="abe")
    #     # self.client.get("/thema/search/1", name="thema1")

    def on_start(self):
        self.client.post("/login", json={"_token":"jjh1yKzwqYKL4ws8D49wwdcmxgyyVVVFkcIK3Ldf"}, verify=False)