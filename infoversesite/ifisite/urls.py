from django.urls import path

from .views import *


urlpatterns = [
    path('', main_page),  # 127.0.0.1:8000/
    path('commands/', commands),  # 127.0.0.1:8000/commands/
    path('feedback/', feedback),  # 127.0.0.1:8000/feedback/
    path('payment/', payment)  # 127.0.0.1:8000/payment/
]