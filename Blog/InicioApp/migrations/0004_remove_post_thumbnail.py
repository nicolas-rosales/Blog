# Generated by Django 4.0.3 on 2022-04-20 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InicioApp', '0003_alter_post_publish_date_alter_post_subtitle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumbnail',
        ),
    ]
