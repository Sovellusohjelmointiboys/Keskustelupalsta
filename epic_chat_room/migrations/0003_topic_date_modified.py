# Generated by Django 4.1.3 on 2022-11-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epic_chat_room', '0002_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
