import  joblib
import pandas as pd
import numpy as np
from . import config
from sklearn import tree
from sklearn import metrics
from . import model_dispatcher
import argparse


def run(fold, model, project_name=None, file_path=None):
    """ fold: K fold number """

    # df = pd.read_csv(config.training_file())
    df = pd.read_csv(file_path)

    df_train = df[df.kfold != fold].reset_index(drop=True)

    df_valid = df[df.kfold == fold].reset_index(drop=True)

    # todo remove columns for unnamed ...
    # df_train = df_train.loc[:, ~df_train.columns.str.match("Unnamed")]

    # df_valid = df_train.loc[:, ~df_valid.columns.str.match("Unnamed")]

    x_train = df_train.drop(['label', 'kfold', 'Unnamed: 0'], axis=1).values
    y_train = df_train.label.values

    x_valid = df_valid.drop(['label', 'kfold', 'Unnamed: 0'], axis=1).values
    y_valid = df_valid.label.values

    clf = model_dispatcher.models[model]

    clf.fit(x_train, y_train)

    preds = clf.predict(x_valid)

    score = metrics.accuracy_score(y_valid, preds)

    # print('Score {0}, fold {1}', score, fold)

    # joblib.dump(config.models_path() + '/score-{0}-fold-{1}'.format(score, fold))

    model_file = '/model-{0},score-{1},fold-{2}.bin'.format(model, round(score * 100, 2), fold)
    path = config.models_path(project_name) + model_file

    # print('Model save path :', path)
    joblib.dump(clf, path)

    f1 = metrics.f1_score(y_valid, preds, average='micro')
    precision = metrics.precision_score(y_valid, preds, average='micro')
    recall = metrics.recall_score(y_valid, preds, average='micro')

    return {'model_file':model_file, 'model_name': model,
            'accuracy': score, 'f1': f1, 'precision': precision, 'recall': recall}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--fold', type=int)
    parser.add_argument('--model', type=str)

    args = parser.parse_args()
    run(fold=args.fold, model=args.model)
