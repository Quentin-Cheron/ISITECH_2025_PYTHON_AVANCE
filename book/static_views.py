from django.shortcuts import render


def home(request):
    """Page d'accueil"""
    from .models import Book
    from book.models import Loan
    from author.models import Author
    
    context = {
        'total_books': Book.objects.count(),
        'total_authors': Author.objects.count(),
        'active_loans': Loan.objects.filter(status='active').count(),
        'available_books': Book.objects.filter(available_copies__gt=0).count(),
        'recent_books': Book.objects.all().order_by('-added_date')[:5],
    }
    
    return render(request, 'static/home.html', context)


def about(request):
    """Page À propos"""
    return render(request, 'static/about.html')


def contact(request):
    """Page de contact"""
    return render(request, 'static/contact.html')
