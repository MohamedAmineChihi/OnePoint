from avion import Avion
from reservation import Reservation
from passager import Passager

def afficher_menu():
    print("Que souhaitez-vous faire ?")
    print("1. Afficher les places disponibles")
    print("2. Réserver une place")
    print("3. Modifier une réservation")
    print("4. Annuler une réservation")
    print("5. Afficher les détails d'une réservation")
    print("6. Quitter")

def afficher_places_disponibles(avion):
    for i in range(avion.disposition[0]):
        for j in range(avion.disposition[1]):
            if avion.est_place_disponible(i, j):
                print(f"Rangée {i}, Siège {j} : Disponible")
            else:
                print(f"Rangée {i}, Siège {j} : Occupé")

def reserver_place(reservation):
    nom = input("Nom du passager : ")
    prenom = input("Prénom du passager : ")
    rangee = int(input("Numéro de rangée : "))
    colonne = int(input("Numéro de siège : "))
    try:
        reservation.ajouter_passager(nom, prenom, rangee, colonne)
        print("La place a été réservée avec succès.")
    except ValueError as e:
        print(str(e))

def modifier_reservation(reservation):
    nom = input("Nom du passager : ")
    prenom = input("Prénom du passager : ")
    rangee = int(input("Nouveau numéro de rangée : "))
    colonne = int(input("Nouveau numéro de siège : "))
    passager = Passager(nom, prenom)
    try:
        reservation.modifier_place(passager, rangee, colonne)
        print("La réservation a été modifiée avec succès.")
    except ValueError as e:
        print(str(e))

def annuler_reservation(reservation):
    nom = input("Nom du passager : ")
    prenom = input("Prénom du passager : ")
    passager = Passager(nom, prenom)
    try:
        reservation.supprimer_passager(passager)
        print("La réservation a été annulée avec succès.")
    except ValueError as e:
        print(str(e))

def afficher_details_reservation(reservation):
    nom = input("Nom du passager : ")
    prenom = input("Prénom du passager : ")
    passager = Passager(nom, prenom)
    try:
        reservation.imprimer_details_reservation(passager)
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    avion = Avion("airbus 360","Jumbo")
    reservation = Reservation(avion)
    choix = None
    while choix != "6":
        afficher_menu()
        choix = input("Votre choix : ")
        if choix == "1":
            afficher_places_disponibles(avion)
        elif choix == "2":
            reserver_place(reservation)
        elif choix == "3":
            modifier_reservation(reservation)
        elif choix == "4":
            annuler_reservation(reservation)
        elif choix == "5":
            afficher_details_reservation(reservation)
        elif choix == "6":
            print("Au revoir !")
        else:
            print("Choix invalide. Veuillez réessayer.")