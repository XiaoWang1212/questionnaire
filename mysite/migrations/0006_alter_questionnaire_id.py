# Generated by Django 5.0.7 on 2024-07-24 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mysite", "0005_auto_20240724_0157"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionnaire",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
