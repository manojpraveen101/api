# Generated by Django 3.1.7 on 2021-03-08 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapi', '0002_auto_20210308_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='companyId',
            new_name='company',
        ),
    ]
