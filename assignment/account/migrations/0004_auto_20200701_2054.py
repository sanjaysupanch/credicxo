# Generated by Django 3.0.7 on 2020-07-01 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200701_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branches',
            old_name='bank_id',
            new_name='bank',
        ),
    ]
