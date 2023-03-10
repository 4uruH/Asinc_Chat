from socket import *
import sys
import json
from DZ3.config import MAX_CONNECTIONS, DEFAULT_IP_ADDRESS, DEFAULT_PORT, ACTION
from DZ3.functions import get_message, send_message


def client_msg_validation(message):
    if 'action' in message and message['action'] == ACTION and 'time' in message:
        return {'response': 200}
    return {
        'response': 400,
        'error': 'Bad Request'
    }


def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('не указан номер порта  -\'p\' ')
        sys.exit(1)
    except ValueError:
        print(
            'номер порта в диапазоне 1024 до 65535.')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        print(
            ' \'a\'- IP адрес для прослушивания')
        sys.exit(1)
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((listen_address, listen_port))
    s.listen(MAX_CONNECTIONS)

    while True:
        client, addr = s.accept()
        try:
            client_msg = get_message(client)
            print(client_msg)
            response = client_msg_validation(client_msg)
            send_message(client, response)
            client.close()

        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
