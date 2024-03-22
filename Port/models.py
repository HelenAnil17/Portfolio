from django.db import models

class contact(models.Model):
    name=models.CharField(max_length=20)
    mail=models.EmailField()
    message=models.TextField(max_length=1000,default="NULL")

