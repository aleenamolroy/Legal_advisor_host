# Generated by Django 5.0.6 on 2024-07-09 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_advocate_login_userprofile_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Advocate',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
