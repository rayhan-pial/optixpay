# Generated by Django 4.2.16 on 2024-12-13 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0001_initial'),
        ('app_deposit', '0002_currency_remove_deposit_received_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='agent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='agent_deposits', to='app_profile.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deposit',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='currency_deposits', to='app_deposit.currency'),
            preserve_default=False,
        ),
    ]
