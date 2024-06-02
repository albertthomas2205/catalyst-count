from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a CSV file')

from django import forms

class CompanyFilterForm(forms.Form):
    industry = forms.CharField(required=False, label='Industry')
    size_range = forms.CharField(required=False, label='Size Range')
    locality = forms.CharField(required=False, label='Locality')
    country = forms.CharField(required=False, label='Country')