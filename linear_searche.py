def linear_searche(item, my_liste):
  "Fonction for linear searche in liste"
    found = False
    for i in range (len(my_liste)):
        if my_liste[i] == item:
            found = True
    return found

liste = [3,65, 64, 4, 5, 14, 44, 23, 34]
linear_searche(44, liste)
