# Generated by Django 4.2.16 on 2024-10-21 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "recommendations",
            "0002_rename_artist_name_recommendation_referenceartist_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="recommendation",
            name="badges",
            field=models.JSONField(blank=True, default=list),
        ),
    ]