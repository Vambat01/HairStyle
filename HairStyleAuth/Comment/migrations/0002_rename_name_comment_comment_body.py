# Generated by Django 3.2.8 on 2021-12-04 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='comment_body',
        ),
    ]