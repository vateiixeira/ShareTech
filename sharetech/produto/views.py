from django.shortcuts import render


def shop(request):
    template = 'shop.html'
    return render(request,template)
