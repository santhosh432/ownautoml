from django.shortcuts import render

# Create your views here.

from .forms import HeartDiseaseForm
from .own.src.heart_disease import inference

def heart_disease(request):

    form = HeartDiseaseForm()

    p = None
    if request.GET:
        data = dict(request.GET)
        print('request data', data)
        data.pop('predict', None)
        data['sex'] = 1
        p = inference.predict(data, '/model-DTEC,score-75.0,fold-4.bin')
        print(p)
    return render(request, 'ai/heart_predict.html', context = {'form': form, 'p':p})