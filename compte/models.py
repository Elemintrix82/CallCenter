from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have a username')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Utilisateur(AbstractBaseUser):
    num = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    username = models.CharField(max_length=100, unique=True, verbose_name='Username')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=100, verbose_name='Phone Number')
    
    # required
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')
    last_login = models.DateTimeField(auto_now_add=True, verbose_name='Last Login')
    is_admin = models.BooleanField(default=False, verbose_name='Is Admin')
    is_staff = models.BooleanField(default=False, verbose_name='Is Staff')
    is_active = models.BooleanField(default=False, verbose_name='Is Active')
    is_superadmin = models.BooleanField(default=False, verbose_name='Is Superadmin')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = MyAccountManager()
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.email
    
    # permission
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
    )
    
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to.',
    )
    
    def get_user_permissions(self, obj=None):
        """
        Renvoie l’ensemble des permissions (chaînes) que l’utilisateur obtient directement.

        Si obj est transmis, ne renvoie que les permissions d’utilisateur liées à cet objet spécifique.
        """
        return [
            permission
            for permission in self.user_permissions.all()
            if permission.content_type.model == obj.__class__
        ]

    def get_group_permissions(self, obj=None):
        """
        Renvoie l’ensemble des permissions (chaînes) que l’utilisateur obtient au travers des groupes auxquels il/elle appartient.

        Si obj est transmis, ne renvoie que les permissions de groupe liées à cet objet spécifique.
        """
        groups = self.groups.all()
        permissions = []

        for group in groups:
            permissions.extend(group.permissions.all())

        return [
            permission
            for permission in permissions
            if permission.content_type.model == obj.__class__
        ]

    def get_all_permissions(self, obj=None):
        """
        Renvoie l’ensemble des permissions (chaînes) que l’utilisateur obtient directement ou au travers des groupes auxquels il appartient.

        Si obj est transmis, ne renvoie que les permissions liées à cet objet spécifique.
        """
        return (
            self.get_user_permissions(obj)
            + self.get_group_permissions(obj)
        )


class Client(models.Model):
    num = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=10)
    addresse = models.CharField(max_length=255)
    code_postal = models.CharField(max_length=5)
    ville = models.CharField(max_length=100)
    date_enregistrement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    
    
class Technicien(models.Model):
    SEXE_CHOICES = (
        ('Monsieur', 'Monsieur'),
        ('Madame', 'Madame'),
        ('Mademoiselle', 'Mademoiselle'),
    )
    
    num = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=10)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=100, choices=SEXE_CHOICES)
    specialite = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    date_enregistrement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom