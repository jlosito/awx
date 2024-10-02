# Generated by Django 4.2.10 on 2024-10-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sso', '0003_convert_saml_string_to_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userenterpriseauth',
            name='provider',
            field=models.CharField(choices=[('radius', 'RADIUS'), ('tacacs+', 'TACACS+')], max_length=32),
        ),
    ]
