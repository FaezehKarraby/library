# Generated by Django 3.2.8 on 2021-12-27 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_rename_date_of_birth_authormodel_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.authormodel'),
        ),
    ]
