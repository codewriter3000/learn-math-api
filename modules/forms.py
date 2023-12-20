from django import forms


class TermForm(forms.Form):
    name = forms.CharField(label='Term name', max_length=100)
    definition = forms.CharField(label='Term definition', widget=forms.Textarea)

class ModuleForm(forms.Form):
    name = forms.CharField(label='Module name', max_length=100)
