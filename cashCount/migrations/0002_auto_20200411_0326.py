# Generated by Django 3.0.5 on 2020-04-10 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashCount', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashmemo',
            name='datecompleted',
        ),
        migrations.AlterField(
            model_name='cashmemo',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
