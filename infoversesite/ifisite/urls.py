from django.urls import path

from .views import *


urlpatterns = [
    path('', main_page, name='main_p'),  # 127.0.0.1:8000/
    path('commands/', commands, name='commands_p'),  # 127.0.0.1:8000/commands/
    path('feedback/', feedback, name='feedback_p'),  # 127.0.0.1:8000/feedback/
    path('payment/', payment, name='payment_p')  # 127.0.0.1:8000/payment/
]