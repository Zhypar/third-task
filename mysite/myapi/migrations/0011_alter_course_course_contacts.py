# Generated by Django 3.2.4 on 2021-06-18 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0010_rename_contacts_course_course_course_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_contacts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_contacts', to='myapi.contact'),
        ),
    ]
