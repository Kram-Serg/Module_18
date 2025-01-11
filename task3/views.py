from django.shortcuts import render


# Create your views here.

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
    context = {'title': title, 'back': back, 'cart': cart}
    return render(request, 'buy.html', context)


def cart_index(request):
    title = 'мой сайт'
    back = 'Вернуться на главную страницу'
    cart = 'Корзина'
    context = {'title': title, 'back': back, 'cart': cart}
    return render(request, 'cart.html', context)