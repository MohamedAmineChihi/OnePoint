class Avion:
    plane_sizes = {
        "Jumbo": (10,60),
        "Jumbo_2": (9, 70),
        "Mid-Size": (7,40),
        "Mid-Size_2": (7, 50),
        "Light": (6,30),
        "Light_2": (6, 40)
    }

    def __init__(self,Nom: str, taille: str):
        print( "Voila les avions disponibles et leurs dispositions Jumbo: (10,60), Jumbo_2: (9, 70), Mid-Size: (7,40), Mid-Size_2: (7, 50), Light: (6,30) ou Light_2: (6, 40)")
        assert taille in Avion.plane_sizes, "La taille doit être Jumbo, Jumbo_2, Mid-Size, Mid-Size_2, Light ou Light_2"
        self.taille = taille
        self.Nom = Nom
        self.disposition = Avion.plane_sizes[taille]
        self.places = []
        self.__init_places()

    def __init_places(self):
        """
        initialise les places de l'avion avec des valeurs None.
        """
        for i in range(self.disposition[0]):
            row = []
            for j in range(self.disposition[1]):
                row.append(None)
            self.places.append(row)

    def est_place_disponible(self, rangee: int, colonne: int) -> bool:
        """
        Vérifie si une place est disponible à une certaine rangée et colonne.
        """
        return self.places[rangee][colonne] is None

    def attribuer_place(self, rangee: int, colonne: int, passager) -> None:
        """
        Attribue une place à un passager à une certaine rangée et colonne.
        Si la place est déjà occupée, une exception ValueError est levée.
        """
        if not self.est_place_disponible(rangee, colonne):
            raise ValueError('La place est déjà occupée')
        self.places[rangee][colonne] = passager

    def liberer_place(self, rangee: int, colonne: int) -> None:
        """
        Libère une place à une certaine rangée et colonne.
        """
        self.places[rangee][colonne] = None

    def modifier_place(self, ancienne_rangee: int, ancienne_colonne: int, nouvelle_rangee: int, nouvelle_colonne: int) -> None:
        """
        Modifie la place d'un passager d'une certaine rangée et colonne vers une nouvelle rangée et colonne.
        """
        passager = self.places[ancienne_rangee][ancienne_colonne]
        self.liberer_place(ancienne_rangee, ancienne_colonne)
        self.attribuer_place(nouvelle_rangee, nouvelle_colonne, passager)

# Créer un avion
avion1 = Avion("Boeing747","Jumbo_2")

# Attribuer la place (2,1) à un passager
avion1.attribuer_place(2, 1, "Passager 1")

# Vérifier si la place (2,1) est disponible
disponible = avion1.est_place_disponible(2, 1)
print(disponible)  # False

# Libérer la place (2,1)
avion1.liberer_place(2, 1)

# Modifier la place du passager de la rangée 1 et colonne 0 à la rangée 3 et colonne 1
avion1.modifier_place(1, 0, 3, 1)