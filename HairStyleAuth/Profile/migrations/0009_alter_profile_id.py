# Generated by Django 3.2.7 on 2021-10-25 21:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0008_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
