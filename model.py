from utils import *


def train(flags):
    info('--------train function----------')
    info(flags)
    debug('debug')
    info('info')
    warning('warning')
    error('error')

    model_name = get_model_name(flags)
    param_name = get_param_name(flags)
    log_name = get_log_name(flags)

    info('use {} for model name'.format(model_name))
    info('use {} for hyperparmeter name'.format(param_name))
    info('use {} for log name'.format(log_name))
    info('')
    info('Start Training!!')
    for i in range(10):
        info('iter {0}: MSE: {1:.2f}'.format(i, 1/(i+1)))


def test(flags):
    info('--------test function----------')


if __name__ == '__main__':
    flags = {
        # model parameters
        'n_neurons': [32, 64, 32],
        'use_skip_connection': True,

        # hyperparameters
        'batch_size': 32,
        'drop_rate': 0.8,
        'learning_rate': 0.001,

        # else
        'log_level': 'debug',
        'log_dir': 'logs',
    }
    flags = dotdict(flags)

    setup_log(flags)
    train(flags)
    test(flags)




