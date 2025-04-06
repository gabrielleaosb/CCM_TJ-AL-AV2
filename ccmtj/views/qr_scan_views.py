from django.shortcuts import render

def qr_scan(request):
    return render(request, 'ccmtj/qr_scan/qr-scan.html')