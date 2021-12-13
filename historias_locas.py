# concatenar cadenas de caracteres
# Supongamos que queremos crear una cadena que diga el mensaje:
# Aprende a programar con __________________

# organizacion = "platzi"
# print('Aprende a programar con ' + organizacion)
# print('Aprende a programar con {}'.format(organizacion))
# print(f'Aprende a programar con {organizacion}') #f-string

# Mad Libs (Historias Locas)

adj = input('Adjetivo: ')
verbo1 = input('Verbo: ')
verbo2 = input('Verbo2: ')
sustantivo_plural = input('Sistantivo (Plural): ')

madlib = f'Programar es {adj}, siempre me emociona porque me encanta {verbo1} problemas. Aprende a {verbo2} ahora y alcanza tus {sustantivo_plural}!!'

print(madlib)