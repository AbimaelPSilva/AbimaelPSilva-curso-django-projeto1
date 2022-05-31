from django.urls import path


from . import views # o ponto significa da pasta onde estoun para importar view

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
]
