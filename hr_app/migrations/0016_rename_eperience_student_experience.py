# Generated by Django 5.0.1 on 2024-02-15 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0015_student_remove_review_user_name_delete_registration_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='eperience',
            new_name='experience',
        ),
    ]
