# Generated by Django 4.1.5 on 2023-02-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('vitality', models.IntegerField()),
                ('resilience', models.IntegerField()),
                ('pcn', models.IntegerField()),
                ('childnumber', models.IntegerField()),
                ('position', models.TextField(max_length=20)),
                ('balance', models.IntegerField()),
                ('alive', models.BooleanField(default=True)),
                ('fatherid', models.IntegerField()),
            ],
        ),
    ]
