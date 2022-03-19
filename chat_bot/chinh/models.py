# from tkinter import Image
from django.db import models

# Create your models here.
class Images(models.Model):
    tit = models.TextField(null=True)
    img = models.ImageField(upload_to="images", null=True)