# from tkinter import Image
from operator import mod
# from turtle import update
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Images(models.Model):
    tit = models.TextField(null=True)
    img = models.ImageField(upload_to="images", null=True)
    upd_str = models.TextField(null=True)

class Usr(models.Model):
    ref = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mk = models.TextField(null=True)
    avt = models.ForeignKey(Images, on_delete=models.CASCADE, null=True)
    ip = models.CharField(max_length=60, null=True)
    mes = models.TextField(null=True)
    data = models.TextField(null=True)
    upd_str = models.TextField(null=True)

class Label(models.Model):
    nm = models.TimeField(null=True)
    value = models.IntegerField(null=True)
    res = models.TextField(null=True)
    upd_str = models.TextField(null=True)

class Cau(models.Model):
    lb = models.ForeignKey(Label, null=True, on_delete=models.CASCADE)
    data = models.TextField(null=True)
    upd_str = models.TextField(null=True)
