# Generated by Django 2.1.1 on 2019-06-20 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("snekbook", "0010_snake_likers")]

    operations = [
        migrations.RemoveField(model_name="user", name="groups"),
        migrations.RemoveField(model_name="user", name="user_permissions"),
        migrations.DeleteModel(name="User"),
    ]
