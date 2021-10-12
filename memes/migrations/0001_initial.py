# Generated by Django 3.2.6 on 2021-10-12 13:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=16)),
                ('image', models.ImageField(upload_to='image/')),
                ('upload_date', models.DateField(default=django.utils.timezone.now)),
                ('image_description', models.TextField(blank=True, max_length=256)),
            ],
        ),
    ]
