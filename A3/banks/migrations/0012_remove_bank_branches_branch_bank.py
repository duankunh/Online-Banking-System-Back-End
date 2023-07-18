# Generated by Django 4.1.2 on 2022-11-01 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0011_remove_bank_branches_bank_branches'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='branches',
        ),
        migrations.AddField(
            model_name='branch',
            name='bank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='banks.bank'),
        ),
    ]
