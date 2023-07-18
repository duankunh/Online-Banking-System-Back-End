from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from banks.models import Bank, Branch


class AddBankForm(forms.ModelForm):
    name = forms.CharField(required=False)
    description = forms.CharField(required=False)
    inst_num = forms.CharField(required=False)
    swift_code = forms.CharField(required=False)

    class Meta:
        model = Bank
        exclude = ['owner', 'branches']

    def clean(self):
        data = super().clean()
        if data.get('name') == "" or data.get('name') is None:
            self.add_error('name', 'This field is required')
        if data.get('description') == "" or data.get('description') is None:
            self.add_error('description', 'This field is required')
        if data.get('inst_num') == "" or data.get('inst_num') is None:
            self.add_error('inst_num', 'This field is required')
        if data.get('swift_code') == "" or data.get('swift_code') is None:
            self.add_error('swift_code', 'This field is required')
        return data


class AddBranchForm(forms.ModelForm):
    name = forms.CharField(required=False)
    transit_num = forms.CharField(required=False)
    address = forms.CharField(required=False)

    class Meta:
        model = Branch
        exclude = ['bank']

    def clean(self):
        data = super().clean()
        if data.get('name') == "" or data.get('name') is None:
            self.add_error('name', 'This field is required')
        if data.get('transit_num') == "" or data.get('transit_num') is None:
            self.add_error('transit_num', 'This field is required')
        if data.get('address') == "" or data.get('address') is None:
            self.add_error('address', 'This field is required')
        try:
            validate_email(data.get('email'))
        except ValidationError:
            self.add_error('email', 'Enter a valid email address')
        return data
