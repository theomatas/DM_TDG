import lib.matrix_2                # importation de la bibliotheque matrix 2, calcul graph
import os
import os.path                     # importation de bibliotheques os, os.path : acces adresses fichiers

X,Y = 0,0                          # initialisation coordonnees de souris (0,0)
interface = False                  # par defaut interface indisponible= false

try:                               
    from tkinter import *  
    print ("interface importe")
    interface = True                #test de l'importation de l'interface graphique 
except:
    print ("interface non disponible")   
 
def loader():                       
    path= os.path.dirname(__file__) + "//..//graph"   #recuperation chemin acces fichier graph
    way = os.listdir(path)                        #recuperation contenu fichier graph
    Matrix = []                                   
    for  i in way:                                  #on itere dans i le nom des fichiers
        file_ = path + "//" + i                 #creation chemin d'acces aux fichiers
        try:
            A = lib.matrix_2.Graph(file_)       #instancier la classe graph avec chaque fichier
            print (i , "charge")                 
            Matrix.append([i,A])                #on dit que le fichier a ete charge
        except Exception as e:                  
            print (i , "non charge: " + str(e))             #le fichier n'a pas ete charge l'erreur est affiche
    print ("__________________")
    return Matrix

def select_file(Matrix):            #demande l'utilisateur un numero de fichier 
    print (" ")       
    for i in Matrix:                                                
        print (Matrix.index(i) + 1, "/" , len(Matrix) , i[0])       
    print ("entrer le numero du fichier")
    print("sortir pour quitter et charger pour reload les fichier")
    IN = input()
    if IN == "sortir":
        return None
    if IN == "charger":
        return 0
    try:
        if int(IN):
            return int(IN)
    except Exception as e:
        print("erreur: "+ str(e))
        return -1
    return -1

def main():
    Matrix = loader() #recuperation de classe loader par matrix
    File = select_file(Matrix)                 
    while File != None:                 #verification de la non interruption du programme
        if 0 < File <= len(Matrix):         #on lance l'algorithme de calcul de graphe si le numero de fichier est valide
            exo(Matrix[File - 1][1])        
        if not File:                        #on relance le chargement des fichiers
            Matrix = loader()
        File = select_file(Matrix)

    print ("fin du programme")

def print_matrix(M):   #se charge d'afficher la matrice d'arc en paddant les resultats
    N = []
    m = len(str(lib.matrix_2.maxi_lst(M)))
    ml = len(str(len(M)))
    m = max([m,ml])
    print(' '*m ,end =" ")
    for i in range(len(M)):
        print( (m - len(str(i)) + 1) *  ' ' + str(i) ,end ="")
    print()
    x = 0
    for i in M:
        print( str(x) + (m - len(str(x)) + 1) *  ' ' ,end ="")
        for j in i:
            
            if j == None:
                j = 'X'
            print((m - len(str(j)) + 1) *  ' ' + str(j),end ="") 
        x += 1
        print()
    
def exo(obj):
    if interface and user():             #si l'interface est disponible et l'utilisateur est d'accord le graphe sera affiche sur l'interface graphique  
        from lib.interface import afs
        fen = Tk()
        canvas = Canvas(fen, width=1000, height=1000,bg="white")
        A = afs(obj,canvas,fen)
        A.run()
        canvas.pack()
        fen.mainloop()             
    else: 
        print ("exo 1: text parser " )
        count = 0 
        for i in obj.get_brut():
            try:
                print(str(i[0]) + " -> " + str(i[1]) + " = " + str(i[2]))
            except:
                t = "arcs"
                if count == 0:
                    t = "sommets"
                print(i,t)
            count += 1
            
        input("appuyer sur entrer pour continuer")
        print ("exo 2: matrice ")
        print_matrix(obj.get_matrix())
        input("appuyer sur entrer pour continuer")
        print ("exo 3: cycle = " + str(obj.cycle()) )
        input("appuyer sur entrer pour continuer")
        print ("exo 4: rang = " + str(obj.rang()) )
        input("appuyer sur entrer pour continuer")
        print ("exo 5: ordonnance = " + str(obj.ordonnance()) )
        input("appuyer sur entrer pour continuer")
        print ("exo 6: trajet ")  
        try:
            x = 0
            
            for i in obj.trajet():
                print(["date tot","date tard","marge","marge min"][x] , " = " , i)
                x += 1
        except:
            print("non disponible")
        input("appuyer sur entrer pour continuer")
        
def user():             #permet a l'utilisateur de lancer ou non l'interface graphique
    try:
        return int(input("interface" + '\n' + "1 - oui" + '\n' + "2 - non" + '\n' )) == 1
    except:
        return False
    
main()                   #lancement de la fonction main

