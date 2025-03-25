import random
question = str(input('Haz una pregunta de si o no:'))
num = random.randint(0, 8)
question = num
if question == 0:
  print('Si, por supuesto.')
elif question == 1:
  print('Habria que sopesarlo.')
elif question == 2:
  print('Sin ninguna duda.')
elif question == 3:
  print('Estoy confundido, intentalo de nuevo')
elif question == 4:
  print('Pregunta mas tarde.')
elif question == 5:
  print('Mejor no te lo digo ahora.')
elif question == 6:
  print('Mis entrañas me dicen que no.')
elif question == 7:
  print('No se ve bien, no.')
else:
  print('Lo dudo mucho.')
