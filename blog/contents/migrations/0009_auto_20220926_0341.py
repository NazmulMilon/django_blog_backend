# Generated by Django 3.0 on 2022-09-26 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contents', '0008_auto_20220923_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_detail',
            field=models.CharField(help_text='comment body', max_length=500),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_detail', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True, help_text='reply written time')),
                ('updated_at', models.DateTimeField(auto_now_add=True, help_text='last updated time ')),
                ('comment', models.ForeignKey(help_text='write reply for comment', on_delete=django.db.models.deletion.CASCADE, to='contents.Comment')),
                ('replier', models.ForeignKey(help_text='person who reply the commenter', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
