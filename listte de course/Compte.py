class GestionCptB:
    def __init(self,numcompte,nom,solde):
        self.nCompte=numcompte
        self.nomClient=nom
        self.soldeCompte=solde
    
    def versement(self,somme_verse):
        self.soldeCompte=self.soldeCompte+somme_verse
        return self.soldeCompte

    def retrait(self,somme_retrait):
        if self.soldeCompte>somme_retrait:
            self.soldeCompte=self.soldeCompte-somme_retrait
            return self.soldeCompte
        else:
            print("le solde actuel de votre compte est insufisant")

    def affichageinfo(self):
        print("Le numéro du compte est",self.numcompte)     
        print("Le nom du client est",self.nomClient)
        print("Le solde du compte est",self.soldeCompte)                  

#test de la classe
cptb1=GestionCptB(1231231,"sara croche",500000)
cptb1.versement(33000)
cptb1.affichageinfo()