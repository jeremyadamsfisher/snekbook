# Generated by Django 2.1.1 on 2019-03-07 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snekbook', '0006_auto_20190307_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snake',
            name='common_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='snake',
            name='fangs',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='snake',
            name='genus',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='snake',
            name='rating',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='snake',
            name='species',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='snake',
            name='toxicity',
            field=models.CharField(max_length=200),
        ),
    ]
