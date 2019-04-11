import model
import argparse
from utils import setup_log


def main():
    parser = argparse.ArgumentParser(description='Code Template')

    # model
    parser.add_argument('-nn', '--n_neurons', type=int, nargs='+', default=[32, 64], help='number of neurons (default: [32, 64])')
    parser.add_argument('-sc', '--use_skip_connection', action='store_true', default=False, help='use skip connection (default: False)')

    # hyperparameter
    parser.add_argument('-b', '--batch_size', type=int, default=32, help='batch size (default: 32)')
    parser.add_argument('-dr', '--drop_rate', type=float, default=0.8, help='drop rate (default: 0.8)')
    parser.add_argument('-lr', '--learning_rate', type=float, default=0.001, help='learning rate (default: 0.001)')

    # else
    parser.add_argument('--log_dir', default='logs', help='log directory to save')
    parser.add_argument('--log_level', default='debug', choices=['debug', 'info', 'warning', 'error'],
                        help='default: debug')

    flags = parser.parse_args()
    setup_log(flags)

    model.train(flags)
    model.test(flags)

    # TODO: add to do


if __name__ == '__main__':
    main()
