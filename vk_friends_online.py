import vk
import sys
import os
import argparse
from getpass import getpass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('app_id', help='VK APP ID')
    parser.add_argument('--api_version', help='VK API Version', default='5.80')
    return parser.parse_args()


def get_user_login():
    login = input('Enter your VK login: ')
    return login


def get_user_password():
    password = getpass(prompt='Enter your VK password: ')
    return password


def get_api_session(login, password, app_id, api_version):
    try:
        session = vk.AuthSession(
            app_id=app_id,
            user_login=login,
            user_password=password,
            scope='friends'
        )
        return vk.API(session, version=api_version)
    except vk.exceptions.VkAuthError:
        return None


def get_online_friends(api_session):
    friends_online_ids = api_session.friends.getOnline()
    return api_session.users.get(user_ids=friends_online_ids)


def output_friends_to_console(friends_online):
    print('Users online:')
    for friend in friends_online:
        print('{} {}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    args = parse_args()

    login = get_user_login()
    password = get_user_password()

    api_session = get_api_session(login, password,
                                  args.app_id, args.api_version)

    if not api_session:
        sys.exit(('Failed to connect to VK. '
                  'Make sure you have entered the correct login/password.'))

    friends_online = get_online_friends(api_session)

    if not friends_online:
        sys.exit('There are no users online')

    output_friends_to_console(friends_online)
