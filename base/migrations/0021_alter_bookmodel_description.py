# Generated by Django 3.2.8 on 2022-01-06 09:42

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_auto_20220104_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
