# Generated by Django 4.2.10 on 2024-09-16 15:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0196_delete_profile'),
    ]

    operations = [
        # delete all sso application migrations
        migrations.RunSQL("DELETE FROM django_migrations WHERE app = 'sso';"),
        # delete all sso application content group permissions
        migrations.RunSQL(
            "DELETE FROM auth_group_permissions "
            "WHERE permission_id IN "
            "(SELECT id FROM auth_permission WHERE content_type_id in (SELECT id FROM django_content_type WHERE app_label = 'sso'));"
        ),
        # delete all sso application content permissions
        migrations.RunSQL("DELETE FROM auth_permission " "WHERE content_type_id IN (SELECT id FROM django_content_type WHERE app_label = 'sso');"),
        # delete sso application content type
        migrations.RunSQL("DELETE FROM django_content_type WHERE app_label = 'sso';"),
        # drop sso application created table
        migrations.RunSQL("DROP TABLE IF EXISTS sso_userenterpriseauth;"),
    ]
