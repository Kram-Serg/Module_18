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
    b_1 = 'Тонни'
    b_2 = 'Яра'
    b_3 = 'Эдна'
    i_1 = 'Сьюзи'
    i_2 = 'Генри'
    i_3 = 'Элейн'
    p_1 = 'Бадди'
    p_2 = 'Роки'
    p_3 = 'Кейли'
    context = {'title': title, 'back': back, 'cart': cart,
               'b_1': b_1, 'b_2': b_2,'b_3': b_3,
               'i_1': i_1, 'i_2': i_2, 'i_3': i_3,
               'p_1': p_1, 'p_2': p_2, 'p_3': p_3
               }
    return render(request, 'buy.html', context)


def cart_index(request):
    title = 'мой сайт'
    back = 'Вернуться на главную страницу'
    cart = 'Корзина'
    context = {'title': title, 'back': back, 'cart': cart}
    return render(request, 'cart.html', context)
