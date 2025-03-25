from django.urls import path
from .views import home, selfie_historica

urlpatterns = [
    path('', home, name='home'),
    path('selfie/', selfie_historica, name='selfie_historica')
]
