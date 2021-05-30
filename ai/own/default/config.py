# coding=utf-8
import os

TRAINING_FILE = '../../input/train_folds.csv'

MODELS = '../models/'

DIR = os.path.dirname(os.path.abspath(__file__))


def input_data(file_name='train_data.csv', train_path=None, project=None):
    """
    :param file_name: input CSV file name with all semesters.
    :return: full pah
    """
    # DIR = DIR
    p = DIR + '/{0}'.format(file_name)
    p = p.replace('src', 'input')
    # print('input data', p)

    return p


def models_path(project_name=None):

    p = DIR
    # print('Model path DIR', p)
    p = p.replace('default', '')
    p = p.replace('src', 'models') + '/models/{0}'.format(project_name)

    return p


def training_file(train_path=None):

    p = DIR + '/{0}'.format('train_fold.csv')
    p = p.replace('src', 'input')
    # print('input data', p)
    return p


if __name__ == '__main__':
    # input_data('FinalMarksGPA-2021-04-15(1).csv')
    # models_path()
    pass

