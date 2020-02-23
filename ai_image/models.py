from django.db import models

class Document(models.Model):
    description=models.CharField(max_length=255,blank=True)
    photo=models.ImageField(uplord_to="documents/",default="defo")
    uploaded_at=models.DateTimeField(auto_now_add=True)
