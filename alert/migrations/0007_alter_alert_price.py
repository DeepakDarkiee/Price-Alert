# Generated by Django 4.0.6 on 2022-07-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0006_alter_alert_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]
