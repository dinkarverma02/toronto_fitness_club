# Generated by Django 4.1.3 on 2022-11-16 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('coach', models.CharField(max_length=200)),
                ('capacity', models.IntegerField()),
                ('day', models.CharField(max_length=50)),
                ('start_time', models.TimeField(default='')),
                ('end_time', models.TimeField(default='')),
                ('keywords', models.ManyToManyField(to='classes.keyword')),
            ],
        ),
    ]
