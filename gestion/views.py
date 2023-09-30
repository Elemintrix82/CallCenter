from django.http import HttpResponse
from django.shortcuts import render

from django.conf import settings
from django.core.mail import send_mail

from compte.models import Client
from .forms import MailForm, SatisfactionForm



def home(request):
    current_page = request.path
    context = {
        'current_page': current_page,
    }
    return render(request, 'gestion/home.html', context)


def about(request):
    current_page = request.path
    context = {
        'current_page': current_page,
    }
    return render(request, 'gestion/about.html', context)


def service(request):
    current_page = request.path
    context = {
        'current_page': current_page,
    }
    return render(request, 'gestion/service.html', context)


def contact(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            telephone = form.cleaned_data['telephone']
            addresse = form.cleaned_data['addresse']
            code_postal = form.cleaned_data['code_postal']
            ville = form.cleaned_data['ville']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            mail = form.save()  # Enregistre les données du formulaire dans le modèle Mail

            # Crée une instance du modèle Client et lui attribue les valeurs correspondantes du modèle Mail
            client = Client(nom=mail.nom, prenom=mail.prenom, email=mail.email, telephone=mail.telephone, addresse=mail.addresse, code_postal=mail.code_postal, ville=mail.ville)
            client.save()  # Enregistre l'instance du modèle Client dans la base de données

            titre = f' CallCenter | nom: {nom} {prenom}, nuémro: {telephone}, adresse: {addresse}, code postal: {code_postal}, ville: {ville} avec l\'email {email} a dit: << {subject} >>"'
            print(f' CallCenter | nom: {nom} {prenom}, nuémro: {telephone}, adresse: {addresse}, code postal: {code_postal}, ville: {ville} avec l\'email {email} a dit: << {subject} >>"')

            send_mail(
                titre,
                message,
                settings.EMAIL_HOST_USER,
                ['valdezwilson82@gmail.com']
            )

            context = {
                'form': form,
                'message': 'Votre message a été envoyé avec succès.'
            }
            return render(request, 'gestion/contact.html', context)
    else:
        form = MailForm()

    current_page = request.path
    context = {
        'current_page': current_page,
        'form': form
    }
    return render(request, 'gestion/contact.html', context)


def satisfaction(request):
    
    form = SatisfactionForm()
    
    if request.method == 'POST':
        form = SatisfactionForm(request.POST)
        if form.is_valid():
            form.cleaned_data['nom']
            email=form.cleaned_data['email']
            form.cleaned_data['qualite']
            form.cleaned_data['competence']
            form.cleaned_data['temps_reponse']
            form.cleaned_data['resolution']
            form.cleaned_data['recommandation']
            form.cleaned_data['commentaire']
            try:
                Client.objects.get(email=email)
                form.save()
                context = {
                    'form': form,
                    'message': 'Votre message a été envoyé avec succès.'
                }
                return render(request, 'gestion/satisfaction.html', context)
            except Client.DoesNotExist:
                context = {
                    'form': form,
                    'message': 'Veuillez entrer l\'email correspondant au formulaire contact que vous nous avez envoyé, svp.'
                }
                return render(request, 'gestion/satisfaction.html', context)
    current_page = request.path
    context = {
        'current_page': current_page,
        'form': form
    }
    return render(request, 'gestion/satisfaction.html', context)