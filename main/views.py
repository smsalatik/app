from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели - HOME',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Классный сайт с мебелю туда сюда',
    }

    return render(request, 'main/about.html', context)