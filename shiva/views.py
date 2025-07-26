from django.shortcuts import render


def Hello(request):
    return render(request, 'i.html')
# Create your views here.

