from django.shortcuts import render

from .forms import UserRegister
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView


# Create your views here.

def main_page(request):
    h1text = 'Главная страница'
    context = {
        'h1text': h1text,
    }
    return render(request, 'main_page.html', context)


class Shop(ListView):
    paginate_by = 2
    model = Game
    template_name = 'games.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['h1text'] = 'Игры'
        context['title'] = 'Игры'
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


def cart(request):
    h1text = 'Корзина'
    context = {
        'h1text': h1text,
    }
    return render(request, 'cart.html', context)


def platform(request):
    h1text = 'Главная страница'
    context = {
        'h1text': h1text,
    }
    return render(request, 'platform.html', context)


def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    form = UserRegister(request.POST)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        repeat_password = form.cleaned_data["repeat_password"]
        age = form.cleaned_data["age"]
        if password == repeat_password and int(age) >= 18 and username not in [x.name for x in users]:
            Buyer.objects.create(name=username, age=age)
            return HttpResponse(f'Приветствуем {username}')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in [x.name for x in users]:
            info['error'] = 'Пользователь уже существует'
    return render(request, 'registration_page.html', context=info)


def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")
        if password == repeat_password and int(age) >= 18 and username not in [x.name for x in users]:
            Buyer.objects.create(name=username, age=age)
            return HttpResponse(f'Приветствуем {username}')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in [x.name for x in users]:
            info['error'] = 'Пользователь уже существует'
    return render(request, 'registration_page.html', context=info)
