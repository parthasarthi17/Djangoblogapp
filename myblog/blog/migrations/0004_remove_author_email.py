# Generated by Django 3.2.9 on 2021-11-11 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211111_0429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
    ]
