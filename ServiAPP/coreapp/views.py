from django.shortcuts import render

def home(request):
    return render(request, 'coreapp/home.html')


def servicios(request):
    return render(request, 'coreapp/servicios.html')