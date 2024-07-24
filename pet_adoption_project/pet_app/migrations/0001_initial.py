# Generated by Django 5.0.7 on 2024-07-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pet_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=100)),
                ('about_pet', models.TextField(max_length=200)),
                ('pet_type', models.CharField(max_length=100)),
                ('pet_age', models.IntegerField()),
                ('pet_breed', models.CharField(max_length=100)),
                ('pet_image', models.ImageField(blank=True, null=True, upload_to='pet_images/')),
            ],
        ),
    ]