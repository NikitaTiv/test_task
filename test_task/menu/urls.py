from django.urls import path

from menu.views import get_menu

urlpatterns = [
    path('', get_menu, name='home'),
]
