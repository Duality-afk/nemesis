# Generated by Django 3.2.4 on 2021-11-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_account_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
