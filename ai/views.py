from django.shortcuts import render

# Create your views here.

from .dynamic_form import DynamicForm
# from .own.src.heart_disease import inference
from .models import Project, ClassificationReport
import os
import pandas as pd
import sys
from django import forms
from ai.own.default import inference

def main_predict(request, pk):

    project = Project.objects.get(pk=pk)

    path = os.getcwd() + '/ai/own/input/{0}/train_fold.csv'.format(project.project_name.lower())
    # path = os.getcwd() + '/train_fold.csv'.format(project.project_name.lower())
    print(path)
    df = pd.read_csv(path)
    df = df.sample(5)

    # print(df.columns.values)
    # print(df.dtypes.to_dict())

    column_filter = {k: str(v) for k, v in df.dtypes.to_dict().items() if k not in ['Unnamed: 0', 'kfold', 'label']}

    print(column_filter)

    def fcolumn(c):
        d = {}
        for k, v in c.items():
            # print(k, v)

            if v == 'int64' or v == 'float64':
                fi = forms.FloatField()
                d[k] = fi
            else:
                fi = forms.CharField(max_length=50)
                d[k] = fi
                # setattr(f, k, fi)
        return d

    class MyForm(forms.Form):
        pass

    form = type('DynamicItemsForm', (MyForm,), fcolumn(column_filter))

    print('main form:', form)
    print('main form:', dir(form))
    # print('main form:', form.as_p())

    p = None

    # print(ClassificationReport.objects.filter(project_name__id=pk, activate=True))
    model_selection = ClassificationReport.objects.filter(project_name__id=pk, activate=True).first()
    # print(model_selection.model_path)

    if request.GET:

        path_model = os.getcwd() + '/ai/own/src/{0}'.format(project.project_name)
        # os.chdir(path_model)
        # sys.path.append(path_model)

        # import inference

        form = form(request.GET)
        data = dict(request.GET)
        # print('request data', data)
        data.pop('predict', None)
        # p = inference.predict(data, '/model-DTEC,score-75.0,fold-4.bin')[0]
        p = inference.predict(data, model_selection.model_path, project_name=project.project_name)[0]
        # sys.path.remove(path_model)
    print('Final predict:', p)
    return render(request, 'ai/predict.html', context={'form': form,
                                                        'p': p,
                                                        'project': project,
                                                        'df': df.to_html()
                                                        })
