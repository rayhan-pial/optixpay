# Generated by Django 4.2.16 on 2024-12-08 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(choices=[('BD', 'Bangladesh'), ('US', 'United States'), ('IN', 'India'), ('UK', 'United Kingdom'), ('CA', 'Canada')], max_length=3, verbose_name='Country'),
        ),
    ]
