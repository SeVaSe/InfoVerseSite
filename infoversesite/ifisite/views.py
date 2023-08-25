from django.shortcuts import render
from django.http import HttpResponse

from .work_files import render_main_page as rmp, render_payment_page as rpp, render_commands_page as rcp,\
    render_feedback_page as rfp


# Create your views here.
def main_page(request):
    return rmp.render_main(request)


def commands(request):
    return rcp.render_commands(request)


def feedback(request):
    return rfp.render_feedback(request)


def payment(request):
    return rpp.render_payment(request)
