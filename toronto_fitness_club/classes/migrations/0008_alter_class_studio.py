# Generated by Django 4.1.3 on 2022-11-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_class_studio_classes_class_instances'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='studio',
            field=models.CharField(max_length=150),
        ),
    ]
