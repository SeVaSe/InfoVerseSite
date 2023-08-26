from django.shortcuts import render


def render_main(request):
    return render(request, 'ifisite/main_page.html')
