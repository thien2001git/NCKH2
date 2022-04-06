from django.contrib import admin

from chinh.models import Cau, Images, Label, Usr

# Register your models here.
admin.site.register(Images)
admin.site.register(Usr)
admin.site.register(Label)
admin.site.register(Cau)
