import sys
from socket import *
import time
import argparse
import logging
import DZ3.logs.config_client_log
from DZ3.config import DEFAULT_IP_ADDRESS, DEFAULT_PORT, ACTION
from DZ3.functions import get_message, send_message

log = logging.getLogger('client')


def create_msg(action, username):
    data = {"action": action,
            "time": time.time(),
            "user": {"account_name": username}}
    log.debug(f'user {username} create a {ACTION} message')
    return data


def server_response_cval(message):
    log.debug(f'server message: {message}')
    if 'response' in message:
        if message['response'] == 200:
            return '200 : OK'
        return f'400 : {message["error"]}'
    raise ValueError


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    return parser


def main():
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port
    if not 1023 < server_port < 65536:
        log.critical(f'server port error: {server_port}. server port must be from 1024 to 65535.')
        sys.exit(1)

    log.info(f'Client started: server: {server_address}, port: {server_port}')

    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((server_address, server_port))
        msg_to_send = create_msg(ACTION, "fantom")
        send_message(s, msg_to_send)
        server_response = get_message(s)
        log.info(f'message from server {server_response}')
        server_response_cval(server_response)
    except ConnectionRefusedError:
        log.critical(f'cant connect to serve {server_address}:{server_port}, connection refused.')


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
