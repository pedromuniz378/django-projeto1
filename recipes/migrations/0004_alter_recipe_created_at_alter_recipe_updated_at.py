# Generated by Django 4.1.7 on 2023-03-14 18:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0003_recipe_updated_at_alter_recipe_is_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
