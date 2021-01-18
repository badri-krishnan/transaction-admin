# Generated by Django 3.1.5 on 2021-01-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_approval', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='authorized_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='flag_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='reject_count',
            field=models.BigIntegerField(default=0),
        ),
    ]
