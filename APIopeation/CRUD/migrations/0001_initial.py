# Generated by Django 4.1.1 on 2022-09-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIoperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.CharField(max_length=100)),
                ('update', models.CharField(max_length=100)),
                ('retrieve', models.CharField(max_length=100)),
                ('delete', models.CharField(max_length=100)),
            ],
        ),
    ]
