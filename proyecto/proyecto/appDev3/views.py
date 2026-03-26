from django.shortcuts import render

def index(request):
    """Vista principal para renderizar el CV"""
    return render(request, 'index.html')
