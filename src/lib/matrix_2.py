def my_open(filename):

  file = open(filename,'r')
  text = file.read()
  return (text)

def parse(text):            #retourner un tableau dont le premier element et le nombre de sommets et le deuxieme le nombre d'arcs suivit par les arcs eux même 
  M = text.split('\n')       #separation du text par retour a la ligne
  x = 0
  while x < len(M):
    if x < 2:
      M[x] = int(M[x])
    else:
      M[x] = mini_parse(M[x])     #on appelle mini_parse sur chaque ligne de valeur d'arc
    x += 1
  return M 

def mini_parse(text):     #retourner un tableau [sommet de depart,sommet d'arriver, valeur arc]
  M = text.split(' ')       #separation du text par des espaces
  N = []
  for i in M:
    N.append(int(i))
  return N

def creat_matrix(n,lst):   #retourner un tableau carre de taille sommet*sommet (matrice de valeur d'arc)
  M = []
  for i in range(n):
    M.append([None]*n)    #remplir avec des "None" toute la matrice
  for i in lst:             #iterer toute les valeurs d'arc
    M[i[0]][i[1]] = i[2]      #on complete la matrice selon: sommet de depart = ligne, sommet d'arriver = colonne, valeur d'arc = valeur cette position de la matrice
  return M

def move_cycle(M,start,end):         #verification d'un sommet (ligne) et lancement recursif sur un sommet donne
  x = 0
  for i in M[start]:                  #on itaire les differents arc possible depuis le sommet "start"
    if i != None:                   #passer les valeurs inexistante
      if is_inside(end,x):              #pour une valeur existante verification grace a is_inside
        return True                   #fin du programme si valeur deja dans end
      else:
        sto = copy(end)
        end.append(x)                 #ajoute la valeur a end
        if move_cycle(M,x,end):
          return True     #recursivite sur la fonction, on relance la fonction sur le sommet(ligne) suivant    
        end = sto
          
    x += 1
  return False

def move_rang(M,start,val,rangs):           #calcul du rang pour un sommet(ligne) sa valeur sera mise a jour si la valeur du rang est inferrieur a la valeur stockee
  x = 0
  if rangs[start] < val:              #remplacement de la valeur si necessaire
    rangs[start] = val            
  for i in M[start]:
    if i != None:
      rangs = move_rang(M,x,val + 1,rangs)      #on appelle move_rang sur le successeur selectione tout en ajoutant 1 a la valeur de rang actuelle
    x += 1
  return rangs

def move_early(M,start,val,rangs):      #calcul du chemin au plus tot pour un sommet(ligne) sa valeur sera mise a jour si la valeur du rang est inferrieur a la valeur stockee
  x = 0
  if rangs[start] < val:
    rangs[start] = val
  for i in M[start]:
    if i != None:
      rangs = move_early(M,x,val + M[start][x],rangs)  #on appelle move_rang sur le successeur selectione tout en ajoutant la valeur de l'arc
    x += 1
  return rangs

def move_late(M,start,val,rangs):       #calcul du chemin au plus tard pour un sommet(ligne) sa valeur sera mise a jour si la valeur du rang est inferrieur a la valeur stockee
  x = 0
  m = len(M)
  if rangs[start] == None or rangs[start] > val:
    rangs[start] = val
  while x < m:
    if M[x][start] != None:
      rangs = move_late(M,x,val - M[x][start],rangs) #on appelle move_rang sur le successeur selectione tout en retirant la valeur de l'arc
    x += 1
  return rangs

def is_inside(M,x): #dit si l'element demande est dans le tableau
  for i in M:
    if i == x:
      return True
  return False

def in_out(M):       #retourne deux tableaux distinct un pour l'entree et un pour la sortie avec des 1 si le sommet est une sortie ou une entree (sinon 0)           
  m = len(M)
  in_ = [0]*m
  out_ = [0]*m
  x = 0
  while x < m:        
    y = 0
    s = 0
    while y < m:
      if M[y][x] != None:         #pour les entrees on regarde la colonne d'un sommet
        s += 1
      y += 1
    if s == 0:  
      in_[x] = 1
    x += 1
  x = 0
  while x < m:
    y = 0
    s = 0
    while y < m:
      if M[x][y] != None:       #pour les sorties on regarde la ligne d'un sommets
        s += 1
      y += 1
    if s == 0:  
      out_[x] = 1
    x += 1  
  return [in_,out_]
      
def in_zero(M):                 #on verifie que toutes les valeurs d'arc incidents sont nulles
  in_ = in_out(M)[0].index(1)
  m = len(M)
  for i in M[in_]:
    if i != 0 and i != None:
      return False
  return True

def check_incident(M): # on verifie que pour un meme sommet les valeur d'arc soit egals.
  m = len(M)
  x = 0
  while x < m:
    y = 0
    s = None
    while y < m:
      j = M[x][y]
      if j != None and s != None and s != j:
        return False
      if j != None:
        s = j
      y += 1
    x += 1
  return True

