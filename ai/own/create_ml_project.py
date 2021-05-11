import os
import argparse


def create_project(project):
    print('Started creating project ....', project)

    try:
        os.makedirs('./input/{0}'.format(project))
        os.makedirs('./src/{0}'.format(project))
        os.makedirs('./notebooks/{0}'.format(project))
        os.makedirs('./models/{0}'.format(project))
    except FileExistsError:
        pass

    with open('./src/{0}/create_folds.py'.format(project), 'w') as f:
        pass
    with open('./src/{0}/train.py'.format(project), 'w') as f:
        pass
    with open('./src/{0}/inference.py'.format(project), 'w') as f:
        pass
    with open('./src/{0}/models.py'.format(project), 'w') as f:
        pass
    with open('./src/{0}/config.py'.format(project), 'w') as f:
        pass
    with open('./src/{0}/model_dispatcher.py'.format(project), 'w') as f:
        pass

    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--project", type=str)

    args = parser.parse_args()

    create_project(project=args.project)

