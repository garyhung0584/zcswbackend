# Generated by Django 3.2.8 on 2022-04-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_member_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='member/'),
        ),
    ]
