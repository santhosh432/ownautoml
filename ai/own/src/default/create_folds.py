import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import manifold
from sklearn import model_selection
# import data_cleaning
import os
import config


def create_fold():
    # path = os.getcwd()
    # project = path.split('/')[-1]

    df = pd.read_csv(config.input_data())

    # df = data_cleaning.cleaning(df, 2)

    print('start folding ...')
    # print(df.head())
    df['kfold'] = -1

    df = df.sample(frac=1).reset_index(drop=True)

    kf = model_selection.KFold(n_splits=5)

    for fold, (trn_, val_) in enumerate(kf.split(X=df)):
        df.loc[val_, 'kfold'] = fold

    df.to_csv(config.training_file())
    print('Done...')

    return True


if __name__ == '__main__':

    create_fold()

