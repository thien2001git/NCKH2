# Generated by Django 4.0.3 on 2022-04-12 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinh', '0007_cau_upd_str_images_upd_str_label_upd_str_usr_upd_str'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='value',
            field=models.IntegerField(null=True),
        ),
    ]
