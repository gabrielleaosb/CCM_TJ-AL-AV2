from django.shortcuts import render

def info_app(request):
    origem = request.GET.get('from', 'home')
    return render(request, 'ccmtj/info_app/info-app.html', {'origem': origem})

def ficha_tecnica(request):
    return render(request, 'ccmtj/info_app/ficha-tecnica.html')