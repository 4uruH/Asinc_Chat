import sys
import os
import logging

sys.path.append('../')

_format = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

absolut_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolut_path, 'server.log')

msg_hand = logging.StreamHandler(sys.stderr)
msg_hand.setFormatter(_format)
msg_hand.setLevel(logging.ERROR)
file_hand = logging.FileHandler(file_path, encoding='utf8')
file_hand.setFormatter(_format)

log = logging.getLogger('server')
log.addHandler(msg_hand)
log.addHandler(file_hand)
log.setLevel(logging.DEBUG)
