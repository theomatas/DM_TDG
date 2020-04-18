import lib.matrix_2
import os
import os.path

X,Y = 0,0
interface = False

try: 
    from tkinter import *  
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
            A = lib.matrix_2.Graph(file_)
            print (i , "charge")
            Matrix.append([i,A])
        except Exception as e:
            print (i , "non charge: " + str(e))
    print ("__________________")
    return Matrix

def select_file(Matrix):
    print (" ")
    for i in Matrix:
        print (Matrix.index(i) + 1, "/" , len(Matrix) , i[0])
    print ("entrer le numero du fichier")
    print("quiter pour sortir et charger pour reload les fichier")
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

def print_matrix(M):
    N = []
    m = len(str(lib.matrix_2.maxi_lst(M)))
    ml = len(str(len(M)))
    m = max([m,ml])
    print(' '*m ,end ="  ")
    for i in range(len(M)):
        print( (m - len(str(i)) + 1) *  ' ' + str(i) ,end =" ")
    print()
    x = 0
    for i in M:
        print( str(x) + (m - len(str(x)) + 1) *  ' ' ,end =" ")
        for j in i:
            
            if j == None:
                j = 'X'
            print((m - len(str(j)) + 1) *  ' ' + str(j),end =" ") 
        x += 1
        print()
    
def exo(obj):
    if interface and user():      
        from lib.interface import afs
        fen = Tk()
        canvas = Canvas(fen, width=1000, height=1000,bg="white")
        A = afs(obj,canvas,fen)
        A.run()
        canvas.pack()
        fen.mainloop()             
    else: 
        print ("exo 1: text parser " )
        for i in obj.get_brut():
            try:
                print(str(i[0]) + " -> " + str(i[1]) + " = " + str(i[2]))
            except:
                print(i)
            
        input()
        print ("exo 2: matrice ")
        print_matrix(obj.get_matrix())
        input()
        print ("exo 3: cycle = " + str(obj.cycle()) )
        input()
        print ("exo 4: rang = " + str(obj.rang()) )
        input()
        print ("exo 5: ordonnance = " + str(obj.ordonnance()) )
        input()
        print ("exo 6: trajet ")  
        try:
            x = 0
            
            for i in obj.trajet():
                print(["date tot","date tard","marge","marge min"][x] , " = " , i)
                x += 1
        except:
            print("non disponible")
                
        
def user():
    try:
        return int(input("interface" + '\n' + "1 - oui" + '\n' + "2 - non" + '\n' )) == 1
    except:
        return False
    
main() 

    
