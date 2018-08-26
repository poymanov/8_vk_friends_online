import vk
import sys
import os
from getpass import getpass
from dotenv import load_dotenv


def get_api_credentials():
    load_dotenv(os.path.join(os.path.dirname(__name__), '.env'))
    return {'app_id': os.getenv('APP_ID'), 'version': os.getenv('VERSION')}


def get_user_login():
    login = input('Enter your VK login: ')
    return login


def get_user_password():
    password = getpass(prompt='Enter your VK password: ')
    return password


def get_api_session(login, password):
    api_credentials = get_api_credentials()

    try:
        session = vk.AuthSession(
            app_id=api_credentials['app_id'],
            user_login=login,
            user_password=password,
            scope='friends'
        )
        return vk.API(session, version=api_credentials['version'])
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
    login = get_user_login()
    password = get_user_password()

    api_session = get_api_session(login, password)

    if not api_session:
        sys.exit('Failed to connect to VK. ' +
                 'Make sure you have entered the correct login/password.')

    friends_online = get_online_friends(api_session)

    if not friends_online:
        sys.exit('There are no users online')

    output_friends_to_console(friends_online)
