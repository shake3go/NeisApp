from django.forms import ModelForm
from NeisAssistant.models import Teachers

class Form(ModelForm):
    class Meta:
        model = Teachers
        fields = ['tId', 'tName', 'tPwd', 'authority', 'gradeNo', 'classNo', 'createId', 'updateId' ]

