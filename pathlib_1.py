from pathlib import Path, PosixPath, WindowsPath

# Declarar rutas concretas

ruta1 = Path('home/usuario')
ruta2 = Path('c:\\windows')
ruta3 = PosixPath('home/Usuario')
ruta4 = WindowsPath('C:\\WINDOWS')  # Error en Linux

# Imprimir las rutas

print(ruta1)  # home/usuario
print(ruta2)  # c:\windows
print(ruta3)  # home/Usuario
print(ruta4)  # C:\WINDOWS

# Las rutas son cadenas de un tipo especial ...

print(type(ruta1))  # 
print(type(ruta2))  # 
print(type(ruta3))  # 
print(type(ruta4))  # 

# Obtener ruta del directorio actual de trabajo

print(Path.cwd())  # /home/usuario/Directorio

# Obtener la ruta del directorio de usuario actual

print(Path.home())  # /home/usuario

# Obtener información del directio o del archivo

# Obtener tamaño en bytes

print(Path('/etc/os-release').stat().st_size)  # 386

# Obtener tiempo de modificación (expresado en segundos)

print(Path('/etc/os-release').stat().st_mtime)  # 1534722298.0

# Para enlaces simbólicos: lstat()

# Cambiar los atributos y/o permisos del directorio o del archivo

Path('/home/usu1/imagen1.png').chmod(0o666)

# Para enlaces simbólicos: lchmod()

# Comprobar si existe el archivo o directorio

print(Path('/etc/os-release').exists())  # True

# Expandir la ruta añadiendo la ruta 'home' del usuario actual

print(Path('~/bashrc').expanduser())  # /home/usuario/bashrc

# Obtener de la ruta una lista con los archivos del patrón

archivos = Path('/home/usu1/Descargas').glob('*.pdf')
for archivo in archivos:
    print(archivo)

# Otros patrones:
# '*/*.pdf' Obtener del directorio con 1 nivel de profundidad
# '**/*.pdf' Obtener del directorio actual y sus subdirectorios
# El patrón '**/*.pdf' es equivalente a rglob('*.pdf')

# Obtener nombre del grupo propietario

print(Path('/etc/os-release').group())  # root

# Conocer si una ruta es un directorio o un enlace simbólico
# que apunta a un directorio existente

print(Path('/etc/os-release').is_dir())  # False

# Conocer si una ruta es un fichero o un enlace simbólico
# que apunta a un fichero existente

print(Path('/etc/os-release').is_file())  # True

# Conocer si una ruta es un enlace simbólico

print(Path('/etc/resolv.conf').is_symlink())  # True

# Conocer si la ruta es un punto de montaje.
# No implementado para windows. Nuevo en Python 3.7

print(Path('/media/usuario').is_mount())  # True

# Obtener iterador con objetos contenidos en un directorio

for elemento in Path('/home/usu1/Descargas').iterdir():
    print(elemento)  # Lista ficheros y directorios

# Crear un directorio (si no existe)

Path('/home/u1/bd').mkdir(mode=0o777, parents=False, exist_ok=True)

# Si parents=True creará los directorios padres que falten 
# en el camino
# Si exist_ok=True y el directorio a crear existe se 
# omitirá mensaje de error

# Abrir un archivo para leer y/o escribir

with Path('/etc/os-release').open(mode='r') as archivo:
    for linea in archivo:
        print(linea.strip())

# Leer y escribir de/en un archivo de texto

archivo = Path('secreto.txt')
archivo.write_text('Este archivo guarda un gran secreto')
print(archivo.read_text())

# Leer y escribir de/en un archivo en formato binario

archivo = Path('secreto.dat')
archivo.write_bytes(b'Este archivo guarda un gran secreto')
print(archivo.read_bytes())

# Conocer el propietario de un archivo

print(Path('/etc/resolv.conf').owner())  # root

# Renombrar un archivo o un directorio

Path('/home/usu1/imagen1.png').rename('/home/usu1/imagen2.png')

# En Unix si se trata de un archivo existeste será reemplazado.

# Renombrar un archivo o un directorio.

Path('/home/usu1/imagen2.png').replace('/home/usu1/imagen1.png')

# Si existe archivo o directorio será reemplezado

# Convertir una ruta en absoluta

print(Path('/etc/resolv.conf').resolve())  
# /run/resolvconf/resolv.conf

print(Path('..').resolve())  # /home/usuario/Local

# Borrar un directorio vacío

dir1 = Path('/home/usu1/temp-1')
if dir1.exists():
    dir1.rmdir()

# Conocer si hay coincidencia en dos rutas

documentos = '/home/usu1/.bashrc'
print(Path('/home/usu1/.bashrc').samefile(documentos))  # True

# Crear un enlace simbólico

Path('MiEnlace').symlink_to('imagen.png')

# Borrar un archivo o un enlace simbólico

Path('imagen.png').unlink() # type: ignore