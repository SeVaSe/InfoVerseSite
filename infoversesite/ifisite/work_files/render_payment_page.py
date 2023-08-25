from django.shortcuts import render
from django.http import HttpResponse


def render_payment(request):
    return render(request, 'ifisite/payment_page.html')