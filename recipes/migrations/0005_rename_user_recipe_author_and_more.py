# Generated by Django 4.1.7 on 2023-03-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0004_alter_recipe_created_at_alter_recipe_updated_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe",
            old_name="user",
            new_name="author",
        ),
        migrations.RenameField(
            model_name="recipe",
            old_name="preparation_step",
            new_name="preparation_steps",
        ),
        migrations.RemoveField(
            model_name="recipe",
            name="preparation_step_is_html",
        ),
        migrations.AddField(
            model_name="recipe",
            name="preparation_steps_is_html",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="cover",
            field=models.ImageField(
                blank=True, default="", upload_to="recipes/covers/%Y/%m/%d/"
            ),
        ),
    ]
