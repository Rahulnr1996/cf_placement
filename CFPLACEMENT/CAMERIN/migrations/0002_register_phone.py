# Generated by Django 4.1 on 2022-09-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAMERIN', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
