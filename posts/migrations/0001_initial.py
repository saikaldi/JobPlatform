# Generated by Django 5.1.4 on 2025-01-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JobPosting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("company", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("full_time", "Full-time"),
                            ("part_time", "Part-time"),
                            ("contract", "Contract"),
                            ("freelance", "Freelance"),
                            ("internship", "Internship"),
                        ],
                        max_length=50,
                    ),
                ),
                ("salary", models.CharField(blank=True, max_length=100, null=True)),
                ("description", models.TextField()),
                ("contact_email", models.EmailField(max_length=254)),
                ("posted_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
