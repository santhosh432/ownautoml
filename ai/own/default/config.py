# coding=utf-8
import os

TRAINING_FILE = '../../input/train_folds.csv'

MODELS = '../models/'

DIR = os.path.dirname(os.path.abspath(__file__))

print('DIR', DIR)


def input_data(file_name='train_data.csv', project=None):
    """
    :param file_name: input CSV file name with all semesters.
    :return: full pah
    """
    # DIR = DIR
    p = DIR + '/{0}'.format(file_name)
    p = p.replace('src', 'input')
    print('input data', p)

    return p


def models_path():

    p = DIR
    p = p.replace('src', 'models')

    return p


def training_file():

    p = DIR + '/{0}'.format('train_fold.csv')
    p = p.replace('src', 'input')
    print('input data', p)
    return p


if __name__ == '__main__':
    # input_data('FinalMarksGPA-2021-04-15(1).csv')
    # models_path()
    pass

