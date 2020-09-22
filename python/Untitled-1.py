import os
nome=input("Inserisci il tuo nome:  ")
###################Comandi base###########################
if nome=="massimo":
    print("ciao, massimo")
elif nome=="spelling":
    for i in range (len(nome)):
        print (nome[i])
elif nome=="skip":
    print ("")
else:
    print("chi sei")
##################File Maniuplation######################
testo=open("text.txt","r+")
print (testo.read())
write=input("scrivi qualcosa dento il file")
if write != "skip" :
    testo.write(write+ "\n" )
testo.close()
###################OS call###############################
hostname="192.168.1.255"
respond = os.system("ping -n 1 "+ hostname)
if respond == 0:
    print ("raggiungibile")
else:
    print (hostname+"   down")
