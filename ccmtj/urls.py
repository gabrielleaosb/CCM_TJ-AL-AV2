from django.urls import path
from .views import home, selfie_historica, qr_scan, agenda, acessibilidade, ccmtjal, leve_para_casa, info_app, ficha_tecnica

urlpatterns = [
    path('', home, name='home'),
    path('selfie/', selfie_historica, name='selfie_historica'),
    path('qr-scan/', qr_scan, name='qr_scan'),
    path('agenda/', agenda, name='agenda'),
    path('acessibilidade/', acessibilidade, name='acessibilidade'),
    path('ccmtjal/', ccmtjal, name='ccmtjal'),
    path('leve-para-casa', leve_para_casa, name='leve_para_casa'),
    path('info-app', info_app, name='info_app'),
    path('ficha-tecnica', ficha_tecnica, name='ficha_tecnica')

]
