from django.urls import path

from recipe import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('add_product_to_recipe/<int:pk>/', views.AddIngredientToRecipeView.as_view(),
         name='add_product_to_recipe'),
]
