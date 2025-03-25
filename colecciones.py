import json
import time

def pausa():
    input("\n🔹 Pulsa ENTER para continuar...\n")

def titulo(texto):
    print(f"\n{'=' * 50}\n🧩 {texto}\n{'=' * 50}")

def explicacion(texto):
    print(f"\n📘 {texto}")
    time.sleep(1.5)

# LISTAS

def listas():
    titulo("LISTAS")
    explicacion("Una lista es una colección ordenada y modificable. Se define con corchetes [].")
    frutas = ["manzana", "naranja", "plátano"]
    print(f"\nLista actual: {frutas}")
    explicacion("Puedes acceder a un elemento con su índice, empezando en 0:")
    print(f"frutas[0] = {frutas[0]}")
    
    nueva = input("🍓 Escribe una fruta para añadir a la lista: ")
    frutas.append(nueva)
    print(f"Lista después de añadir '{nueva}': {frutas}")
    
    borrar = input("❌ Escribe una fruta que quieras eliminar: ")
    if borrar in frutas:
        frutas.remove(borrar)
        print(f"Lista después de eliminar '{borrar}': {frutas}")
    else:
        print(f"'{borrar}' no estaba en la lista.")

    pausa()

# TUPLAS

def tuplas():
    titulo("TUPLAS")
    explicacion("Una tupla es como una lista, pero inmutable. Se define con paréntesis ().")
    colores = ("rojo", "verde", "azul")
    print(f"Tupla original: {colores}")
    explicacion("No puedes modificar una tupla directamente, pero puedes convertirla en lista.")
    
    colores_lista = list(colores)
    nuevo = input("🎨 Añade un color: ")
    colores_lista.append(nuevo)
    colores = tuple(colores_lista)
    print(f"Tupla final tras la conversión: {colores}")
    
    pausa()
    
# DICCIONARIOS   

def diccionarios():
    titulo("DICCIONARIOS")
    explicacion("Los diccionarios almacenan pares clave:valor. Se definen con llaves {}.")
    persona = {"nombre": "Lucía", "edad": 25}
    print(f"Diccionario: {persona}")
    
    clave = input("🗝️ Añade una nueva clave (ej: 'profesión'): ")
    valor = input(f"📌 Valor para '{clave}': ")
    persona[clave] = valor
    print(f"Diccionario actualizado: {persona}")
    
    eliminar = input("❌ ¿Qué clave quieres eliminar?: ")
    if eliminar in persona:
        del persona[eliminar]
        print(f"Diccionario tras borrar '{eliminar}': {persona}")
    else:
        print(f"'{eliminar}' no se encontró.")

    pausa()
    
# SETS

def sets():
    titulo("SETS (conjuntos)")
    explicacion("Un set es una colección desordenada, sin duplicados. Se define con llaves o con set().")
    colores = {"rojo", "azul", "verde"}
    print(f"Set actual: {colores}")
    
    nuevo = input("➕ Añade un color: ")
    colores.add(nuevo)
    print(f"Set tras añadir: {colores}")
    
    borrar = input("❌ ¿Qué color quieres quitar?: ")
    colores.discard(borrar)
    print(f"Set tras eliminar '{borrar}': {colores}")
    
    pausa()

def conversiones():
    titulo("CONVERSIONES ENTRE ITERABLES")
    explicacion("Convertir entre lista, tupla y set es fácil con funciones: list(), tuple(), set()")
    lista = ["a", "b", "c", "c"]
    print(f"Lista original: {lista}")
    
    tupla = tuple(lista)
    print(f"Convertida a tupla: {tupla}")
    
    conjunto = set(lista)
    print(f"Convertida a set (elimina duplicados): {conjunto}")
    
    nueva_lista = list(conjunto)
    print(f"Set convertido a lista: {nueva_lista}")
    
    pausa()
    
# CONVERSION JSON

def json_conversion():
    titulo("JSON ↔️ DICCIONARIO")
    explicacion("JSON es un formato de texto muy usado para intercambiar datos. En Python usamos json.dumps() y json.loads().")
    
    diccionario = {
        "animal": "gato",
        "edad": 3
    }
    print(f"Diccionario original: {diccionario}")
    
    json_string = json.dumps(diccionario)
    print(f"📤 Convertido a JSON (string): {json_string}")
    
    nuevo_dic = json.loads(json_string)
    print(f"📥 Convertido de JSON a diccionario: {nuevo_dic}")
    
    pausa()

# METODOS DE COLECCIONES

# LISTAS

def mostrar_lista():
    titulo("MÉTODOS DE LISTAS")
    lista = [1, 2, 3]
    print("Lista inicial:", lista)
    lista.append(4)
    print("append(4):", lista)
    lista.insert(1, 99)
    print("insert(1, 99):", lista)
    lista.extend([5, 6])
    print("extend([5, 6]):", lista)
    lista.remove(99)
    print("remove(99):", lista)
    lista.pop()
    print("pop():", lista)
    lista.sort()
    print("sort():", lista)
    lista.reverse()
    print("reverse():", lista)
    print("count(2):", lista.count(2))
    print("index(1):", lista.index(1))
    pausa()
    
# TUPLAS

