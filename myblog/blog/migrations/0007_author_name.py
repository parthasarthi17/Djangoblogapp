# Generated by Django 3.2.9 on 2021-11-11 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
