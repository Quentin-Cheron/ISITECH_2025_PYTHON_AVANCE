from django.urls import path
from . import static_views

app_name = 'static'

urlpatterns = [
    path('', static_views.home, name='home'),
    path('about/', static_views.about, name='about'),
    path('contact/', static_views.contact, name='contact'),
]
