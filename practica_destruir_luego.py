

class perro():

    def __init__(self,nombre = 'duque',edad = 100 ):
        self.nombre =nombre
        self.edad = edad


    def ladrar(self):
        print('guau guau')

    def correr(self):
        print('runnn runn')




mi_dog = perro('simon',200)

mi_dog.correr()
mi_dog.ladrar()