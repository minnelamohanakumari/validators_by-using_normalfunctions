from django import forms
from django.core import validators
def check_for_a(x):
    if x[0].lower()=='a':
        raise forms.ValidationError('should not start with digit')


def check_for_len(y):
    if len(y)<5:
        raise forms.ValidationError('len is 5 characters only')


class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,validators.MaxLengthValidator(5)])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        if e!=r:
            raise forms.ValidationError('not matched')


    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('not correct')

