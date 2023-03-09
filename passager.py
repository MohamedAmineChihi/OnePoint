class Passager:
    def __init__(self, nom: str, prenom: str):
        """
        Initialise un objet Passager avec un nom et un prénom.
        """
        assert isinstance(nom, str), "Le nom doit être une chaîne de caractères"
        assert isinstance(prenom, str), "Le prénom doit être une chaîne de caractères"
        self.nom = nom
        self.prenom = prenom

# Instances de Passager
#passager1 = Passager("Dupont", 0)
passager2 = Passager("Martin", "Marie")
print(passager2)