from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from compte.models import Client, Technicien


class Magasin(models.Model):
    num = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    code_postal = models.CharField(max_length=5)
    ville = models.CharField(max_length=100)
    date_enregistrement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    
    
class Appel(models.Model):
    ETAT_APPEL_CHOICES = (
        ('EN_ATTENTE', 'En attente'),
        ('EN_COURS', 'En cours'),
        ('TERMINE', 'Terminé'),
    )
    
    num = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_appel = models.DateTimeField()
    heure_appel = models.TimeField()
    duree_appel = models.IntegerField()
    sujet_appel = models.CharField(max_length=100)
    description_appel = models.TextField()
    etat_appel = models.CharField(max_length=100, choices=ETAT_APPEL_CHOICES)
    date_enregistrement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_client.nom
    

class Mail(models.Model):
    num = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=10)
    addresse = models.CharField(max_length=255)
    code_postal = models.CharField(max_length=5)
    ville = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_enregistrement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    
    
class Produit(models.Model):
    num = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.IntegerField()
    image = models.ImageField(upload_to="images")
    fiche_technique = models.FileField(upload_to='documents/')
    date_enregistrement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    
    
class Intervention(models.Model):
    ETAT_CHOICES = (
        ('EN_ATTENTE', 'En attente'),
        ('EN_COURS', 'En cours'),
        ('TERMINE', 'Terminé'),
    )
    
    num = models.AutoField(primary_key=True)
    id_appel = models.ForeignKey(Appel, on_delete=models.CASCADE)
    id_technicien = models.ForeignKey(Technicien, on_delete=models.CASCADE)
    date = models.DateTimeField()
    heure = models.TimeField()
    duree = models.IntegerField()
    description = models.TextField()
    etat = models.CharField(max_length=100, choices=ETAT_CHOICES)
    date_enregistrement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_technicien.nom
    
    
class Satisfaction(models.Model):
    num = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    qualite = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    competence = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    temps_reponse = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    resolution = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    recommandation = models.BooleanField(default=True)
    commentaire = models.TextField(blank=True)
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Satisfaction de {}'.format(self.nom)