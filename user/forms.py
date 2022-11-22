from email.policy import default
from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter Name'})
    mobileno = forms.CharField(error_messages={'requird':'Enter mobile no'})
    email = forms.CharField(error_messages={'requird':'Enter email '})
   # message = forms.CharField(error_messages={'requird':'Enter message '})
    message = forms.CharField(error_messages={'requird':'Enter message '},widget=forms.Textarea(attrs={'cols': 50, 'rows': 7}))
    

    #custom validation logic
    #def clean(self):
    #    cleaned_data = super().clean()
    #    valname = self.cleaned_data['name']
    #    valemail = self.cleaned_data['email']
    #    if len(valname)<4:
    #        raise forms.ValidationError("Name should be more than or equal 4")
    #    if len(valemail)<10:
    #        raise forms.ValidationError("Email should be more than or equal 10")
    
