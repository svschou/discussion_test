# Generated by Django 3.0.6 on 2020-06-04 20:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0007_vote_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brainstorm',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='brainstormcomment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='brainstormresponse',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='response',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]