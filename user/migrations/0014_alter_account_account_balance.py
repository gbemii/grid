# Generated by Django 3.2a1 on 2022-03-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_transactions_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_balance',
            field=models.IntegerField(),
        ),
    ]
