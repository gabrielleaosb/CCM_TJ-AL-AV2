from django.shortcuts import render

def home(request):
    return render(request, 'ccmtj/home.html')

def selfie_historica(request):
    return render(request, 'ccmtj/selfie.html')
