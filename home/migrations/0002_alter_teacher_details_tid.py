# Generated by Django 4.1.5 on 2023-03-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_details',
            name='tid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
