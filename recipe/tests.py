from django.test import TestCase

from .models import Ingredient, Recipe, RecipeComposition


class TestDataBase(TestCase):
    fixtures = []

    def setUp(self):
        self.ingredient = Ingredient.objects.create(
            name='Potato',
        )
        self.recipe = Recipe.objects.create(
            name="French Fries",
        )

    def test_add_ingredient_to_RecipeComposition(self):
        """Testing the increase/decrease of time_used value when
        adding and removing an ingredient in the RecipeComposition model.
        """
        # add ingredient
        self.recipe_comp = RecipeComposition.objects.create(
            recipe=self.recipe,
            ingredient=self.ingredient,
        )
        self.assertEqual(self.ingredient.times_used, 1)
        self.assertEqual(self.recipe_comp.get_recipe_ingredients()[0], 'Potato')

        # delete ingredient
        self.recipe_comp.delete()
        self.assertEqual(self.ingredient.times_used, 0)


