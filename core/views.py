from django.shortcuts import render

# Create your views here.


def landing(request):
    template = 'landing.html'

    contexts = {}

    return render(request, template, contexts)


def about(request):
    template = 'about.html'

    contexts = {}

    return render(request, template, contexts)


def contact(request):
    template = 'contact.html'

    contexts = {}

    return render(request, template, contexts)


def gallery(request):
    template = 'gallery.html'

    contexts = {}

    return render(request, template, contexts)


def merchandise(request):
    template = 'merchandise.html'

    contexts = {}

    return render(request, template, contexts)


def closing(request):
    template = 'closing.html'

    contexts = {}

    return render(request, template, contexts)
