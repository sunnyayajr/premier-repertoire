v= int(input ("Quelle est votre vitess ?  "))
d=(v/10)**2


do=int(input("Quelle est la distance de l'obstacle "))


print ("La distance de freinage est de", d)

       
if d > do:
    print ("CRASH")

else:
    print ("OUF")
    m = do-d 

    if m < 5:
        print ("LIMITE")

    



 

