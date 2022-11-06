from django.shortcuts import render

# Create your views here.

def logar(request):
    return render(request, 'dashboard.html')