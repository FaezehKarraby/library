# Generated by Django 3.2.8 on 2021-12-16 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_bookmodel_translator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genremodel',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='genremodel',
            old_name='title',
            new_name='name',
        ),
    ]
