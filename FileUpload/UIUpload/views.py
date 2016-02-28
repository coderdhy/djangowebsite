from django.shortcuts import render

# Create your views here.


def uiaddfile(request):
    return render(request, 'pluploaddemo.html')

