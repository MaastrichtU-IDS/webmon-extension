# Generated by Django 2.2 on 2021-07-14 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_contract_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cause',
            name='creator',
        ),
    ]
