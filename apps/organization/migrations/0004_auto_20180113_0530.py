# Generated by Django 2.0.1 on 2018-01-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='has_auth',
            field=models.BooleanField(default=False, verbose_name='是否认证'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='index',
            field=models.IntegerField(default=999, verbose_name='排序'),
        ),
    ]
