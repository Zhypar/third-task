# Generated by Django 3.2.4 on 2021-06-18 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_delete_hero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_course',
        ),
        migrations.RemoveField(
            model_name='course',
            name='branches',
        ),
        migrations.RemoveField(
            model_name='course',
            name='contacts',
        ),
        migrations.AddField(
            model_name='contact',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='myapi.course'),
        ),
    ]