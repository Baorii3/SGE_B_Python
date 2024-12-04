class Colibri:
    #Constructor
    def __init__(self, nom, tamany, pes, edat, color) :
        self.nom = nom
        self.tamany = tamany
        self.pes = pes
        self.edat = edat
        self.color = color
    
    #Getters i Setters
    
    def getNom(self):
        return self.nom
    def setNom(self, nuevo_nom):
        self.nom = nuevo_nom

    def getTamany(self):
        return self.tamany
    def setTamany(self,nuevo_tamany):
        self.tamany = nuevo_tamany

    def getPes(self):
        return self.pes
    def setPes(self, nuevo_pes):
        self.pes = nuevo_pes
    
    def getEdat(self):
        return self.edat
    def setEdat(self, nueva_edat):
        self.edat = nueva_edat

    def getColor(self):
        return self.color
    def setColor(self, nuevo_color):
        self.color = nuevo_color