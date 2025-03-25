#MAP
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  

#FILTER
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares) 

#REDUCE
from functools import reduce

numeros = [1, 2, 3]
resultado = reduce(lambda x, y: x + y, numeros)
print(resultado)

#ENUMERATE
frutas = ["pera", "fresa", "naranja"]
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

#ZIP
nombres = ["Nay", "Gaizka", "Thais"]
edades = [25, 30, 22]

combinado = list(zip(nombres, edades))
print(combinado)

#*ARGS
def sumar(*numeros):
    return sum(numeros)  

print(sumar(3, 5, 7))  
print(sumar(10, 20))   
print(sumar(1, 2, 3, 4, 5))  

#**KWARGS
def mostrar_info(**informacion):
    print(informacion["nombre"])  
    print(informacion["edad"])    
    print(informacion["ciudad"])  

mostrar_info(nombre="Nay", edad=24, ciudad="Disney")