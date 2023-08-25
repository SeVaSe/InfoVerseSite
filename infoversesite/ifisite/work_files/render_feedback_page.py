from django.shortcuts import render
from django.http import HttpResponse


def render_feedback(request):
    return render(request, 'ifisite/feedback_page.html')