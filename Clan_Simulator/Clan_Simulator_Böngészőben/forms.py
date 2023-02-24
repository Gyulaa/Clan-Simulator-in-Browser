from django import forms

class AddMemberForm(forms.Form):
    name = forms.CharField(max_length=25)
    fatherid = forms.IntegerField()