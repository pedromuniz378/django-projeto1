from .test_recipe_base import TestRecipeBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized


class CategoryModelTest(TestRecipeBase):
    def setUp(self) -> None:
        self.category = self.make_category()
        return super().setUp()

    def test_recipe_category_name_max_length_is_65_chars(self):
        self.category.name = "A" * 70

        with self.assertRaises(ValidationError):
            self.category.full_clean()

    def test_recipe_category_string_representation_is_name_field(self):
        needed = "Testing Representation"

        self.category.name = needed
        self.category.full_clean()
        self.category.save()

        self.assertEqual(
            str(self.category),
            self.category.name,
        )