def mostrar_tupla():
    titulo("MÉTODOS DE TUPLAS")
    tupla = (1, 2, 3, 2)
    print("Tupla:", tupla)
    print("count(2):", tupla.count(2))
    print("index(3):", tupla.index(3))
    print("Las tuplas son inmutables, no se pueden modificar.")
    pausa()

# DICCIONARIOS

def mostrar_diccionario():
    titulo("MÉTODOS DE DICCIONARIOS")
    persona = {"nombre": "Ana", "edad": 30}
    print("Diccionario inicial:", persona)
    print("get('nombre'):", persona.get("nombre"))
    persona["altura"] = 1.70
    print("persona['altura'] = 1.70 ->", persona)
    persona.update({"edad": 31})
    print("update({'edad': 31}) ->", persona)
    persona.pop("nombre")
    print("pop('nombre') ->", persona)
    print("keys():", list(persona.keys()))
    print("values():", list(persona.values()))
    print("items():", list(persona.items()))
    persona.clear()
    print("clear() ->", persona)
    pausa()

# SETS

def mostrar_set():
    titulo("MÉTODOS DE SETS")
    mi_set = {1, 2, 3}
    print("Set inicial:", mi_set)
    mi_set.add(4)
    print("add(4):", mi_set)
    mi_set.discard(2)
    print("discard(2):", mi_set)
    mi_set.discard(10)
    print("discard(10) (no lanza error):", mi_set)
    otro_set = {3, 4, 5}
    print("Otro set:", otro_set)
    print("union:", mi_set.union(otro_set))
    print("intersection:", mi_set.intersection(otro_set))
    mi_set.clear()
    print("clear():", mi_set)
    pausa()

# CONVERSIONES

def mostrar_conversiones():
    titulo("CONVERSIONES ENTRE COLECCIONES")
    lista = [1, 2, 2, 3]
    tupla = (4, 5, 6)
    conjunto = {7, 8, 9}
    diccionario = {"a": 1, "b": 2}

    print(f"📋 Lista original: {lista}")
    print("➡ Lista → Tupla:", tuple(lista))
    print("➡ Lista → Set:", set(lista))

    print(f"\n📦 Tupla original: {tupla}")
    print("➡ Tupla → Lista:", list(tupla))
    print("➡ Tupla → Set:", set(tupla))

    print(f"\n🔗 Set original: {conjunto}")
    print("➡ Set → Lista:", list(conjunto))
    print("➡ Set → Tupla:", tuple(conjunto))

    print(f"\n📚 Diccionario original: {diccionario}")
    print("➡ Diccionario → Lista de claves:", list(diccionario))
    print("➡ Diccionario → Lista de valores:", list(diccionario.values()))
    print("➡ Diccionario → Lista de items:", list(diccionario.items()))

    pausa()

def menu_repaso():
    while True:
        print("\n===== MENÚ DE REPASO DE MÉTODOS =====")
        print("1. Listas")
        print("2. Tuplas")
        print("3. Diccionarios")
        print("4. Sets")
        print("5. Conversiones")
        print("6. Salir del repaso")
        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            mostrar_lista()
        elif opcion == "2":
            mostrar_tupla()
        elif opcion == "3":
            mostrar_diccionario()
        elif opcion == "4":
            mostrar_set()
        elif opcion == "5":
            mostrar_conversiones()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# CIERRE 

def despedida():
    print("\n🎉 ¡Enhorabuena! Has completado todos los niveles.")
    print("💡 Ahora dominas las colecciones en Python como un/a pro.")
    print("Vuelve cuando quieras para seguir practicando. 🐍")

# EJECUCIÓN DEL JUEGO 

def juego():
    print("🧠 Bienvenido/a a la AVENTURA DE COLECCIONES EN PYTHON")
    input("Presiona ENTER para comenzar...\n")
    listas()
    tuplas()
    diccionarios()
    sets()
    conversiones()
    json_conversion()
    menu_repaso()
    despedida()

if __name__ == "__main__":
    juego()


# 1. Definir una clase
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

# 2. Crear un objeto de la clase
persona1 = Persona("Juan", 30, "Madrid")

# 3. Acceder a los atributos del objeto
nombre = persona1.nombre
edad = persona1.edad
ciudad = persona1.ciudad


# Lista ↔ tupla
lista = [1, 2, 3, 4]
tupla = tuple(lista)  # Convierte lista en tupla

otra_lista = list(tupla)  # Convierte tupla en lista

# Lista ↔ set
lista = [1, 2, 2, 3, 4, 4]
conjunto = set(lista)  # Convierte lista en set (elimina duplicados)

otra_lista = list(conjunto)  # Convierte set en lista

# Tupla ↔ set
tupla = (5, 6, 6, 7, 8)
conjunto = set(tupla)  # Convierte tupla en set (elimina duplicados)

otra_tupla = tuple(conjunto)  # Convierte set en tupla

# Lista ↔ Diccionario
lista_pares = [("nombre", "Juan"), ("edad", 30)]
diccionario = dict(lista_pares)  # Convierte lista de pares en diccionario

otra_lista = list(diccionario.items())  # Convierte diccionario en lista de tuplas


