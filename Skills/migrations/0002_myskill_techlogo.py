# Generated by Django 4.1.3 on 2022-11-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myskill',
            name='techlogo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
