import time
import os
import logging
from logging import debug, info, warning, error


def get_model_name(flags):
    return 'nn{}-sc{}'.format('_'.join(str(x) for x in flags.n_neurons),  flags.use_skip_connection)


def get_param_name(flags):
    return 'bs{}-dr{}-lr{}'.format(flags.batch_size, flags.drop_rate, flags.learning_rate)


def get_time():
    now = time.localtime()
    return "%02d_%02d_%02d_%02d_%02d" % (now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)


def get_log_name(flags):
    return get_model_name(flags) + '-' + get_param_name(flags) + '-' + get_time()


def _covert_str_to_level(flags):
    if flags.log_level == 'debug':
        log_level = logging.DEBUG
    elif flags.log_level == 'info':
        log_level = logging.INFO
    elif flags.log_level == 'warning':
        log_level = logging.WARNING
    elif flags.log_level == 'error':
        log_level = logging.ERROR
    return log_level


def setup_log(flags):
    os.makedirs(flags.log_dir, exist_ok=True)
    log_name = get_log_name(flags)
    log_path = os.path.join(flags.log_dir, log_name)

    logging.root.handlers = []
    log_format = '%(asctime)s %(levelname)s - %(message)s'
    log_datefmt = '%d-%b-%y %H:%M:%S'
    log_level = _covert_str_to_level(flags)

    logging.basicConfig(format=log_format, datefmt=log_datefmt, level=log_level, filename=log_path, filemode='w')
    console = logging.StreamHandler()
    console.setLevel(log_level)
    formatter = logging.Formatter(log_format, datefmt=log_datefmt)
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
