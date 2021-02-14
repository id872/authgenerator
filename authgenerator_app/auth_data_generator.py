from hashlib import sha256, sha1
from random import choice
from string import printable


def get_random_string(string_len):
    return ''.join(choice(printable[:63]) for _ in range(string_len))


class AuthDataGenerator:
    """ Authentication data generator for data monitor application"""
    API_KEY = sha256(get_random_string(10000).encode()).hexdigest()
    API_HASH = sha1(get_random_string(10000).encode()).hexdigest()
    USERNAME = 'DevMonitorUserNameSomething'
    PASSWORD = get_random_string(50)
