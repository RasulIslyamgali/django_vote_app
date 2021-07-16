from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Добро пожаловать. Вы попали на страницу для опроса.')


def detail(request, question_id):
    return HttpResponse('Вы смотрите на вопрос %s' % question_id)


def results(request, question_id):
    response = 'Вы смотрите на результат вопроса %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('Вы голосуете по вопросу %s' % question_id)


