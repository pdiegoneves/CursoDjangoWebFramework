from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.all().order_by('-id')


    return render(request, 'recipes/pages/home.html', status=201, context={
        'recipes': recipes, 
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', status=201, context={
        'recipe': make_recipe(), 
        'is_detail_page': True,
    })
