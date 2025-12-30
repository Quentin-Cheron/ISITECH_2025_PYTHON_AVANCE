from django.urls import path
from . import loan_views

app_name = 'loan'

urlpatterns = [
    path('', loan_views.loan_list, name='list'),
    path('overdue/', loan_views.loan_overdue, name='overdue'),
    path('history/', loan_views.loan_history, name='history'),
    path('create/', loan_views.loan_create, name='create'),
    path('<int:pk>/return/', loan_views.loan_return, name='return'),
]
