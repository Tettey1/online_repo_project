# Generated by Django 4.0.3 on 2022-04-24 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_studentprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
