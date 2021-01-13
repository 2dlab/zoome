import jwt


class ZoomClient:
    def __init__(self, api_key: str, secret_api_key: str, expired_time: int = 5400):
        self.api_key = api_key
        self.secret_api_key = secret_api_key
        self.expired_time = expired_time
        self.jwt = self.generate_jwt_token(self.expired_time)

    def generate_jwt_token(self, exp: int = 1496091964000):
        header = {"alg": "HS256", "typ": "JWT"}
        payload = {"iss": self.api_key, "exp": exp}
        signature = jwt.encode(payload, self.secret_api_key, algorithm="HS256", headers=header)
        return signature

    def get_conferences_list(self):
        pass


if __name__ == '__main__':
    print('use this code like import module')
