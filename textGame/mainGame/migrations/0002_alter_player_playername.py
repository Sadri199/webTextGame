# Generated by Django 5.1.3 on 2024-11-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainGame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='playerName',
            field=models.CharField(max_length=50),
        ),
    ]
