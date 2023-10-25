from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('merchandise', views.merchandise, name='merchandise'),
    path('closing', views.closing, name='closing'),
]
