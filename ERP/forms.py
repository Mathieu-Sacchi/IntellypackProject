from django import forms
from django.forms import ModelForm
from .models import Dossier


class DossierForm(ModelForm):
    class Meta:
        model = Dossier
        fields = '__all__'
        widgets = {
            'client_siren': forms.TextInput(attrs={'class': 'form-control'}),
            'client_raison_sociale': forms.TextInput(attrs={'class': 'form-control'}),
            'client_adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'client_code_postal': forms.TextInput(attrs={'class': 'form-control'}),
            'client_ville': forms.TextInput(attrs={'class': 'form-control'}),
            'client_RCS': forms.TextInput(attrs={'class': 'form-control'}),
            'client_lieu_d_installation': forms.TextInput(attrs={'class': 'form-control'}),
            'client_telephone_fixe': forms.TextInput(attrs={'class': 'form-control'}),
            'client_telephone_portable': forms.TextInput(attrs={'class': 'form-control'}),
            'client_IBAN': forms.TextInput(attrs={'class': 'form-control'}),
            'client_BIC': forms.TextInput(attrs={'class': 'form-control'}),

            'collaborateur_nom': forms.TextInput(attrs={'class': 'form-control'}),
            'collaborateur_numero': forms.TextInput(attrs={'class': 'form-control'}),

            'n_de_contrat': forms.TextInput(attrs={'class': 'form-control'}),
            'montant': forms.TextInput(attrs={'class': 'form-control'}),
            'type_equipement': forms.Select(attrs={'class': 'form-control'}),
            'duree': forms.TextInput(attrs={'class': 'form-control'}),
            'periodicite': forms.Select(attrs={'class': 'form-control'}),
            'nom_fournisseur': forms.TextInput(attrs={'class': 'form-control'}),
            'siren_fournisseur': forms.TextInput(attrs={'class': 'form-control'}),
            'loyer': forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'client_siren': 'SIREN du Client ',
            'client_raison_sociale': 'Raison Sociale ',
            'client_adresse': "Adresse ",
            'client_code_postal': "Code Postal ",
            'client_ville': 'Ville ',
            'client_RCS': 'RCS ',
            'client_lieu_d_installation': 'Lieu d\'Installation ',
            'client_telephone_fixe': 'Téléphone Fixe ',
            'client_telephone_portable': 'Téléphone Portable ',
            'client_IBAN': 'IBAN ',
            'client_BIC': 'BIC ',

            'collaborateur_nom': 'Nom du Collaborateur ',
            'collaborateur_numero': 'Numéro du Collaborateur ',

            'n_de_contrat': 'N° du Contrat ',
            'montant': 'Montant ',
            'type_equipement': 'Type d\'Equipement ',
            'duree': 'Durée ',
            'periodicite': 'Périodicité ',
            'nom_fournisseur': 'Nom du Fournisseur ',
            'siren_fournisseur': 'SIREN du Fournisseur ',
            'loyer': 'Loyer ',

        }
