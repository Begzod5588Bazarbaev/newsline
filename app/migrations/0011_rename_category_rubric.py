# Generated by Django 4.1.5 on 2023-02-02 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_post_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Rubric',
        ),
    ]