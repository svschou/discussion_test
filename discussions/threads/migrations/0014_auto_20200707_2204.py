# Generated by Django 3.0.6 on 2020-07-07 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('threads', '0013_vieweddiscussionreply_last_seen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ViewedDiscussionReply',
            new_name='ViewedDiscussion',
        ),
        migrations.RemoveField(
            model_name='discussionreply',
            name='viewed',
        ),
        migrations.AddField(
            model_name='discussion',
            name='viewed',
            field=models.ManyToManyField(related_name='thread_vieweddiscussions', through='threads.ViewedDiscussion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vieweddiscussion',
            name='discussion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threads.Discussion'),
        ),
    ]