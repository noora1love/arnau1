from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category, Tablecloth
from django.views.generic import DetailView


def index(request):
    categoryes = Category.objects.all()
    return render(request, 'main/index.html', { 'categoryes' :categoryes } )

def shop(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    tablecloths = Tablecloth.objects.filter(category=category)

    return render(request, 'main/shop.html', {'category': category, 'tablecloths': tablecloths})