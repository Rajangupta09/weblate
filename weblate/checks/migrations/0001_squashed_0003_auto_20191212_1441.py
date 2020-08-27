# Generated by Django 3.0.6 on 2020-05-27 11:24

import django.db.models.deletion
from django.db import migrations, models

from weblate.checks.models import CHECKS


class Migration(migrations.Migration):

    replaces = [
        ("checks", "0001_squashed_0002_auto_20180416_1509"),
        ("checks", "0002_check_unit"),
        ("checks", "0003_auto_20191212_1441"),
    ]

    initial = True

    dependencies = [
        ("trans", "0001_squashed_0143_auto_20180609_1655"),
        ("lang", "0001_squashed_0011_auto_20180215_1158"),
        ("trans", "0052_auto_20191212_1403"),
        ("trans", "0054_auto_20191212_1441"),
    ]

    operations = [
        migrations.CreateModel(
            name="Check",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "check",
                    models.CharField(
                        choices=CHECKS.get_choices(),
                        max_length=50,
                    ),
                ),
                ("ignore", models.BooleanField(db_index=True, default=False)),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="trans.Unit"
                    ),
                ),
            ],
            options={"unique_together": {("unit", "check")}},
        ),
    ]
