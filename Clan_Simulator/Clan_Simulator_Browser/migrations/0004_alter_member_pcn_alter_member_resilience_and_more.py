# Generated by Django 4.2.2 on 2023-07-01 13:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clan_Simulator_Browser', '0003_member_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='pcn',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='member',
            name='resilience',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='member',
            name='vitality',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
