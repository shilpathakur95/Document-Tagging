from django import forms
from testApp.models import Topics,Input

class TopicsForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ('topic','cutoff_25','cutoff_50','cutoff_75', 'data', )

class InputForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = ('input_class','input_content_type','input_content', )