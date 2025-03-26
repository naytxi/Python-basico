#MAP
print('MAP')
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  

#FILTER
print('FILTER')
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares) 

#REDUCE
print('REDUCE')
from functools import reduce

numeros = [1, 2, 3]
resultado = reduce(lambda x, y: x + y, numeros)
print(resultado)

#ENUMERATE
print('ENUMERATE')
frutas = ["pera", "fresa", "naranja"]
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

#ZIP
print('ZIP')
nombres = ["Nay", "Gaizka", "Thais"]
edades = [25, 30, 22]

combinado = list(zip(nombres, edades))
print(combinado)

#*ARGS
print('*ARGS')
def sumar(*numeros):
    return sum(numeros)  

print(sumar(3, 5, 7))  
print(sumar(10, 20))   
print(sumar(1, 2, 3, 4, 5))  

#**KWARGS
print('**KWARGS')
def mostrar_info(**informacion):
    print(informacion["nombre"])  
    print(informacion["edad"])    
    print(informacion["ciudad"])  

mostrar_info(nombre="Nay", edad=24, ciudad="Disney")

#LIST COMPREHESION
print('LIST COMPREHESION')
pares = [x for x in range(10) if x % 2 == 0]  
print(pares)

original = [1, 2, 3, 4, 5]
nueva_lista = [numero for numero in original]  

print(nueva_lista)
