# Generated by Django 4.0.4 on 2022-11-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0002_alter_image_studios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to='studio_images/'),
        ),
    ]
