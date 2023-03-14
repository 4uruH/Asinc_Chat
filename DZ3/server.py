from socket import *
import sys
import json
import argparse
import logging
import DZ3.logs.config_server_log
from DZ3.config import MAX_CONNECTIONS, DEFAULT_IP_ADDRESS, DEFAULT_PORT, ACTION
from DZ3.functions import get_message, send_message
from decorator import logger

server_log = logging.getLogger('server')


@logger
def client_msg_validation(message):
    server_log.debug(f'client message validation : {message}')
    if 'action' in message and message['action'] == ACTION and 'time' in message:
        return {'response': 200}
    return {
        'response': 400,
        'error': 'Bad Request'
    }


@logger
def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    return parser


@logger
def main():
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p

    if not 1023 < listen_port < 65536:
        server_log.critical(f'wrong port {listen_port}. available ports from 1024 to 65535.')
        sys.exit(1)
    server_log.info(f'server started on port: {listen_port}, awaiting connections from: {listen_address}.')

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((listen_address, listen_port))
    s.listen(MAX_CONNECTIONS)

    while True:
        client, addr = s.accept()
        try:
            client_msg = get_message(client)
            server_log.debug(f'received message from client {client_msg}')
            response = client_msg_validation(client_msg)
            send_message(client, response)
            server_log.debug(f'send message: {response} to client')
            client.close()
            server_log.info('connection close')

        except (ValueError, json.JSONDecodeError):
            server_log.error(f'cant decode a client message or wrong data from client {addr}')
            client.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
