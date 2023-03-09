from avion import Avion
from passager import Passager

class Reservation:
    def __init__(self, avion: Avion):
        """
        Initialise une nouvelle réservation pour un avion donné.

        """
        self.avion = avion
        # un dictionnaire contenant les passagers et leur place attribuée
        self.passagers = {}

    def ajouter_passager(self, nom: str, prenom: str, rangee: int, colonne: int) -> None:
        """
        Ajoute un nouveau passager à la réservation.
        Args: nom (str): le nom du passager.

        """
        # vérifie si la place est disponible
        assert self.avion.est_place_disponible(rangee, colonne), "La place est déjà occupée"
        # crée un nouvel objet Passager
        passager = Passager(nom, prenom)
        # attribue la place au passager
        self.avion.attribuer_place(rangee, colonne, passager)
        # ajoute le passager et sa place attribuée au dictionnaire des passagers
        self.passagers[passager] = (rangee, colonne)

    def modifier_place(self, passager: Passager, nouvelle_rangee: int, nouvelle_colonne: int) -> None:
        """
        Modifie la place d'un passager dans la réservation.
        """
        # vérifie si le passager est présent dans la réservation
        assert passager in self.passagers, "Le passager n'est pas dans la réservation"
        # récupère l'ancienne place du passager
        ancienne_rangee, ancienne_colonne = self.passagers[passager]
        # modifie la place de l'avion pour le passager
        self.avion.modifier_place(ancienne_rangee, ancienne_colonne, nouvelle_rangee, nouvelle_colonne)
        # met à jour la nouvelle place du passager dans le dictionnaire des passagers
        self.passagers[passager] = (nouvelle_rangee, nouvelle_colonne)

    def supprimer_passager(self, passager: Passager) -> None:
        """
                Supprime un passager de la réservation
        """
        # vérifie si le passager est présent dans la réservation
        assert passager in self.passagers, "Le passager n'est pas dans la réservation"
        # récupère la place du passager
        rangee, colonne = self.passagers[passager]
       # libère la place de l'avion pour le passager
        self.avion.liberer_place(rangee, colonne)
        # supprime le passager et sa place attribuée du dictionnaire des passagers
        del self.passagers[passager]

    def imprimer_details_reservation(self, *passagers):
        """
            donne les détails de la reservation d' un passager.

        """
        # pour chaque passager donné en argument
        for passager in passagers:
            # vérifie si le passager est présent dans la réservation
            assert passager in self.passagers, "Le passager n'est pas dans la réservation"
            # récupère la place du passager
            rangee, colonne = self.passagers[passager]
            # imprime les détails du passager et de sa place attribuée
            print(f'{passager.nom} {passager.prenom}: Vol {self.avion.vol},  Siège ({rangee},{colonne})')
