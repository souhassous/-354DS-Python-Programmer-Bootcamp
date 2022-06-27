def binary_searche(item, my_liste):
  "Fonction for the binary searche in liste"
    found = False
    my_liste = sorted(my_liste)
    print(my_liste)
    first = 0
    last = len(my_liste) -1
    
    while first <= last and found == False:
        midpoint = (first + last) // 2
        print(midpoint)
        if my_liste[midpoint] == item:
            found = True
        elif my_liste[midpoint] > item:
            last = midpoint - 1
        else:
            first = midpoint +1
    return found

liste = [3,65, 64, 4, 5, 14, 44, 23, 34]
binary_searche(5, liste)
