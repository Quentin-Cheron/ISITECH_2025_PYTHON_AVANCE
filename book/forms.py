from django import forms
from datetime import date, timedelta
from .models import Loan


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower_name', 'borrower_email', 'library_card_number', 'due_date']
        widgets = {
            'book': forms.Select(attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full'}),
            'borrower_name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full', 'placeholder': 'Nom complet'}),
            'borrower_email': forms.EmailInput(attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full', 'placeholder': 'email@example.com'}),
            'library_card_number': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full', 'placeholder': 'Numéro de carte'}),
            'due_date': forms.DateInput(attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full', 'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrer uniquement les livres disponibles
        self.fields['book'].queryset = self.fields['book'].queryset.filter(available_copies__gt=0)
        
        # Date de retour par défaut : 14 jours
        if not self.instance.pk:
            self.fields['due_date'].initial = date.today() + timedelta(days=14)
    
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < date.today():
            raise forms.ValidationError("La date de retour ne peut pas être dans le passé.")
        return due_date
