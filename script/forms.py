from django import forms
from script.models import Script,ScriptStep
from django.forms.widgets import TextInput
from uni_form.helper import FormHelper
from uni_form.helpers import Layout,Fieldset,ButtonHolder
from uni_form.layout import Submit

class ScriptForm(forms.ModelForm):
    class Meta:
        model =Script
        fields = ('name','type','category')
        widgets={'name':TextInput(attrs={'size':100})}


class ScriptStepForm(forms.ModelForm):
    class Meta:
        model=ScriptStep
        exclude = ['script','email']
