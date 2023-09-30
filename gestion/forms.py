from django import forms
from gestion.models import Mail, Satisfaction


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = '__all__'
        
        
    def __init__(self, *args, **kwargs):
        super(MailForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs['placeholder'] = 'Entrez votre nom'
        self.fields['prenom'].widget.attrs['placeholder'] = 'Entrez votre prenom'
        self.fields['sexe'].widget.attrs['placeholder'] = 'Entrez votre sexe'
        self.fields['email'].widget.attrs['placeholder'] = 'Entrez votre email'
        self.fields['telephone'].widget.attrs['placeholder'] = 'Entrez votre numéro telephone'
        self.fields['addresse'].widget.attrs['placeholder'] = 'Entrez votre addresse'
        self.fields['code_postal'].widget.attrs['placeholder'] = 'Entrez votre code postal'
        self.fields['ville'].widget.attrs['placeholder'] = 'Entrez votre ville'
        self.fields['subject'].widget.attrs['placeholder'] = 'Entrez le sujet'
        self.fields['message'].widget.attrs['placeholder'] = 'Entrez votre message'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
            
class SatisfactionForm(forms.ModelForm):
    class Meta:
        model = Satisfaction
        fields = '__all__'
        
        
    def __init__(self, *args, **kwargs):
        super(SatisfactionForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs['placeholder'] = 'Entrez votre nom'
        self.fields['email'].widget.attrs['placeholder'] = 'Entrez votre email'
        # self.fields['qualite'].widget.attrs['placeholder'] = 'Entrez votre note'
        # self.fields['competence'].widget.attrs['placeholder'] = 'Entrez votre note'
        # self.fields['temps_reponse'].widget.attrs['placeholder'] = 'Entrez votre note'
        # self.fields['resolution'].widget.attrs['placeholder'] = 'Entrez votre note'
        # self.fields['recommandation'].widget.attrs['placeholder'] = 'Entrez votre note'
        self.fields['commentaire'].widget.attrs['placeholder'] = 'Entrez votre commentaire ou suggestion'
        for field in self.fields:
            if field != 'recommandation':
                self.fields[field].widget.attrs['class'] = 'form-control'
        