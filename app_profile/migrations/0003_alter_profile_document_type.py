# Generated by Django 4.2.16 on 2024-12-08 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0002_alter_profile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='document_type',
            field=models.CharField(choices=[('PASSPORT', 'Passport'), ('NID', 'NID'), ('DRIVING_LICENSE', 'Driver License')], max_length=20, verbose_name='Document Type'),
        ),
    ]
