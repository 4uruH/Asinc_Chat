import sys
import logging
import DZ3.logs.config_server_log
import DZ3.logs.config_client_log
import traceback
import inspect

if sys.argv[0].find('client') == -1:
    log = logging.getLogger('server')
else:
    log = logging.getLogger('client')


def logger(func_to_log):

    def log_saver(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        log.debug(f'Called function {func_to_log.__name__} with arguments: {args}, {kwargs}. '
                  f'Called from module {func_to_log.__module__}. '
                  f'From function {traceback.format_stack()[0].strip().split()[-1]}. '
                  f'From function {inspect.stack()[1][3]}')
        return ret

    return log_saver
