# Generated by Django 3.1.4 on 2020-12-06 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0008_auto_20201205_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='removedpost',
            name='post_body',
            field=models.TextField(blank=True, default=''),
        ),
    ]
