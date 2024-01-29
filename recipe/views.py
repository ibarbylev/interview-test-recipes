from django.shortcuts import render
from django.views import generic

from .models import RecipeComposition, Recipe, Ingredient


class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.all()
        context['ingredients'] = Ingredient.objects.all()
        return context


class AddIngredientToRecipeView(generic.FormView):
    template_name = 'recipe/change-recipe.html'

    def get(self, recipe_pk, **kwargs):
        return render(self.request, self.template_name)

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs['recipe_id']
        form.instance.product_id = self.kwargs['product_id']
        form.instance.weight = self.kwargs['weight']
        return super().form_valid(form)
