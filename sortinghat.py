
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("\nPrefieres")
print("1) Amanecer")
print("2) Atardecer")
answer = int(input())

if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Elige mejor")

print("\nCuando muera quiero que me recuerden como:")
print("1) EL Bueno")
print("2) El Magnifico")
print("3) El Sabio")
print("4) El Astuto")
answer2 = int(input())

if answer2 == 1:
    gryffindor += 2
elif answer2 == 2:
    ravenclaw += 2
elif answer2 == 3:
    hufflepuff += 2
elif answer2 == 4:
    slytherin += 2
else:
    print("Elige uno vamos")

print("\nQue instrumento prefieres escuchar:")
print("1) Violin")
print("2) Trompeta")
print("3) Piano")
print("4) Bateria")
answer3 = int(input())

if answer3 == 4:
    gryffindor += 2
elif answer3 == 3:
    ravenclaw += 2
elif answer3 == 2:
    hufflepuff += 2
elif answer3 == 1:
    slytherin += 2
else:
    print("Que elijas leñe")

print("\nQue postre eliges: ")
print("1) Helado")
print("2) Cheesecake")
print("3) Las torrijas de mi abuela")
print("4) Soy mas de salado")
answer3 = int(input())

if answer3 == 1:
    gryffindor += 2
elif answer3 == 2:
    ravenclaw += 2
elif answer3 == 3:
    hufflepuff += 2
elif answer3 == 4:
    slytherin += 2
else:
    print("Eligee pesao")

print("\nFinalmente ciudad: ")
print("1) Londres")
print("2) New York")
print("3) Atenas")
print("4) Dubai")
answer3 = int(input())

if answer3 == 2:
    gryffindor += 2
elif answer3 == 3:
    ravenclaw += 2
elif answer3 == 1:
    hufflepuff += 2
elif answer3 == 4:
    slytherin += 2
else:
    print("Venga que solo falta una")

# Determinar la casa con mayor puntuación
print("\n🏰 El Sombrero Seleccionador ha decidido... 🏰")
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print("🦁 ¡GRYFFINDOR! 🔥")
elif ravenclaw >= gryffindor and ravenclaw >= slytherin:
    print("🦅 ¡RAVENCLAW! 📚")
elif hufflepuff >= slytherin:
    print("🦡 ¡HUFFLEPUFF! 🌿")
else:
    print("🐍 ¡SLYTHERIN! 🐍")
