from django.shortcuts import render
from .models import SelfieHistorica

def home(request):
    return render(request, 'ccmtj/home.html')

def selfie_historica(request):
    thumbs = SelfieHistorica.objects.all()
    return render(request, 'ccmtj/selfie.html', {'thumbs': thumbs})

def qr_scan(request):
    return render(request, 'ccmtj/qr-scan.html')

def agenda(request):
    return render(request, 'ccmtj/agenda.html')

def acessibilidade(request):
    return render(request, 'ccmtj/acessibilidade.html')

def ccmtjal(request):
    return render(request, 'ccmtj/ccmtjal.html')

def leve_para_casa(request):
    return render(request, 'ccmtj/leve-para-casa.html')

def info_app(request):
    origem = request.GET.get('from', 'home')
    return render(request, 'ccmtj/info-app.html', {'origem': origem})

def ficha_tecnica(request):
    return render(request, 'ccmtj/ficha-tecnica.html')
