# Generated by Django 3.2.8 on 2021-12-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_bookmodel_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='translator',
            field=models.CharField(default='None', max_length=255),
        ),
    ]
