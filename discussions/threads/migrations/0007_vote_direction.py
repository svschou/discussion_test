# Generated by Django 3.0.6 on 2020-06-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0006_auto_20200604_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='direction',
            field=models.CharField(choices=[('u', 'UP'), ('d', 'DOWN')], default='u', max_length=1),
        ),
    ]
