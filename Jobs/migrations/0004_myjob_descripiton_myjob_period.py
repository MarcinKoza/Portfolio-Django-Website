# Generated by Django 4.1.3 on 2022-11-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0003_rename_myjobs_myjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='myjob',
            name='descripiton',
            field=models.CharField(default='NaN', max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myjob',
            name='period',
            field=models.CharField(default='NaN', max_length=64),
            preserve_default=False,
        ),
    ]
