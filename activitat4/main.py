from Cotxe import Cotxe
from Colibri import Colibri

#Instancias de cotxe
cotxe1 = Cotxe("Renault1","Renault", "4","5","Motor1")
cotxe2 = Cotxe("Nissan1","Nissan", "4","5","Motor2")
cotxe3 = Cotxe("Porsche1","Porsche", "4","2","Motor3")

#Instancias de colibri
colibri1 = Colibri("Ian",20,15,4,"blau")
colibri2 = Colibri("Chali",10,2,5,"multicolor")
colibri3 = Colibri("Izan",6,5,2,"blau")

#getters de Cotxe
print("Marca Cotxe:",cotxe1.getMarca())
print("Model Cotxe:",cotxe1.getModel())
print("Motor Cotxe:",cotxe1.getMotor())

#getters de Colibri
print("Nom Colibri:",colibri1.getNom())
print("Edat Colibri:",colibri1.getEdat())
print("Color Colibri:",colibri1.getColor())

#Setters de Cotxe
cotxe1.setModel("RenaultGrand")
cotxe1.setMotor("Motor Grand")

#Getters de Cotxe dels atributs modificats
print("Model Cotxe despres de canviar:",cotxe1.getModel())
print("Motor Cotxe despres de canviar:",cotxe1.getMotor())

#Setters de Colibri
colibri1.setNom("Imad")
colibri1.setEdat("3")

#Getters de Colibri dels atributs modificats
print("Nom Colibri despres de canviar:",colibri1.getNom())
print("Edat Colibri despres de canviar:",colibri1.getEdat())




