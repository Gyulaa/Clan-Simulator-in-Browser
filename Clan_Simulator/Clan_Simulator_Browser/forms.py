from django import forms

# form tht adds new member
class AddMemberForm(forms.Form):
    name = forms.CharField(max_length=25)
    fatherid = forms.IntegerField()