from django.urls import path
from ccmtj.views import (
    home, selfie_historica, qr_scan, agenda, ccmtjal,
    acessibilidade_index, acessibilidade_audio_descricao, acessibilidade_braile, acessibilidade_video_com_libras,
    acessibilidade_video_com_legendas,
    leve_para_casa_index, leve_para_casa_videos, leve_para_casa_imagens, leve_para_casa_passeio_360, leve_para_casa_documentos,
    info_app, ficha_tecnica
)


urlpatterns = [
    path('', home, name='home'),
    path('selfie/', selfie_historica, name='selfie_historica'),
    path('qr-scan/', qr_scan, name='qr_scan'),
    path('agenda/', agenda, name='agenda'),

    # Acessibilidade
    path('acessibilidade/', acessibilidade_index, name='acessibilidade'),
    path('acessibilidade/audio-descricao', acessibilidade_audio_descricao, name='acessibilidade_audio_descricao'),
    path('acessibilidade/braile', acessibilidade_braile, name='acessibilidade_braile'),
    path('acessibilidade/video-com-libras', acessibilidade_video_com_libras, name='acessibilidade_video_com_libras'),
    path('acessibilidade/video-com-legendas', acessibilidade_video_com_legendas, name='acessibilidade_video_com_legendas'),

    # CCMTJAL
    path('ccmtjal/', ccmtjal, name='ccmtjal'),

    # Leve para Casa
    path('leve-para-casa', leve_para_casa_index, name='leve_para_casa'),
    path('leve-para-casa/videos', leve_para_casa_videos, name='leve_para_casa_videos'),
    path('leve-para-casa/imagens', leve_para_casa_imagens, name='leve_para_casa_imagens'),
    path('leve-para-casa/passeio-360', leve_para_casa_passeio_360, name='leve_para_casa_passeio_360'),
    path('leve-para-casa/documentos', leve_para_casa_documentos, name='leve_para_casa_documentos'),  

    # Info App
    path('info-app', info_app, name='info_app'),
    path('ficha-tecnica', ficha_tecnica, name='ficha_tecnica')

]
