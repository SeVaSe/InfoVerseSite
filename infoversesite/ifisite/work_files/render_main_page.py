from django.shortcuts import render
from ifisite.models import Command

def render_main(request):
    commands = Command.objects.all()  # Получаем все объекты из модели Command
    print(commands)
    return render(request, 'ifisite/main_page.html', {'commands': commands})
