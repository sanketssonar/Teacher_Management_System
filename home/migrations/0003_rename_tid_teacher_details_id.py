# Generated by Django 4.1.5 on 2023-03-29 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_teacher_details_tid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher_details',
            old_name='tid',
            new_name='id',
        ),
    ]
