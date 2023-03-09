# OnePoint
Le code présenté est un ensemble de classes permettant d'attribuer des sièges dans un avion. 
* La classe `Passager` représente un passager avec un nom et un prénom. 
* La classe `Avion` permet de créer un objet avion avec une taille spécifiée (Jumbo, Jumbo_2, Mid-Size, Mid-Size_2, Light ou Light_2). 
Le code utilise une disposition pré-définie des places pour chaque taille d'avion et crée une matrice de places à None. 

Les méthodes `est_place_disponible`, `attribuer_place`,`liberer_place` et `modifier_place`  permettent de vérifier si une place est disponible, d'attribuer une place à un passager, de libérer une place et de modifier la place d'un passager.



* La classe `Reservation` représente une réservation pour un avion spécifié et permet d'ajouter, de modifier et de supprimer des passagers dans cette réservation.

La méthode `ajouter_passager`  ajoute un nouveau passager à la réservation et attribue une place disponible pour ce passager. La méthode ` modifier_place` permet de modifier la place d'un passager dans la réservation  la méthode  `supprimer_passager` supprime un passager de la réservation et la méthode `imprimer_details_reservation` donne les détails de réservation d'un ou plusieurs passagers.

