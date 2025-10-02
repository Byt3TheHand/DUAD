import csv
headers=['Nombre','Genero','Desarrollador','Clasificacion ESBR']
data=[
{'Nombre':'Grand Theft Auto','Genero':'Accion','Desarrollador':'RockStar Games','Clasificacion ESBR':'M'},
{'Nombre':'The Elder Scrolls IV: Oblivion','Genero':'RPG','Desarrollador':'Bethesda','Clasificacion ESBR':'M'},
{'Nombre':'Tony Hawk\'s Pro Skater 2','Genero':'Deportes','Desarrollador':'Activision','Clasificacion ESBR':'T'}
]

with open ('videogames.csv', newline='',mode='w',encoding='utf-8') as file:
    writer=csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)


while True:
    name= input('Ingrese el nombre del juego: ')
    genre= input ('Ingrese el genero del juego: ')
    developer= input('Ingrese el desarrollador del juego: ')
    rating= input('Ingrese la clasificacion del juego: ')

    game_list = {
        'Nombre' : name,
        'Genero' : genre,
        'Desarrollador' : developer,
        'Clasificacion ESBR': rating
    }

    with open('videogames.csv', newline='', mode='a', encoding='utf-8') as file:
        new_game_csv= csv.DictWriter (file, fieldnames=headers)
        new_game_csv.writerow(game_list)

    add_another_game = input(' Desea agragar un juego nuevo? (s/n): ')
    if add_another_game !='s':
        break