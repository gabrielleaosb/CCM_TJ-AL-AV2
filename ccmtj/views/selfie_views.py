from ..models import SelfieHistorica
from django.shortcuts import render

def selfie_historica(request):
    thumbs = SelfieHistorica.objects.all()
    return render(request, 'ccmtj/selfie/selfie.html', {'thumbs': thumbs})