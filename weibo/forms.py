from django import forms


class WeiboForm(forms.Form):
    text = forms.CharField(max_length=140)
