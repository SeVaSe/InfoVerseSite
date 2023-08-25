from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main_page(request):
    return render(request, 'ifisite/main_page.html')


def commands(request):
    return HttpResponse("Команды")
