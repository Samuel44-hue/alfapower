# Generated by Django 5.1.2 on 2024-10-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Image', models.ImageField(null=True, upload_to='')),
                ('Project_Name', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
