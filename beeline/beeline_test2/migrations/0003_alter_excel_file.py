# Generated by Django 4.0.5 on 2022-06-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beeline_test2', '0002_alter_excel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excel',
            name='file',
            field=models.FileField(upload_to='beeline/media'),
        ),
    ]
