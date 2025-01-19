from django import forms
from .models import UploadedFile
import os

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            ext = os.path.splitext(file.name)[1].lower()
            if ext not in ['.csv', '.xls', '.xlsx']:
                raise forms.ValidationError(
                    'Apenas arquivos CSV, XLS e XLSX são permitidos.'
                )
        return file
