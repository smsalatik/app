from django.shortcuts import render

from products.models import Categories

def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'DAGMeet - Главная',
        'content': 'Халяльная продукция с Дагестана DAGMeet',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'DAGMeet - О нас',
        'content': 'О нас',
        'text_on_page': 'Производим настоящюю продукцию в горах Дагестана.',
    }

    return render(request, 'main/about.html', context)