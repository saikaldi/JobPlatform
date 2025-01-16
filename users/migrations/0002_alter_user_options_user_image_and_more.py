# Generated by Django 5.1.4 on 2025-01-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "User", "verbose_name_plural": "Users"},
        ),
        migrations.AddField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="users_images", verbose_name="Avatar"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterModelTable(
            name="user",
            table="user",
        ),
    ]
