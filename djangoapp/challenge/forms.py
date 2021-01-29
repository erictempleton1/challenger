from django import forms
from challenge.models import Challenge, Activity


class ChallengeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'input is-primary',
            'placeholder': 'My Awesome Challenge!'
        })

    class Meta:
        model = Challenge
        fields = ['name']

class ActivityForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['distance'].widget.attrs.update({
            'class': 'input is-primary'
        })
        self.fields['measure'].widget.attrs.update({
            'class': 'input is-primary',
        })
        self.fields['hours'].widget.attrs.update({
            'class': 'input is-primary',
        })
        self.fields['minutes'].widget.attrs.update({
            'class': 'input is-primary',
        })
        self.fields['seconds'].widget.attrs.update({
            'class': 'input is-primary',
        })

    class Meta:
        model = Activity
        fields = ['activity', 'distance', 'measure', 'hours', 'minutes', 'seconds']