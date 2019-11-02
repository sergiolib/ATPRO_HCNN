import argparse
import os
from datetime import datetime
from datasets import get_cifar100


def get_model_directory():
    model_directory = args.model
    if model_directory == '':
        now = datetime.now()
        timestamp = now.strftime('%Y%m%d%H%M%S')
        model_directory = f'./saved_models/{args.name}/{timestamp}'
    os.makedirs(model_directory, exist_ok=True)
    return model_directory


def get_logs_directory():
    logs_dir = "./logs"
    os.makedirs(logs_dir, exist_ok=True)
    return logs_dir


def get_data(dataset):
    if dataset == 'cifar100':
        tr, val, te = get_cifar100()
    return tr, val, te


def main(args):
    logs_directory = get_logs_directory()
    model_directory = get_model_directory()
    training_data, validation_data, test_data = get_data(args.dataset)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='HDCNN baseline running script'
    )

    parser.add_argument('-tr', '--train', help='Train a new model',
                        action='store_true')
    parser.add_argument('-te', '--test', help='Test a model',
                        action='store_true')
    parser.add_argument('-m', '--model', help='Specify where to store model',
                        type=str, default='')
    parser.add_argument('-n', '--name', help='Model run name',
                        type=str, default='baseline_hdcnn')
    parser.add_argument('-d', '--dataset', help='Dataset to use',
                        type=str, default='cifar100',
                        choices=['cifar100'])

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
