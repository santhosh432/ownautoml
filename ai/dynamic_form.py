"""
dynamic form for prediction model

"""
from django import forms

column_type = {'s': forms.CharField(),
               'n': forms.FloatField(),
               'b': forms.BooleanField()
               }


class MyForm(forms.Form):
    pass


class DynamicForm:
    """ creating dynamic form for model """
    def __init__(self, df_columns):
        self.df = df_columns

    def dform(self):
        f = eval('MyForm')
        # print(f)
        for k, v in self.df.items():
            # print(k, v)

            if v == 'int64' or v == 'float64':
                fi = forms.FloatField()
                setattr(f, k, fi)
            else:
                fi = forms.CharField(max_length=50)
                setattr(f, k, fi)
        return f

