# Generated by Django 4.2.5 on 2023-09-26 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_lesson_data_views_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='data_views',
            new_name='data_viewed',
        ),
    ]