from django.shortcuts import render

from blog import models

# Create your views here.


def landing(request):
    blogs = models.Blog.objects.all()
    template = 'landing.html'

    contexts = {
        'blogs': blogs,
    }

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


def timeline(request):
    template = 'timeline.html'

    contexts = {}

    return render(request, template, contexts)
