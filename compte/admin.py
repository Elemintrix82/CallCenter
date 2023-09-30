from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur, Client, Technicien

# Register your models here.
class UtilisateurAdmin(UserAdmin):
    list_display = ('num', 'email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    list_per_page = 20
    list_max_show_all = 10
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



# Traduire les noms des modèles
Utilisateur._meta.verbose_name ='Utilisateur'
Utilisateur._meta.verbose_name_plural = 'Utilisateurs'

admin.site.register(Utilisateur, UtilisateurAdmin)


@admin.register(Client)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'nom', 
        'prenom', 
        'email', 
        'telephone',
        'date_enregistrement',
        )
    search_fields = ['nom', 'email', 'date_enregistrement']
    ordering = ['date_enregistrement']
    list_per_page = 10
    list_max_show_all = 10
    

@admin.register(Technicien)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'nom', 
        'prenom', 
        'email', 
        'telephone',
        'sexe',
        'date_enregistrement',
        )
    search_fields = ['nom', 'email', 'sexe', 'date_enregistrement']
    ordering = ['date_enregistrement']
    list_per_page = 10
    list_max_show_all = 10