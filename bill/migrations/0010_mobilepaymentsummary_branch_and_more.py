# Generated by Django 4.0.6 on 2024-06-19 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_terminal_printersetting'),
        ('bill', '0009_mobilepaymentsummary'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilepaymentsummary',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.branch'),
        ),
        migrations.AddField(
            model_name='mobilepaymentsummary',
            name='sent_in_mail',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mobilepaymentsummary',
            name='terminal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
