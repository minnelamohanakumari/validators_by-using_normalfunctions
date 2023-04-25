from django import forms
def check_for_a(x):
    if x[0].lower()=='a':
        raise forms.ValidationError('should not start with digit')


def check_for_len(y):
    if len(y)<5:
        raise forms.ValidationError('len is 5 characters only')


class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    age=forms.IntegerField()
    email=forms.EmailField()