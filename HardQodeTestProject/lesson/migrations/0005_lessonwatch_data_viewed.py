# Generated by Django 4.2.5 on 2023-09-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_alter_lessonwatch_watch_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonwatch',
            name='data_viewed',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
