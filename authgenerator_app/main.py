from os import path, makedirs, remove

from auth_data_generator import AuthDataGenerator
from json_auth_data import JsonAuthData
from sql_auth_data import SqlAuthData


def write_config_file(file_name, content):
    current_dir = path.dirname(path.abspath(__file__))
    out_dir = path.join(current_dir, 'configuration')

    if not path.exists(out_dir):
        makedirs(out_dir)

    file_path = path.join(out_dir, file_name)

    if path.exists(file_path):
        remove(file_path)

    with open(file_path, 'w') as config_file:
        config_file.write(content)


def main():
    json_auth_data = JsonAuthData(AuthDataGenerator.API_KEY, AuthDataGenerator.API_HASH,
                                  AuthDataGenerator.USERNAME, AuthDataGenerator.PASSWORD)
    sql_auth_data = SqlAuthData(AuthDataGenerator.API_KEY, AuthDataGenerator.API_HASH,
                                AuthDataGenerator.USERNAME, AuthDataGenerator.PASSWORD)
    write_config_file('auth_data.json', str(json_auth_data))
    write_config_file('sql_users.sql', str(sql_auth_data))


if __name__ == "__main__":
    main()
