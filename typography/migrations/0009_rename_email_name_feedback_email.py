# Generated by Django 5.0.7 on 2024-08-12 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('typography', '0008_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='email_name',
            new_name='email',
        ),
    ]
