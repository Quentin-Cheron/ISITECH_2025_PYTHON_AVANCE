from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("book.static_urls")),
    path("admin/", admin.site.urls),
    path("book/", include("book.urls", namespace="book")),
    path("author/", include("author.urls", namespace="author")),
    path("loan/", include("book.loan_urls", namespace="loan")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
