# Generated by Django 3.2.4 on 2021-06-18 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0009_course_contacts_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='contacts_course',
            new_name='course_contacts',
        ),
    ]
