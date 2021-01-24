from django.http import HttpResponse
from django.shortcuts import render, redirect
# Import all the Form classes needed
from .forms import DossierForm
# Used for dynamic URLs notably
from .models import *

from pdf_writer4 import pdf


# Create your views here.

def download_pdf(request, dossier_id):
    dossier = Dossier.objects.get(id=dossier_id)

    pdf(request)

    context = {'dossier': dossier}

    return render(request, context)


def home(request):
    return render(request, 'ERP/Project_Form.html')


# Django form for Dossier class
def create_dossier(request):

    form = DossierForm()

    if request.method == 'POST':
        form = DossierForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirection after form is
            return redirect('/')

    context = {'form': form}
    return render(request, 'ERP/dossier_form.html', context)


def update_dossier(request, dossier_id):
    # Dynamic url setup, gets data relative to the dossier queried
    dossier = Dossier.objects.get(id=dossier_id)
    form = DossierForm(instance=dossier)

    if request.method == 'POST':
        form = DossierForm(request.POST, instance=dossier)
        if form.is_valid():
            form.save()
            # Redirection after form is
            return redirect('/')

    context = {'form': form}
    return render(request, 'ERP/dossier_form.html', context)


def delete_dossier(request, dossier_id):
    dossier = Dossier.objects.get(id=dossier_id)

    if request.method == 'POST':
        dossier.delete()
        return redirect('/')

    context = {'item': dossier}
    return render(request, 'ERP/delete.html', context)


# def projects(request):
    # return HttpResponse('Liste des projets')


# def newProjectForm(request):
    # return HttpResponse('Formulaire de création d\'un nouveau projet')
