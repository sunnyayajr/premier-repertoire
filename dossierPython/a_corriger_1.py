# ce script comporte des erreurs qui empêchent son bon déroulement.
# corrigez les erreurs en n'oubliant pas de bien regarder les messages d'erreur


# definitions de quelques constantes
pi= 3.14159
e= 2.71
i= 5

#dialogue1
ps=input ("quel est votre pseudo?  ")
print ("bonjour ",ps)
a= int(input ("votre annee de naissance  ?"))
print( " ah vous avez " , 2024 - a  , "ans")
print ("au revoir")

#dialogue2
ps=input ("quel est votre pseudo?  ")
age=input ("bonjour "+ps + "quel est votre âge?")
print("plus que 100-age avant d'être centenaire ")

# calculs de quelques termes d'une suite

n=0
x=5
x=2+x/3
n+=1
x=2+x/3
n+=1
x=2+x/3
n+=1
x=2+x/3
n+=1
x=2+x/3
n+=1
print("x =", x,"n", n )


