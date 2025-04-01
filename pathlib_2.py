from os import path
from pathlib import Path

# Especifica la ruta donde quieres crear el archivo
ruta_archivo = Path("/home/penascalf5/Documentos/Python-basico/nuevo_archivo.txt")

# Crear el archivo si no existe
ruta_archivo.touch()

# Verificar si el archivo fue creado
if ruta_archivo.exists():
    print(f"El archivo {ruta_archivo} ha sido creado.")
else:
    print(f"El archivo {ruta_archivo} ya existe.")

# Muestra la ruta actual
print(Path.cwd()) 

# Comprueba si existe el directorio 
print(Path('/home/penascalf5/Documentos/Python-basico').exists())

# es una ruta absoluta?
print(Path('/home/penascalf5/Documentos/Python-basico').is_dir()) 
from pathlib import Path

# Especifica la ruta de tu archivo
ruta_archivo = Path("/home/penascalf5/Documentos/Python-basico/nuevo_archivo.txt")

# Comprobamos si el archivo existe
if ruta_archivo.exists():
    # Obtener el nombre del archivo (incluyendo su extensión)
    print(f"Nombre del archivo: {ruta_archivo.name}")
    
    # Obtener la extensión del archivo
    print(f"Extensión del archivo: {ruta_archivo.suffix}")
    
    # Obtener el tamaño del archivo en bytes
    print(f"Tamaño del archivo: {ruta_archivo.stat().st_size} bytes")
    
    # Obtener la fecha de última modificación del archivo
    print(f"Última modificación: {ruta_archivo.stat().st_mtime}")
    
    # Obtener la ruta completa del archivo
    print(f"Ruta completa: {ruta_archivo.resolve()}")
    
    # Obtener el directorio donde se encuentra el archivo
    print(f"Directorio del archivo: {ruta_archivo.parent}")
    
else:
    print(f"El archivo {ruta_archivo} no existe.")
