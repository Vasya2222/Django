from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    html = '''
    <h1>Эта главная страница</h1>
    '''
    return HttpResponse(html)


def about_me(request):
    html = '''
        <h1>Обо мне</h1>
        <p> Меня зовут Василий. Мне 20 лет. И я сейчас делаю 1 дз по Djagno в Geekbrains.
        '''
    return HttpResponse(html)