# Generated by Django 2.1.1 on 2019-03-07 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("snekbook", "0004_auto_20190307_0559")]

    operations = [
        migrations.RemoveField(model_name="snake", name="recommended_snakes"),
        migrations.AddField(
            model_name="snake",
            name="recommended_snakes",
            field=models.ManyToManyField(
                related_name="_snake_recommended_snakes_+", to="snekbook.Snake"
            ),
        ),
        migrations.AddField(
            model_name="snake",
            name="img_norm",
            field=models.CharField(default="", max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="snake",
            name="img_thumb",
            field=models.CharField(default="", max_length=20),
            preserve_default=False,
        ),
    ]
