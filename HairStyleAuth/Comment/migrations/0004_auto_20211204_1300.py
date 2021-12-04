# Generated by Django 3.2.8 on 2021-12-04 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0010_auto_20211115_2326'),
        ('Order', '0006_alter_order_comment_id'),
        ('Comment', '0003_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='profile_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Profile.profile'),
        ),
    ]
