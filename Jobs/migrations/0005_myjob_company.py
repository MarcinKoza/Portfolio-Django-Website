# Generated by Django 4.1.3 on 2022-11-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0004_myjob_descripiton_myjob_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='myjob',
            name='company',
            field=models.CharField(default='NaN', max_length=64),
            preserve_default=False,
        ),
    ]
