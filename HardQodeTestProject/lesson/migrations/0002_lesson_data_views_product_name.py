# Generated by Django 4.2.5 on 2023-09-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='data_views',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
