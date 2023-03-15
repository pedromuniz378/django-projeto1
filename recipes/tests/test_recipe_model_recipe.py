from .test_recipe_base import TestRecipeBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelTest(TestRecipeBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name="Test default Category"),
            author=self.make_author(username="newuser"),
            title="Recipe Title",
            description="Recipe Description",
            slug="recipe-slug",
            preparation_time=10,
            preparation_time_unit="Minutos",
            servings=5,
            servings_unit="Porções",
            preparation_steps="Recipe Preparation Steps",
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = "A" * 70

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    @parameterized.expand(
        [
            ("title", 65),
            ("description", 165),
            ("preparation_time_unit", 65),
            ("servings_unit", 65),
        ]
    )
    def test_recipe_title_max_length(self, field, max_len):
        setattr(self.recipe, field, "A" * (max_len + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()

        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg="preparation_steps_is_html is not False",
        )

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()

        self.assertFalse(
            recipe.is_published,
            msg="is_published is not False",
        )

    def test_recipe_string_representation(self):
        needed = "Testing Representation"

        self.recipe.title = needed
        self.recipe.full_clean()
        self.recipe.save()

        self.assertEqual(
            str(self.recipe),
            needed,
            msg="Recipe string representation must be "
            f"{needed} but {str(self.recipe)} was recieved",
        )
