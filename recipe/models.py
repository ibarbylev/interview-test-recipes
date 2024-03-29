from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    times_used = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}: {self.times_used}"


class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.name}"


class RecipeComposition(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    weight_in_grams = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('recipe', 'ingredient')
        ordering = ['recipe__name']

    def get_recipe_ingredients(self):
        # Get all ingredients for current recipe
        return self.recipe.recipecomposition_set.values_list('ingredient__name', flat=True)

    def __str__(self):
        return f"Recipe: {self.recipe.name}| ingredient: {self.ingredient}"


@receiver(post_save, sender=RecipeComposition)
def increase_howmany_used(sender, instance, **kwargs):
    # When saving a new entry in RecipeComposition, increase howmany_used by 1
    instance.ingredient.times_used += 1
    instance.ingredient.save()


@receiver(post_delete, sender=RecipeComposition)
def decrease_howmany_used(sender, instance, **kwargs):
    # When deleting a new entry in RecipeComposition, decrease howmany_used by 1
    instance.ingredient.times_used -= 1
    instance.ingredient.save()
