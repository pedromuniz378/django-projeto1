from django.urls import reverse, resolve

from recipes import views
from .test_recipe_base import TestRecipeBase, Recipe


class RecipeViewsTest(TestRecipeBase):
    def test_recipe_home_view_is_correct(self):
        view = resolve(reverse("recipes:home"))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertTemplateUsed(response, "recipes/pages/home.html")

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertIn(
            "<h1>No recipes found here!</h1>",
            response.content.decode("utf-8"),
        )

    def test_recipe_home_template_loads_recipes(self):
        # Need a recipe for this test
        self.make_recipe()

        response = self.client.get(reverse("recipes:home"))
        context_recipe = response.context["recipes"]
        content = response.content.decode("utf-8")

        self.assertEqual(len(context_recipe), 1)
        # Test default recipe name
        self.assertIn("Recipe Title", content)

    def test_recipe_home_template_dont_load_recipes(self):
        # Need a recipe for this test
        self.make_recipe(is_published=False)

        response = self.client.get(reverse("recipes:home"))
        self.assertIn(
            "<h1>No recipes found here!</h1>",
            response.content.decode("utf-8"),
        )

    def test_recipe_category_view_is_correct(self):
        view = resolve(reverse("recipes:category", kwargs={"category_id": 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = "This is a category test"
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(
            reverse(
                "recipes:category",
                kwargs={
                    "category_id": 1,
                },
            )
        )
        content = response.content.decode("utf-8")

        # Test default recipe name
        self.assertIn(needed_title, content)

    def test_recipe_category_template_dont_load_recipes(self):
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                "recipes:category",
                kwargs={
                    "category_id": recipe.id,
                },
            )
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_recipe_detail_view_is_correct(self):
        view = resolve(reverse("recipes:recipe", kwargs={"id": 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse("recipes:recipe", kwargs={"id": 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = "This is detail page - It load one recipe"
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(
            reverse(
                "recipes:recipe",
                kwargs={
                    "id": 1,
                },
            )
        )
        content = response.content.decode("utf-8")

        # Test default recipe name
        self.assertIn(needed_title, content)

    def test_recipe_detail_template_dont_load_recipes(self):
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                "recipes:recipe",
                kwargs={
                    "id": recipe.id,
                },
            )
        )
        self.assertEqual(response.status_code, 404)
