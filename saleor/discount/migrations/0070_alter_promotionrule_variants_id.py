# Generated by Django 3.2.24 on 2024-03-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discount", "0069_promotionrule_variants"),
    ]

    operations = [
        migrations.AlterField(
            model_name="promotionrule_variants",
            name="id",
            field=models.BigAutoField(
                editable=False, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]