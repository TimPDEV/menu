from django.urls import path

from menu.views import index

urlpatterns = [
    path('<slug:slug>', index, name='sub'),
    path('', index, name='index'),
]
