class Persona:
    def __init__(self,nombre,apellidos,sexo,edad,altura,color_ojos,color_cabello):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.altura = altura
        self.color_ojos = color_ojos
        self.color_cabello = color_cabello
        
    def mostrar_info(self):
        print("Nombre: "+self.nombre)
        print("Apellidos: "+self.apellidos)
        print("Género: "+self.sexo)
        print("Edad: "+self.edad)
        print("Altura: "+self.altura)
        print(self.color_ojos)
        print(self.color_cabello)
        
    def calcular_edad(self):
        edad = int(self.edad)
        edad = edad + 10
        print(" En diez años la persona " + self.nombre + " tendra " + str(edad))

nombre = input("Ingrese Nombre aqui: ")
apellidos = input("Ingrese apellido aqui: ")
genero = input("Ingrese el genero aqui: ")
edad = input("Ingrese la edad aqui: ")
altura = input("Ingrese la altura aqui ")
color_ojos = input("Ingrese color de ojos:")
color_cabello = input("Ingrese color de cabello")
     
pepito = Persona(nombre, apellidos, genero, edad, altura,color_ojos,color_cabello)
pepito.calcular_edad()
pepito.mostrar_info() 
    
