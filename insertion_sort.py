def insertion_sort(my_liste):
  "Fonction fot the insertion sorte of a liste"
    n = len(my_liste)
    for i in range(1, n):
        j = i - 1
        if my_liste[i] < my_liste[j]:
            my_liste[i],my_liste[j] = my_liste[j] , my_liste[i]
            print(my_liste)
            insertion_sort(my_liste)
    return my_liste




liste = [3,5, 64, 4, 25, 14, 44, 23, 34]
insertion_sort(liste)
