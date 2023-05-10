from django.forms import forms


class YourForm(forms.Form):

    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField()
    desc = forms.CharField(label='name', max_length=100)

