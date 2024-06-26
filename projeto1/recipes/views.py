from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', status=201, context={
        'recipes': recipes, 
    })

def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(category__id = category_id, is_published=True).order_by('-id'))

    return render(request, 'recipes/pages/category.html', status=201, context={
        'recipes': recipes, 
        'title': f'{recipes[0].category.name} - Category |'
    })

def recipe(request, id):
    # recipe = Recipe.objects.filter(pk = id, is_published=True).first()

    recipe = get_object_or_404(Recipe, pk = id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', status=201, context={
        'recipe': recipe, 
        'is_detail_page': True,
    })
