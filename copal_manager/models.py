from django.db import models

# Create your models here.
class Proprietaire(models.Model):

    # Affichage Proprietaire
    def __str__(self):
        return self.nom + ", " + self.prenom

    # Attributs:
    CHOICES = [('M', 'Monsieur'),('Mme', 'Madame'), ('M&Mme', 'Monsieur et Madame'), ('Societe', 'Societe')]
    civilite = models.CharField(max_length=20, choices=CHOICES, default="M")
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    adresse = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=50)
    siret = models.CharField(max_length=30, blank=True)

class BienImmobilier(models.Model):

    # Affichage BienImmobilier:
    def __str__(self):
        return self.nom + "(" + str(self.proprietaire) + ")"


    # Attributs:
    nom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=50)
    surface = models.DecimalField(max_digits=10, decimal_places=2)
    type_bien = models.CharField(max_length=50)
    nb_pieces = models.IntegerField(default=0)   
    nb_chambres = models.IntegerField(default=0)   
    nb_sdb = models.IntegerField(default=0)     
    etage = models.IntegerField(default=0)   
    commentaire = models.CharField(max_length=150, blank=True)

    # Foreign Keys:
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)


class Contrat(models.Model):

    # Affichage Contrat:
    def __str__(self):
        return self.numero_contrat + ": " + str(self.proprietaire)

    numero_contrat = models.CharField(max_length=10, default="0")
    date_debut = models.DateField()
    date_fin = models.DateField(null = True, blank = True)
    frais_gestion = models.DecimalField(max_digits=10, decimal_places=2)
    frais_mer = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Foreign Keys:
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    bien_immo = models.ForeignKey(BienImmobilier, on_delete=models.DO_NOTHING)
   

class Facture(models.Model):
    
    # Attributs:
    date = models.DateField() 
    montant_ht = models.DecimalField(max_digits=10, decimal_places=2) 
    tva = models.DecimalField(max_digits=10, decimal_places=2)
    montant_ttc = models.DecimalField(max_digits=10, decimal_places=2)      

    # Foreign Keys:                    
    contrat = models.ForeignKey(Contrat, on_delete=models.DO_NOTHING) 


class Prestation(models.Model):
    
    # Attributs:
    qte = models.DecimalField(max_digits=10, decimal_places=2) 
    type_presta = models.CharField(max_length=10)
    prix_ht = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=10, decimal_places=2)
    prix_ttc = models.DecimalField(max_digits=10, decimal_places=2)

    # Foreign Keys:
    id_facture = models.ForeignKey(Facture, on_delete=models.DO_NOTHING)                                                                                                                       

