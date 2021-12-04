# Generated by Django 3.2.8 on 2021-12-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0002_rename_name_comment_comment_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.CharField(max_length=350, null=True)),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('grade', models.IntegerField(choices=[(0, 'Low'), (1, 'Normal'), (2, 'High')], default=1)),
            ],
        ),
    ]
