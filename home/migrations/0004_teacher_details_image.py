# Generated by Django 4.1.5 on 2023-03-29 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_tid_teacher_details_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_details',
            name='image',
            field=models.ImageField(blank='False', upload_to='images'),
        ),
    ]