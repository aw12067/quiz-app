# Generated by Django 3.2.3 on 2021-07-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20210706_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='points',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]
