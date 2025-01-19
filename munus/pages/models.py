from django.db import models
import os

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def process_file(self):
        # Implementar lógica de processamento do arquivo aqui
        return f"Pré-visualização do arquivo {os.path.basename(self.file.name)}"
