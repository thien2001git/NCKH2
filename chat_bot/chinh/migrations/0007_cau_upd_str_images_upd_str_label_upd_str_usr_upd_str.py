# Generated by Django 4.0.3 on 2022-04-12 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinh', '0006_label_res'),
    ]

    operations = [
        migrations.AddField(
            model_name='cau',
            name='upd_str',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='images',
            name='upd_str',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='label',
            name='upd_str',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='usr',
            name='upd_str',
            field=models.TextField(null=True),
        ),
    ]
