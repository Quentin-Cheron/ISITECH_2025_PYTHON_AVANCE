from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('', views.author_list, name='list'),
    path('<int:pk>/', views.author_detail, name='detail'),
]
