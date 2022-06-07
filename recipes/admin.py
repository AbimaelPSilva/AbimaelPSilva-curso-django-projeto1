from django.contrib import admin

from .models import Category, Recipe


# Existem duas formas de registrar
# 1ª Forma
class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)

# 2ª Forma


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
