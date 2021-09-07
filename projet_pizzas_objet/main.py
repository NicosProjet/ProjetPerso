

class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def Afficher(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = " - VEGETARIENNE "
        print(f"PIZZA {self.nom} : {self.prix}euros" + veg_str)
        print(", ".join(self.ingredients))
        print()

class PizzaPersonnalisee(Pizza):

    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENTS = 1.2
    dernier_numero = 0

    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.numero = PizzaPersonnalisee.dernier_numero
        super().__init__("Personnalisée" + str(self.numero), 0, [])
        self.demander_ingredients_utilisateur()
        self.calculer_le_prix()

    def demander_ingredients_utilisateur(self):
        # "Ingredients pour la pizza personalisée" (n)
        print(f"Ingrédients pour la pizza personnalisée {self.numero}")
        while True:
            ingredients = input("Ajoutez un ingrédients (ou ENTER pour terminer): ")
            if ingredients == "":
                return
            self.ingredients.append(ingredients)
            print(f"Vous avez {len(self.ingredients)} ingredients(s) : {', '.join(self.ingredients)}")

    def calculer_le_prix(self):

        self.prix = self.PRIX_DE_BASE + len(self.ingredients)*self.PRIX_PAR_INGREDIENTS

# Tuple de plusieurs pizzas contenant le nom le prix et une liste d'ingrédients
pizzas = (
    Pizza("Hawai", 7.50, ("tomate", "ananas", "oignons"),True),
    Pizza("4 fromages", 8.90, ("brie", "emmental", "compté", "parmesan")),
    Pizza("4 saisons", 12.50, ("oeuf", "emmental", "tomate", "jambon")),
    Pizza("Végétatienne", 11.50, ("champignons", "tomate", "oignons", "poivrons"), True,),
    PizzaPersonnalisee(),
    PizzaPersonnalisee()

)

for i in pizzas:
    i.Afficher()

# (Exo) Boucle afficher :
#(1) Que les pizzas vegetatiennes
#       for i in pizzas:
#           if i.vegetarienne:
#              i.Afficher()

#(2) Que les pizzas non-vegetariennes
#       for i in pizzas:
#           if not i.vegetarienne:
#               i.Afficher()

#(3) Que les pizzas qui ont de la tomate

# for i in pizzas:
#     if "tomate" in i.ingredients:
#         i.Afficher()

#(4) Que les pizzas à moins de 10 euros
# for i in pizzas:
#     if i.prix < 10:
#         i.Afficher()
