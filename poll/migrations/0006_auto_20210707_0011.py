# Generated by Django 3.2.3 on 2021-07-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_auto_20210706_2351'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.AddField(
            model_name='poll',
            name='answer',
            field=models.CharField(default='none', max_length=30),
        ),
    ]
