# pour répondre à l'énoncé donné sur la feuille TP, une étudiant a rendu le programme ci-dessous.
# il est content , pas de rouge quand il le fait fonctionner.
# il a fait un test avec un poids de 3 kilos et a obtenu le bon résultat.
# il est sûr de mériter un 20/20
# qu'en pensez-vous?


poids= float(input("Bonjour quelle est le poids de votre paquet"))


if poids<=0.1 :
    print("Les frais sont de 1.5")
if 0.1<poids<=0.5:
    print ("les frais sont de 3")
if 0.5<poids<=1 :
    print ("les frais sont de 5")
if 1<poids<=2 :
    print ("les frais sont de 7")
else:
    print ("les frais sont de 15")