def copy(M): # copi le contenue d'un tableau
  N = []
  for i in M:
    N.append(i)
  return N

def maxi(L): # permet de trouver le maximun d'un tableau meme s'il contient des None(s) 
  x = None
  for i in L:
    if i != None and x == None:
      x = i
    if i != None and x < i :
      x = i
  return x
    
def maxi_lst(L): # appelle la fonction maxi ( capable de marcher malgrees des None(s)) sur chaques ligne d'un tableau pour en trouver le maximun.
  M = []
  for i in L:
    M.append(maxi(i))
  return maxi(M)
    
    
def positif(M):          # s'il y a une valeur d'arc negative dans la matrice d'arc on retourne faux sinon vrai 
  for i in M:
    for j in i:
      if j != None and j < 0:
        return False
  return True
      
class Graph:
  def __init__(self,filename):
    self.brut = parse(my_open(filename))    # recuperation du text parse
    self.matrix = creat_matrix(self.brut[0],self.brut[2:]) # retourne la matrice de valeur d'arc
  def get_matrix(self):
    return self.matrix
  def get_brut(self):
    return self.brut
  def cycle(self):   # True = circuit(s), False = pas de circuit
    M = self.matrix
    x = 0
    for i in M:
      if move_cycle(M,x,[x]):   #on verifie qu'en partant de n'importe quel sommet nous n'avons pas de cycle
        return True
      x += 1
    return False
  def rang(self):         #calcul du rang
    if self.cycle():      #verification s'il y a un cycle
      return False        #retourner false et sortir de la fonction s'il y a un cycle
    M = self.matrix         #initialisation de la matrice dans M
    m = self.brut[0]        #initialisation de m sommets
    rangs = [0]*m           #tableau de 0 de longueur m
    for i in range(m):          #parcourir tous les sommets
        rangs = move_rang(M,i,0,rangs)    
    return rangs
  def ordonnance(self):        #fonction dde teste d'ordonnancement 
    M = self.matrix
    in_ = in_out(M)[0]        #initiliser liste entrees
    out_ = in_out(M)[1]         #initialiser liste sorties
    if not positif(M):        
      return False , "il y a au moins une valeur d'arc negative"
    if self.cycle():
      return False , "c'est un cycle"           
    if not sum(in_) == 1 :                        #si la sommme de la liste in_ est egale a 1 il y a une entree
      return False , "mauvais nombre en entree"
    if not sum(out_) == 1:                        #si la somme de la liste out_ est egale a 1 il y a une sortie
      return False , "mauvais nombre en sortie"  
    if not in_zero(M):
      return False , "il n'y pas que des 0 en sortie du sommet initial"
    if not check_incident(M):
      return False , "valeur d'arc d'incidence ne sont pas egales pour un meme sommet" 
    return True

  def trajet_early(self): # calcul du chemin au plus tot
    M = self.matrix
    m = self.brut[0]
    early = [0]*m # on genere un tableau remplie de 0 d'une longeur egal au nombre de sommets
    in_ = in_out(M)[0]
    early = move_early(M,in_.index(1),0,early) # on lance la fonction recursive sur le sommet d'entree du graph
    return early  
  def trajet_late(self,early): # calcul du chemin au plus tard
    M = self.matrix
    m = self.brut[0]
    late = [None]*m # on genere un tableau remplie de None d'une longeur egal au nombre de sommets
    out_ = in_out(M)[1]
    x = out_.index(1)
    late = move_late(M,x,early[x],late) # on lance la fonction recursive sur le sommet de sorti du graph
    return late   
  def tache(self): # retourne le tableau des valeur d'arc ( un sommet = une valeur car graphe d'ordonnancement )
    M = self.matrix
    N = []
    for i in M:
      N.append(maxi(i))
    return N
  def marge_min(self,early,arc): # calcul du chemin au plus tot
    Mat = self.matrix
    m = self.brut[0]
    M = []
    n = 0
    for i in Mat:
      x = 0
      N = []
      for j in i:
        if j != None:
          N.append(early[x]) # on stock dans le tableau N les chemin au plus tot 
        x += 1
      if N!= []:
        M.append(min(N) - early[n] - arc[n]) # calcul du chemin au plus tot, minimun(chemin au plus tot des successeurs 
      else:
        M.append(0)
      n += 1
    return M
          
  def trajet(self):
    if self.ordonnance() != True:
      return False    
    early = self.trajet_early()     #recuperation chemin au plus tot
    late = self.trajet_late(copy(early))     #recuperation chemin au plus tard
    tache = self.tache()                  #recuperation de tache
    marge_min = self.marge_min(early,tache)     #recuperation de marge min
    marge = []
    for i in range(len(self.matrix)):
      e = early[i]
      l = late[i]
      marge.append(l-e) # la marge total est calcule ici. trajet au plus tard - trajet au plus tot.
      
    return [early,late,marge,marge_min]      #tout retourner
