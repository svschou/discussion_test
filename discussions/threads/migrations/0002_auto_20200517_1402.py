# Generated by Django 3.0.6 on 2020-05-17 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('threads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threads.Reaction')),
            ],
        ),
        migrations.DeleteModel(
            name='React',
        ),
        migrations.AddField(
            model_name='reaction',
            name='responses',
            field=models.ManyToManyField(related_name='thread_responses', through='threads.Response', to=settings.AUTH_USER_MODEL),
        ),
    ]