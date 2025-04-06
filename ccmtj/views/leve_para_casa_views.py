from django.shortcuts import render

def leve_para_casa_index(request):
    return render(request, 'ccmtj/leve_para_casa/index.html')

def leve_para_casa_videos(request):
    return render(request, 'ccmtj/leve_para_casa/videos.html')

def leve_para_casa_imagens(request):
    return render(request, 'ccmtj/leve_para_casa/imagens.html')

def leve_para_casa_passeio_360(request):
    return render(request, 'ccmtj/leve_para_casa/passeio_360.html')

def leve_para_casa_documentos(request):
    return render(request, 'ccmtj/leve_para_casa/documentos.html')
