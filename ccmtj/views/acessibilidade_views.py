from django.shortcuts import render

def acessibilidade_index(request):
    return render(request, 'ccmtj/acessibilidade/index.html')

def acessibilidade_audio_descricao(request):
    return render(request, 'ccmtj/acessibilidade/audio_descricao.html')

def acessibilidade_braile(request):
    return render(request, 'ccmtj/acessibilidade/braile.html')

def acessibilidade_video_com_libras(request):
    return render(request, 'ccmtj/acessibilidade/video_com_libras.html')

def acessibilidade_video_com_legendas(request):
    return render(request, 'ccmtj/acessibilidade/video_com_legendas.html')
