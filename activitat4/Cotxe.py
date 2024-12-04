class Cotxe:
    #Constructor
    def __init__(self, marca, model, num_rodes, portes, motor) :
        self.marca = marca
        self.model = model
        self.num_rodes = num_rodes
        self.portes = portes
        self.motor = motor
    
    #Getters i Setters
    
    def getMarca(self):
        return self.marca
    def setMarca(self, nueva_marca):
        self.marca = nueva_marca

    def getModel(self):
        return self.model
    def setModel(self,nuevo_model):
        self.model = nuevo_model

    def getNumRodes(self):
        return self.num_rodes
    def setNumRodes(self, nuevo_numRodes):
        self.num_rodes = nuevo_numRodes
    
    def getPortes(self):
        return self.portes
    def setPortes(self, nueva_portes):
        self.portes = nueva_portes

    def getMotor(self):
        return self.motor
    def setMotor(self, nuevo_motor):
        self.motor = nuevo_motor


