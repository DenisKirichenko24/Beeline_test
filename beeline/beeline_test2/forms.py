from django.forms import ModelForm

from .models import ExcelModel


class ExcelForm(ModelForm):
    class Meta:
        model = ExcelModel
        fields = ['file']
        labels = {'doc': ('Document')}
        help_texts = {'doc': ('Please upload the document')}