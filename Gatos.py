class gato:
    def __init__(self,nombre,nombre_dueño,direccion,raza,color,color_ojos,vacunas):
        self.nombre = nombre
        self.nombre_dueño = nombre_dueño
        self.direccion = direccion 
        self.raza = raza
        self.color = color
        self.color_ojos = color_ojos
        self.vacunas = vacunas
    def mostrar_info(self):
        print("Nombre gato: " + self.nombre)
        print("Nombre del dueño: " + self.nombre_dueño)
        print("Direccion: " + self.direccion)
        print("Raza: " + self.raza)
        print("Color: " + self.color)
         
        print("Color.ojos: " + self.color_ojos)
        print("¿Cuenta con vacunas? " + self.vacunas)
         
nombre = input("Ingrese el nombre del felino: ")
nombre_dueño = input("Ingrese el nombre del dueño: ")
direccion = input("Ingrese el domicilio: ")
raza = input("Ingrese la raza: ")
color = input("Ingrese el color de pelo: ")
color_ojos = input("Ingrese el color de ojos: ")
vacunas = input("Ingrese si el felino cuenta con vacunas: ")   

gatito = gato(nombre,nombre_dueño,direccion,raza,color,color_ojos,vacunas)
gatito.mostrar_info()
        

        
        