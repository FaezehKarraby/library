# Generated by Django 3.2.8 on 2021-12-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_bookmodel_production_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='publisher',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
