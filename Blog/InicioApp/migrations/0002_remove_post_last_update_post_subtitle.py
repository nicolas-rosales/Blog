# Generated by Django 4.0.3 on 2022-04-15 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InicioApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='last_update',
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
