# Generated by Django 2.2.9 on 2020-02-03 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoafisica',
            name='teste',
        ),
    ]
