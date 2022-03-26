# from tkinter import Image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Images(models.Model):
    tit = models.TextField(null=True)
    img = models.ImageField(upload_to="images", null=True)

class Usr(models.Model):
    ref = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mk = models.TextField(null=True)
    avt = models.ForeignKey(Images, on_delete=models.CASCADE, null=True)
    ip = models.CharField(max_length=60, null=True)
    mes = models.TextField(null=True)
    data = models.TextField(null=True)
