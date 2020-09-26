from django import forms
#
from .models import Directions

class DirectionsForm(forms.ModelForm):
    from_loc = forms.CharField(max_length=100, label='From: ', required=True)
    to_loc = forms.CharField(max_length=100, label='To: ', required=True)

    class Meta():
        model = BlogPost
        fields = ['from_loc', 'to_loc']