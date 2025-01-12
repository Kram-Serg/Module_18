

# Create your views here.
from django.shortcuts import render


# Create your views here.
def menu_index(request):
    title = 'мой сайт'
    back = 'Вернуться на главную страницу'
    cart = 'Корзина'

    context = {'title': title, 'back': back, 'cart': cart}
    return render(request, 'menu.html', context)


def start_index(request):
    title = 'мой сайт'
    back = 'Вернуться на главную страницу'
    cart = 'Корзина'
    context = {'title': title, 'back': back, 'cart': cart}
    return render(request, 'start.html', context)


def buy_index(request):
    title = 'мой сайт'
    back = 'Вернуться на главную страницу'
    cart = 'Корзина'
    basic = ['Тонни', 'Яра', 'Эдна']
    improved = ['Сьюзи', 'Генри', 'Элейн']
    perfect = ['Бадди', 'Роки', 'Кейли']
    context = {'title': title, 'back': back, 'cart': cart,
               'basic': basic,
               'improved': improved,
               'perfect': perfect
               }
    return render(request, 'buy.html', context)


def cart_index(request):
    title = 'мой сайт'
    back = 'Вернуться на главную страницу'
    cart = 'Корзина'
    context = {'title': title, 'back': back, 'cart': cart}
    return render(request, 'cart.html', context)