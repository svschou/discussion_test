# Generated by Django 3.0.6 on 2020-06-06 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0010_discussion_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='brainstorm',
            name='topic',
            field=models.TextField(default='General'),
        ),
        migrations.AddField(
            model_name='reaction',
            name='topic',
            field=models.TextField(default='General'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='topic',
            field=models.TextField(default='General'),
        ),
    ]
