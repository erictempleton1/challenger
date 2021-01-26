from django import forms
from challenge.models import Challenge


class ChallengeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'input is-primary'
        }

    class Meta:
        model = Challenge
        fields = ['name']
