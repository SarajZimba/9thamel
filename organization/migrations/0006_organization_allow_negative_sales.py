# Generated by Django 4.0.6 on 2024-06-25 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_organization_loyalty_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='allow_negative_sales',
            field=models.BooleanField(default=False),
        ),
    ]
