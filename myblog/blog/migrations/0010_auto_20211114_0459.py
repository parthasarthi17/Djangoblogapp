# Generated by Django 3.2.9 on 2021-11-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='date_added',
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='writer',
            field=models.CharField(default='anonymous', max_length=50),
        ),
    ]
