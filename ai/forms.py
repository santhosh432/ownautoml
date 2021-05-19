from django import forms




"""
age
sex
chest pain type (4 values)
resting blood pressure
serum cholestoral in mg/dl
fasting blood sugar > 120 mg/dl
resting electrocardiographic results (values 0,1,2)
maximum heart rate achieved
exercise induced angina
oldpeak = ST depression induced by exercise relative to rest
the slope of the peak exercise ST segment
number of major vessels (0-3) colored by flourosopy
thal: 3 = normal; 6 = fixed defect; 7 = reversable defect

"""


class HeartDiseaseForm(forms.Form):
    age = forms.FloatField()
    sex = forms.BooleanField(widget= forms.CheckboxInput(), required=False)
    cp = forms.FloatField()
    rp = forms.FloatField()
    sc = forms.FloatField()
    fbd = forms.FloatField()
    rer = forms.FloatField()
    mhra = forms.FloatField()
    eia = forms.FloatField()
    op = forms.FloatField()
    sp = forms.FloatField()
    nmv = forms.FloatField()
    th = forms.FloatField()



