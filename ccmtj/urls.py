from django.urls import path
from .views import home, selfie_historica, qr_scan, agenda, acessibilidade, ccmtjal, leve_para_casa, info_app

urlpatterns = [
    path('', home, name='home'),
    path('selfie/', selfie_historica, name='selfie_historica'),
    path('qr-scan/', qr_scan, name='qr-scan'),
    path('agenda/', agenda, name='agenda'),
    path('acessibilidade/', acessibilidade, name='acessibilidade'),
    path('ccmtjal/', ccmtjal, name='ccmtjal'),
    path('leve-para-casa', leve_para_casa, name='leve-para-casa'),
    path('info-app', info_app, name='info-app')

]
