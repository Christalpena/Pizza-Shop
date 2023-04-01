from django import forms

class Information(forms.Form):
    Name = forms.CharField(max_length=30,label='Name',required=True,widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    Last_Name = forms.CharField(max_length=30,label='Last Name',required=True,widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    Gmail= forms.EmailField(label='Gmail',required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
