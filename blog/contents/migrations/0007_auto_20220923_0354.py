# Generated by Django 3.0 on 2022-09-23 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contents', '0006_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_detail', models.CharField(help_text='comment body', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='comment written time')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='comment updated time')),
                ('posts', models.ForeignKey(help_text='post details', on_delete=django.db.models.deletion.CASCADE, to='contents.Post')),
                ('user', models.ForeignKey(help_text='person who comment', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
