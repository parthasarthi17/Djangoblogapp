# Generated by Django 3.2.9 on 2021-11-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.TextField(default='namesssss', max_length=100),
        ),
    ]