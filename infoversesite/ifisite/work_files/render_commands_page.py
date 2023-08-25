from django.shortcuts import render
from django.http import HttpResponse


def render_commands(request):
    return render(request, 'ifisite/commands_page.html')