from django.urls import path
from .views import home, selfie_historica, qr_scan, agenda

urlpatterns = [
    path('', home, name='home'),
    path('selfie/', selfie_historica, name='selfie_historica'),
    path('qr-scan/', qr_scan, name='qr-scan'),
    path('agenda/', agenda, name='agenda')
]
