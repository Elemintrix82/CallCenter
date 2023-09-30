from django.contrib import admin

import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.http import JsonResponse
from django.urls import path

from .models import Appel, Intervention, Magasin, Mail, Produit, Satisfaction


@admin.register(Magasin)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'nom',
        'adresse',
        'code_postal',
        'ville',
        'date_enregistrement',
    )
    search_fields = ['nom', 'adresse', 'code_postal', 'ville', 'date_enregistrement']
    ordering = ['date_enregistrement']
    list_per_page = 10
    list_max_show_all = 10
    

@admin.register(Appel)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'id_client',
        'date_appel',
        'heure_appel',
        'duree_appel',
        'sujet_appel',
        'etat_appel',
        'date_enregistrement',
    )
    search_fields = ['id_client', 'date_appel', 'sujet_appel', 'etat_appel', 'date_enregistrement']
    ordering = ['date_enregistrement']
    list_per_page = 10
    list_max_show_all = 10
    

@admin.register(Mail)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'nom',
        'sexe',
        'email',
        'subject',
        'message',
        'date_enregistrement',
    )
    search_fields = ['nom', 'email', 'sexe', 'date_enregistrement']
    ordering = ['date_enregistrement']
    list_per_page = 10
    list_max_show_all = 10
    
    
@admin.register(Produit)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'nom',
        'description',
        'prix',
        'image',
        'date_enregistrement',
    )
    search_fields = ['nom', 'description', 'prix', 'date_enregistrement']
    ordering = ['date_enregistrement']
    list_per_page = 10
    list_max_show_all = 10
    

@admin.register(Intervention)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'id_appel',
        'id_technicien',
        'date',
        'heure',
        'duree',
        'description',
        'etat',
        'date_enregistrement',
    )
    search_fields = ['id_client', 'date_appel', 'sujet_appel', 'etat_appel', 'date_enregistrement']
    ordering = ['date_enregistrement']
    list_per_page = 10
    list_max_show_all = 10
    
    
@admin.register(Satisfaction)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'nom',
        'email',
        'qualite',
        'competence',
        'temps_reponse',
        'resolution',
        'recommandation',
        'date_enregistrement',
    )
    search_fields = [   
                    'num',     
                    'nom',
                    'email',
                    'qualite',
                    'competence',
                    'temps_reponse',
                    'resolution',
                    'recommandation',
                    'date_enregistrement',
                ]
    ordering = ['date_enregistrement']
    date_hierarchy  =  "created_at"
    list_per_page = 10
    list_max_show_all = 10
    
    # Injecter des données de graphique lors du chargement de la page dans la vue ChangeList
    def changelist_view(self, request, extra_context=None):
        chart_data = self.chart_data()
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}
        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        extra_urls = [
            path("chart_data/", self.admin_site.admin_view(self.chart_data_endpoint))
        ]
        # NOTE! Nos URL personnalisées doivent être placées avant les URL par défaut, car celles
        # ceux par défaut correspondent à n'importe quoi.
        return extra_urls + urls

    # Point de terminaison JSON pour générer des données de graphique utilisées pour le chargement dynamique
    # via JS.
    def chart_data_endpoint(self, request):
        chart_data = self.chart_data()
        return JsonResponse(list(chart_data), safe=False)

    def chart_data(self):
        return (
            Satisfaction.objects.annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(y=Count("qualite"))
            .order_by("-date")
        )
