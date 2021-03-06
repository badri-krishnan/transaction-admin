# Generated by Django 3.1.5 on 2021-01-17 17:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.UUIDField(default=uuid.uuid4, help_text='Unique TransactionId for this transaction', primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('merchant_name', models.CharField(max_length=200)),
                ('issuing_bank', models.CharField(max_length=200)),
                ('merchant_bank', models.CharField(max_length=200)),
                ('status', models.CharField(blank=True, choices=[('A', 'Authorized'), ('R', 'Reject'), ('F', 'Flag')], default='m', help_text='Status of Transaction', max_length=1)),
            ],
        ),
    ]
