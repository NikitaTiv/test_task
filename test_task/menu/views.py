from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def get_menu(request: WSGIRequest) -> HttpResponse:
    return render(request, 'menu/menu.html')
