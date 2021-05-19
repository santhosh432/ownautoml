from django.shortcuts import render

# Create your views here.

from .forms import HeartDiseaseForm
from .own.src.heart_disease import inference
from .models import Project
import os
import pandas as pd


def heart_disease(request, pk):

    project = Project.objects.get(pk=pk)

    path = os.getcwd() + '/ai/own/input/{0}/train_fold.csv'.format(project.project_name.lower())

    df = pd.read_csv(path)
    df = df.sample(5)
    form = HeartDiseaseForm()

    p = None
    if request.GET:
        form = HeartDiseaseForm(request.GET)
        data = dict(request.GET)
        print('request data', data)
        data.pop('predict', None)
        p = inference.predict(data, '/model-DTEC,score-75.0,fold-4.bin')[0]


    return render(request, 'ai/predict.html', context={'form': form,
                                                             'p': p,
                                                             'project': project,
                                                             'df': df.to_html()
                                                             })
