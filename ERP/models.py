from django.db import models


# Create your models here.

# After adding data run manage.py, then makemigrations, then migrate , then register in the admin


from pdf_writer4 import pdf


class PDF_data():

    template = r'C:\Users\Mathi\Documents\Coding\PDF_Templates\Test_Contract.pdf'  # location of the pdf template
    pdf_path = pdf(request=True, template=r'C:\Users\Mathi\Documents\Coding\PDF_Templates\Test_Contract.pdf')

print(pdf(request=True, template=r'C:\Users\Mathi\Documents\Coding\PDF_Templates\Test_Contract.pdf'))

class Dossier(models.Model):

    TYPE_EQUIPEMENT = (
        ('Matériel informatique', 'Matériel informatique'),
        ('Equipement industriel', 'Equipement industriel'),
        ('Logiciels', 'Logiciels'),
        ('Equipement médical', 'Equipement médical'),
        ('Autre équipement', 'Autre équipement'),
    )
    DUREE = (
        ('24 mois', '24 mois'),
        ('36 mois', '36 mois'),
        ('48 mois', '48 mois'),
        ('60 mois', '60 mois'),
        ('72 mois', '72 mois'),
        ('84 mois', '84 mois'),
    )
    PERIODICITE = (
        ('mensuel', 'mensuel'),
        ('trimestriel', 'trimestriel'),
    )

    # Données client, one to many relationship call client data
    # client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    client_siren = models.CharField(max_length=20, null=True, blank=True)
    client_raison_sociale = models.CharField(max_length=100, null=True, blank=True)
    client_adresse = models.CharField(max_length=200, null=True, blank=True)
    client_code_postal = models.CharField(max_length=20, null=True, blank=True)
    client_ville = models.CharField(max_length=20, null=True, blank=True)
    client_RCS = models.CharField(max_length=20, null=True, blank=True)
    client_lieu_d_installation = models.CharField(max_length=20, null=True, blank=True)
    client_telephone_fixe = models.CharField(max_length=20, null=True, blank=True)
    client_telephone_portable = models.CharField(max_length=20, null=True, blank=True)
    client_IBAN = models.CharField(max_length=50, null=True, blank=True)
    client_BIC = models.CharField(max_length=20, null=True, blank=True)

    # Données collaborateur
    # collaborateur = models.ForeignKey(Collaborateur, null=True, on_delete=models.SET_NULL)
    collaborateur_nom = models.CharField(max_length=20, null=True, blank=True)
    collaborateur_numero = models.CharField(max_length=20, null=True, blank=True)

    # Données dossier
    n_de_contrat = models.CharField(max_length=20, null=True, blank=True)
    montant = models.CharField(max_length=9, null=True, blank=True)
    type_equipement = models.CharField(max_length=50, null=True, choices=TYPE_EQUIPEMENT, blank=True)
    duree = models.CharField(max_length=20, null=True, choices=DUREE, blank=True)
    periodicite = models.CharField(max_length=20, null=True, choices=PERIODICITE, blank=True)
    nom_fournisseur = models.CharField(max_length=100, null=True, blank=True)
    siren_fournisseur = models.CharField(max_length=20, null=True, blank=True)
    loyer = models.CharField(max_length=10, null=True, blank=True)

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.client_raison_sociale) + " / Contrat n°" + str(self.n_de_contrat)




# class Client(models.Model):

# raison_sociale = models.CharField(max_length=100, null=True)
# siren = models.CharField(max_length=20, null=True)
# adresse = models.CharField(max_length=200, null=True)
# code_postal = models.CharField(max_length=20, null=True)
# ville = models.CharField(max_length=20, null=True)
# RCS = models.CharField(max_length=20, null=True)
# lieu_d_installation = models.CharField(max_length=20, null=True)
# telephone_fixe = models.CharField(max_length=20, null=True)
# telephone_portable = models.CharField(max_length=20, null=True)
# IBAN = models.CharField(max_length=50, null=True)
# BIC = models.CharField(max_length=20, null=True)

# date_creation = models.DateTimeField(auto_now_add=True)

# def __str__(self):
# return self.raison_sociale


# class Collaborateur(models.Model):
# nom_collaborateur = models.CharField(max_length=20, null=True)
# numero_collaborateur = models.CharField(max_length=20, null=True)


# def __str__(self):
# return self.nom_collaborateur + ' / N° : ' + str(self.numero_collaborateur)



