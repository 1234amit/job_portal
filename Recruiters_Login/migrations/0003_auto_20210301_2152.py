# Generated by Django 3.0.8 on 2021-03-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruiters_Login', '0002_auto_20210301_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiters',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]