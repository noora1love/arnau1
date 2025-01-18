from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category, Tablecloth
from django.views.generic import DetailView


def index(request):
    categoryes = Category.objects.all()
    categories = Category.objects.all()

    return render(request, 'main/index.html', { 'categoryes' :categoryes, 'categories': categories,} )




def shop_detail(request, category_id, tablecloth_id):
    category = get_object_or_404(Category, id=category_id)
    tablecloth = get_object_or_404(Tablecloth, id=tablecloth_id, category=category)
    categories = Category.objects.all()

    # Получаем товары той же категории, но исключаем текущий товар
    related_tablecloths = Tablecloth.objects.filter(category=category).exclude(id=tablecloth.id)

    # Если товаров в категории мало, можно добавить другие товары (например, случайные)
    if related_tablecloths.count() < 4:
        related_tablecloths = Tablecloth.objects.all()[:4]  # Возвращаем любые 4 товара

    return render(request, 'main/detail.html', {
        'category': category,
        'tablecloth': tablecloth,
        'related_tablecloths': related_tablecloths,
        'categories': categories,  # передаем связанные товары

    })


def shop(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    categories = Category.objects.all()
    tablecloths = Tablecloth.objects.filter(category=category)

    return render(request, 'main/shop.html', {'category': category, 'tablecloths': tablecloths,  'categories': categories, })
