# Generated by Django 3.2.7 on 2021-11-15 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0009_alter_profile_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='address')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RelatedOrder', to='Profile.profile', verbose_name='user')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_orders',
            field=models.ManyToManyField(related_name='RelatedProfile', to='Profile.ProfileOrder', verbose_name='ProfileOrder'),
        ),
    ]