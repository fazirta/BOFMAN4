from django.shortcuts import render

# Create your views here.

def landing(request):
    template = 'landing.html'

    contexts = {}

    return render(request, template, contexts)