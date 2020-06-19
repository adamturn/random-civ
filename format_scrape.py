# sloc!!!
# standard library
import random


def main():

    data = [
        ('Alexander', 'Macedonian'), 
        ('Amanitore', 'Nubian'), 
        ('Chandragupta', 'Indian'), 
        ('Cleopatra', 'Egyptian'), 
        ('Cyrus', 'Persian'), 
        ('Dido', 'Phoenician'), 
        ('Gandhi', 'Indian'), 
        ('Gilgamesh', 'Sumerian'), 
        ('Gitarja', 'Indonesian'), 
        ('Jadwiga', 'Polish'), 
        ('Kristina', 'Swedish'), 
        ('Kupe', 'Maori'),
        ('Lautaro', 'Mapuche'), 
        ('Montezuma', 'Aztec'), 
        ('Pachacuti', 'Incan'), 
        ('Pericles', 'Greek'), 
        ('Peter', 'Russian'), 
        ('Poundmaker', 'Cree'), 
        ('Saladin', 'Arabian'), 
        ('Seondeok', 'Korean'), 
        ('Shaka', 'Zulu'), 
        ('Suleiman', 'Ottoman'), 
        ('Tamar', 'Georgian'), 
        ('Tomyris', 'Scythian'), 
        ('Trajan', 'Roman'), 
        ('Victoria', 'English'), 
        ('Wilhelmina', 'Dutch'), 
        ('Gorgo', 'Greek'), 
        ('Harald Hardrada', 'Norwegian'), 
        ('Hojo Tokimune', 'Japanese'), 
        ('Genghis Khan', 'Mongolian'), 
        ('Frederick Barbarossa', 'German'), 
        ('Jayavarman VII', 'Khmer'), 
        ('John Curtin', 'Australian'), 
        ('Mansa Musa', 'Mali'), 
        ('Matthias Corvinus', 'Hungarian'), 
        ('Pedro II', 'Brazilian'), 
        ('Philip II', 'Spanish'), 
        ('Simon Bolivar', 'Gran Colombia'), 
        ('Teddy Roosevelt', 'American'), 
        ('Wilfrid Laurier', 'Canadian'), 
        ('Qin Shi Huang', 'Chinese'), 
        ('Robert the Bruce', 'Scottish'), 
        ('Mvemba a Nzinga', 'Kongolese'), 
        ('Lady Six Sky', 'Mayan'), 
        ('Catherine de Medici', 'French'), 
        ('Eleanor of Aquitaine', 'English'), 
        ('Eleanor of Aquitaine', 'French'), 
    ]
    print("[civbot] Welcome! I will randomly select 'n' civs.")
    gate = True
    while gate:
        n = input("[user] n = ")
        for _ in range(int(n)):
            civ = random.choice(data)
            print(f"{civ[0]} ({civ[1]})")
        cont = input("Continue? [y]/n: ")
        breakpoint()
        if cont == 'n' or 'q':
            break

    return None


if __name__ == "__main__":
    main()
