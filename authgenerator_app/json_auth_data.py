from json import dumps


class JsonAuthData:
    """JSON config data for data_logger application"""

    def __init__(self, api_key, api_hash, username, user_password):
        self.api_key = api_key
        self.api_hash = api_hash
        self.username = username
        self.user_password = user_password

    def __str__(self):
        return dumps(self.__dict__)
