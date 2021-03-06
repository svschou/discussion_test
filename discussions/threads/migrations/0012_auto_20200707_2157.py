# Generated by Django 3.0.6 on 2020-07-07 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('threads', '0011_auto_20200606_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewedDiscussionReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discussion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threads.DiscussionReply')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='discussionreply',
            name='viewed',
            field=models.ManyToManyField(related_name='thread_vieweddiscussionreplies', through='threads.ViewedDiscussionReply', to=settings.AUTH_USER_MODEL),
        ),
    ]
