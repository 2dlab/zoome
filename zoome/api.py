import json
import jwt
import os
import requests
import http.client
from datetime import datetime, timedelta


class ZoomClient:
    def __init__(self, api_key: str = '', secret_api_key: str = '',
                 expired_time: int = 1496091964000, jwt_token: str = ''):

        self.api_key = api_key
        self.secret_api_key = secret_api_key
        self.expired_time = expired_time
        self.jwt = jwt_token if jwt_token else self.generate_jwt_token(self.expired_time)

        self.conn = http.client.HTTPSConnection("api.zoom.us")
        self.headers = {
            "authorization": f"Bearer {self.jwt}",
            "content-type": "application/json"
        }

        self.user = self.get_user()

    def generate_jwt_token(self, exp: int = 1496091964000):
        if not self.api_key or not self.secret_api_key:
            raise Exception('api_key and secret_api_key - should be defined')

        header = {"alg": "HS256", "typ": "JWT"}
        payload = {"iss": self.api_key, "exp": exp}
        signature = jwt.encode(payload, self.secret_api_key, algorithm="HS256", headers=header)
        return signature

    def request(self, method: str, query: str):
        self.conn.request(method, query, headers=self.headers)
        data = self.conn.getresponse().read()
        return data.decode("utf-8")
    
    def get_user(self):
        res = json.loads(self.request("GET", "/v2/users?status=active&page_size=1&page_number=1"))

        if 'message' in res.keys():
            raise Exception(res['message'])

        return res["users"][0]

    def get_meetings_list(self, offset_days: int = 31, page_size: int = 100):
        from_date = datetime.date(datetime.now()) - timedelta(days=offset_days)
        query = f"/v2/users/{self.user['id']}/recordings?from={from_date}&page_size={page_size}"

        res = json.loads(self.request("GET", query))
        return res["meetings"]

    def download_file(self, full_path: str, url: str):
        res = requests.get(f"{url}?access_token={self.jwt}", stream=True)
        with open(full_path, "wb") as file:
            for chunk in res.iter_content(chunk_size=1024*1024):
                if chunk:
                    file.write(chunk)
                    file.flush()
                    os.fsync(file.fileno())


if __name__ == "__main__":
    print("use this code like import module")
