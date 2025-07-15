from django.shortcuts import render

def index(request):
    return render(request, 'commitees/index.html')
