
'''
#boucle :
for i in range (5):
    print(i)

#boucle :

fruits = ["pomme", "cerise"]
for fruit in fruits:
    print("liste :", fruit)


#boucle :
fruits = ["pomme", "cerise"]
print(fruits[1])

'''





'''
# boucle 

a=range (2,8,1)
b=list(range(8))
b1=list(range(2,8))
b2=list(range(2,8,1))
b3=list(range(2,8,3))
c=list(range(8,2,1))
d=list(range(8,8))
e=list(range(8,3,-1))
f=list(range(-2,-8,-2))
g=list(range(5,31,5))
h=list(range(50,30,-5))



  
    
# boucle pour repeter bonjour
for i in range (1,11):
    print (i, "- bonjour")

# boucle pour calculer la somme 
n=100
s=0 # ne pas oublier de declarer ici
for i in range (1,n+1):
    s=s+i**2
print("somme=",s) #calcul par la machine
print("somme=",n*(n+1)*(2*n+1)/6) #calcul avec formule

# ---------

s=0
for i in range (1,n+1):
    s=s+2**i
print("somme=",s)
print("somme=",n*(n+1)*(2*n+1)/6)


#chaines :

mot = "python"
print(mot[0])
print(mot[3])
print(mot[4])

mot = "python"
for lettre in mot:
    print(lettre)

mot = "python"
print(mot[2])

ch = "python"
print(len(ch))

#parcours d'une chaine :

#avec les indices
ch ="mot"
for i in range(len(ch)):
    print(ch[i])


for c in ch:
    print(c)


ch ="coucou"
for i in range(len(ch)):
    print(ch[i]) #reponse : coucou
    print(ch[3]) #reponse : cccccc
    

ch="bonjour"
resultat =""
for lettre in ch:
    resultat = resultat + lettre * 2
print(resultat)

'''

#exercice 5 - boucle sur tuple
etudiants= ("pierre","paul","mohamed", "lucie", "anne", "sophie", "lucas", "louane",
"maria", "romain", "celine", "justine", "ali", "tom", "dylan")
for prenom in etudiants:
    if (prenom[0]=='l') or (prenom[0]=='L'): #commence par 0 : si la premiere lettre es un l (1=0) afficher prenom (sensible a la casse : majuscule vs miniscule # if (prenom[0]=='l') : 
        print(prenom)

"""

    if ('a' in prenom): #contient 'contenu' : prenom contient a
        print (prenom)
    if (prenom[-1]=='e'): #termine par -1 : prenom se termine par e 
      print (prenom)
"""
for prenom in etudiants:  #programme qui calcule puis affiche le tuple des prénoms contenant au moins 6 lettres
    if len(prenom) == 6:
        print (prenom)

"""

    #exercice - res (produit cartesien) 

ch="coucou"
res = ""
for lettre in ch:
    res = res + lettre * 2
    print(res)
    

cc
ccoo
ccoouu
ccoouucc
ccoouuccoo
ccoouuccoouu
"""




s=0

nbrnotes=int(input("combien de valeurs="))
for i in range (1, nbrnotes+1): #je v de 1 jusqu'a 
    val=float(input("valeur"+str(i)+"?")) #pas de virgul dans input, on separe pas donc contactener 
if i == 1:
    mini = 0
    maxi = 20
    s+=val
    moy=s/nbrnotes
    print("somme=",s,"moyenne=", moy)
    

#  fonction initialisation par 1er valeur :   if i==1    mini=val   --     maxi=val    (maxi=max(maxi, val)   --   mini=val    (mini=min(mini, val)






















           
           
