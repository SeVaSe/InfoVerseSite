from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main_page(request):
    return HttpResponse("Главная страница")


def commands(request):
    return HttpResponse("Команды")
