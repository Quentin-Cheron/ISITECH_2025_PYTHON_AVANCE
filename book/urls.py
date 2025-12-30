from django.urls import path

from book import views

app_name = "book"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("search/", views.search, name="search"),
]
