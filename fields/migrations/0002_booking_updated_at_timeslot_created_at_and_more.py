# Generated by Django 5.2 on 2025-04-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timeslot',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
