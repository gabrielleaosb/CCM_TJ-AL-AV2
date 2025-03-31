from django.shortcuts import render
from .models import SelfieHistorica

def home(request):
    return render(request, 'ccmtj/home.html')

def selfie_historica(request):
    thumbs = SelfieHistorica.objects.all()
    return render(request, 'ccmtj/selfie.html', {'thumbs': thumbs})

def qr_scan(request):
    return render(request, 'ccmtj/qr-scan.html')
