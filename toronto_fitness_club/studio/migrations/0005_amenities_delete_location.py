# Generated by Django 4.1.3 on 2022-11-13 02:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0004_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('studios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='studio.studio')),
            ],
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
