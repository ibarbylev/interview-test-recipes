from django.urls import path

from recipe import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
]
