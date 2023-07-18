# Generated by Django 4.1.2 on 2022-11-01 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0013_alter_bank_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bank',
            name='inst_num',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bank',
            name='swift_code',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='branch',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='branch',
            name='transit_num',
            field=models.CharField(max_length=200),
        ),
    ]
