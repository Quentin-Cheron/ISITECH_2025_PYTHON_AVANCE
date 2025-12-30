from datetime import date

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import LoanForm
from .models import Loan


def loan_list(request):
    """Liste des emprunts actifs"""
    loans = Loan.objects.filter(status="active").select_related("book")

    # Pagination
    paginator = Paginator(loans, 20)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "loan/loan_list.html",
        {"page_obj": page_obj, "loans": page_obj, "title": "Emprunts actifs"},
    )


def loan_overdue(request):
    """Liste des emprunts en retard"""
    loans = Loan.objects.filter(
        status="active", due_date__lt=date.today()
    ).select_related("book")

    # Pagination
    paginator = Paginator(loans, 20)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "loan/loan_list.html",
        {
            "page_obj": page_obj,
            "loans": page_obj,
            "title": "Emprunts en retard",
            "is_overdue": True,
        },
    )


def loan_history(request):
    """Historique de tous les emprunts"""
    search_query = request.GET.get("search", "")

    loans = Loan.objects.all().select_related("book")

    if search_query:
        loans = loans.filter(borrower_name__icontains=search_query)

    # Pagination
    paginator = Paginator(loans, 20)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "loan/loan_list.html",
        {
            "page_obj": page_obj,
            "loans": page_obj,
            "title": "Historique des emprunts",
            "show_all": True,
        },
    )


def loan_create(request):
    """Formulaire de création d'emprunt"""
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)

            # Vérifier la disponibilité
            if loan.book.available_copies > 0:
                # Décrémenter les exemplaires disponibles
                loan.book.available_copies -= 1
                loan.book.save()

                # Sauvegarder l'emprunt
                loan.save()

                messages.success(
                    request, f'Emprunt créé avec succès pour "{loan.book.title}"'
                )
                return redirect("loan:list")
            else:
                messages.error(request, "Ce livre n'est plus disponible.")
    else:
        form = LoanForm()

    return render(
        request, "loan/loan_form.html", {"form": form, "title": "Nouvel emprunt"}
    )


def loan_return(request, pk):
    """Formulaire de retour de livre"""
    loan = get_object_or_404(Loan, pk=pk)

    if request.method == "POST":
        if loan.status == "active":
            # Marquer comme retourné
            loan.status = "returned"
            loan.return_date = timezone.now()
            loan.save()

            # Incrémenter les exemplaires disponibles
            loan.book.available_copies += 1
            loan.book.save()

            messages.success(
                request, f'Livre "{loan.book.title}" retourné avec succès.'
            )
            return redirect("loan:list")
        else:
            messages.error(request, "Cet emprunt a déjà été retourné.")

    return render(request, "loan/loan_return.html", {"loan": loan})
