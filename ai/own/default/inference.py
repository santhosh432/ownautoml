import os
import joblib
import pandas as pd

DIR = os.path.dirname(os.path.abspath(__file__))


def predict(data, model, project_name=None):
    model_path = DIR.replace('src', 'models')
    # print(model_path)
    model_path = model_path + model
    # print('default:', model_path)

    model_path = model_path.replace('default', 'models/{0}'.format(project_name))
    m = joblib.load(model_path)

    return m.predict(pd.DataFrame(data))

