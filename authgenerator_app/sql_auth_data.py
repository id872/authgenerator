from bcrypt import gensalt, hashpw


def get_bcrypt_hash(user_pass):
    return hashpw(user_pass.encode(), gensalt())


class SqlAuthData:
    """SQL data for users table for devmon application"""

    def __init__(self, api_key, api_hash, username, user_password, ):
        self.api_key = api_key
        self.api_hash = api_hash
        self.username = username
        self.user_password_hash = get_bcrypt_hash(user_password).decode()

    def __str__(self):
        return "INSERT INTO `users` (`user_name`, `user_password_hash`, `api_key`, `api_hash`) VALUES\n" \
               "('{}', '{}', '{}', '{}');".format(self.username, self.user_password_hash, self.api_key, self.api_hash)
