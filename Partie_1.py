import matrix_2
import os
import os.path

try: 
    from Tkinter import *
    print ("interface importe")
    interface = True
except:
    print ("interface non disponible")
 
def loader():   
    path= os.path.dirname(__file__) + "//graph"
    way = os.listdir(path)
    Matrix = []
    for  i in way:
        file_ = path + "//" + i 
        try:
            A = matrix_2.Graph(file_)
            print (i , "charge")
            Matrix.append([i,A])
        except:
            print (i , "non charge")
    print ("__________________")
    return Matrix

def select_file(Matrix):
    print (" ")
    for i in Matrix:
        print (Matrix.index(i) + 1, "/" , len(Matrix) , i[0])
    print ("entrer le numero du fichier")
    IN = input()
    if IN == "sortir":
        return None
    if IN == "charger":
        return 0
    try:
        if int(IN):
            return int(IN)
    except:
        return -1
    return -1

def main():
    Matrix = loader()
    File = select_file(Matrix)
    while File != None:
        if 0 < File <= len(Matrix):
            exo(Matrix[File - 1][1])        
        if not File:
            Matrix = loader()
        File = select_file(Matrix)

    print ("fin du programme")
    
def exo(obj):
    
    print ("exo 1: text parser " + str(obj.get_brut()) )
    input()
    print ("exo 2: matrice " + str(obj.get_matrix()) )
    input()
    print ("exo 3: cycle = " + str(obj.cycle()) )
    input()
    print ("exo 4: rang = " + str(obj.rang()) )
    input()
    print ("exo 5: rang = " + str(obj.ordonnance()) )
    input()
    print ("exo 6: trajet " + str(obj.trajet()) )    
    
    
main() 
