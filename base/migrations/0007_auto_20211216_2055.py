# Generated by Django 3.2.8 on 2021-12-16 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_authormodel_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='production_year',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='translator',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
