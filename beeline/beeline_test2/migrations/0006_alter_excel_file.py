# Generated by Django 4.0.5 on 2022-06-26 19:34

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beeline_test2', '0005_alter_excel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excel',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media'), upload_to=''),
        ),
    ]
