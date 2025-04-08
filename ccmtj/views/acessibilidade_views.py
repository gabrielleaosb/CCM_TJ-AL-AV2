from django.shortcuts import render
from ..models import AudioDescricao

def acessibilidade_index(request):
    return render(request, 'ccmtj/acessibilidade/index.html')

def acessibilidade_audio_descricao(request):
    audio_list = AudioDescricao.objects.all()
    return render(request, 'ccmtj/acessibilidade/audio_descricao.html', {'audio_list': audio_list})

def acessibilidade_braile(request):
    return render(request, 'ccmtj/acessibilidade/braile.html')

def acessibilidade_video_com_libras(request):
    return render(request, 'ccmtj/acessibilidade/video_com_libras.html')

def acessibilidade_video_com_legendas(request):
    return render(request, 'ccmtj/acessibilidade/video_com_legendas.html')
