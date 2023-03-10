import sys
from socket import *
import time
from DZ3.config import DEFAULT_IP_ADDRESS, DEFAULT_PORT, ACTION
from DZ3.functions import get_message, send_message


def create_msg(action, username):
    data = {"action": action,
            "time": time.time(),
            "user": {"account_name": username}}

    return data


def server_response_cval(message):
    if 'response' in message:
        if message['response'] == 200:
            return '200 : OK'
        return f'400 : {message["error"]}'
    raise ValueError


def main():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((server_address, server_port))
    msg_to_send = create_msg(ACTION, "fantom")
    send_message(s, msg_to_send)
    server_response = get_message(s)
    server_response_cval(server_response)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
