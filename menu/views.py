from django.shortcuts import render


def index(request, slug=None):
    return render(request, 'index.html')
