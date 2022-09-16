# Generated by Django 3.0 on 2022-09-16 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_auto_20220914_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(help_text='body of a single blog post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='last update time'),
        ),
    ]