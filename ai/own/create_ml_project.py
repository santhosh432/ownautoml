import os
import argparse


def create_project(project):
    print('Started creating project ....', project)
    cwd = os.getcwd()
    print(cwd)
    absolute_path = os.path.abspath(__file__)
    p = os.path.dirname(absolute_path)

    print(p)
    try:
        os.makedirs(p + '/input/{0}'.format(project))
        os.makedirs(p + '/src/{0}'.format(project))
        os.makedirs(p + '/notebooks/{0}'.format(project))
        os.makedirs(p + '/models/{0}'.format(project))
    except FileExistsError:
        pass

    # for input only

    with open(p + '/input/{0}/train.csv'.format(project), 'w') as f:
        pass
    with open(p + '/input/{0}/test.csv'.format(project), 'w') as f:
        pass

    # for SRC only

    with open(p + '/src/{0}/create_folds.py'.format(project), 'w') as f:
        pass
    with open(p + '/src/{0}/train.py'.format(project), 'w') as f:
        pass
    with open(p + '/src/{0}/inference.py'.format(project), 'w') as f:
        pass
    with open(p + '/src/{0}/models.py'.format(project), 'w') as f:
        pass
    with open(p + '/src/{0}/config.py'.format(project), 'w') as f:
        pass
    with open(p + '/src/{0}/model_dispatcher.py'.format(project), 'w') as f:
        pass

    print('Project created successfully ..............')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--project", type=str)

    args = parser.parse_args()

    create_project(project=args.project)

