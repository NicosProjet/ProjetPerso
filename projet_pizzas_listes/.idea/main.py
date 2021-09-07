
listePizzas = ["4 fromages", "carbo", "hawai", "rougail"]


def afficherPizza(collection):
    print(f'|---------- Liste des pizzas({len(listePizzas)})--------|')

        # affiche la liste des pizzas
    for i in collection:
        print(i)
    print('')

        # affiche la première et dernière pizza du tableau
    print(f"Première pizza {collection[0]}")
    print(f"Dernière pizza {collection[-1]}")


def ajouter_pizza_utilisateur(collection):

        # Lorsque l'utilisateur rentre le nom d'une pizza:
    newPizzas = input("Pizza à ajouter: ")
        #vérifie si la pizza existe
    if newPizzas in collection:
        print(f"La pizza {newPizzas} existe déjà")
    else:
        #l'ajoute dans la liste
        collection.append(newPizzas)



a = 0
while a == 0:
    ajouter_pizza_utilisateur(listePizzas)
    afficherPizza(listePizzas)
