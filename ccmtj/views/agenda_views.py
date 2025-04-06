from django.shortcuts import render

def agenda(request):
    return render(request, 'ccmtj/agenda/agenda.html')
