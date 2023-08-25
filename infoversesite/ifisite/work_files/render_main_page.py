from django.shortcuts import render
from django.http import HttpResponse


def render_main(request):
    return render(request, 'ifisite/main_page.html')