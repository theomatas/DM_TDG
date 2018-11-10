def my_open(filename):

  path = filename
  days_file = open(path,'r')
  days = days_file.read()
  return (days)

def my_write(filename,text):

  path = filename
  days_file = open(path,'w')
  days_file.write(text)
  return 1

def parse(text):
  M = text.split('\n')
  x = 0
  while x < len(M):
    if x < 2:
      M[x] = int(M[x])
    else:
      M[x] = mini_parse(M[x])
    x += 1
  return M 

def mini_parse(text):
  M = text.split(' ')
  N = []
  for i in M:

    N.append(int(i))
  return N

def creat_matrix(n,lst):
  M = []
  for i in range(n):
    M.append([None]*n)
  for i in lst:
    M[i[0]][i[1]] = i[2]
  return M

def move_cycle(M,start,end):
  x = 0
  for i in M[start]:
    if i != None:
      if is_inside(end,x):
        return True
      else:
        end.append(x)
        return move_cycle(M,x,end)
    x += 1
  return False

def move_rang(M,start,val,rangs):
  x = 0
  if rangs[start] < val:
    rangs[start] = val
  for i in M[start]:
    if i != None:
      rangs = move_rang(M,x,val + 1,rangs)
    x += 1
  return rangs

def move_early(M,start,val,rangs):
  x = 0
  if rangs[start] < val:
    rangs[start] = val
  for i in M[start]:
    if i != None:
      rangs = move_early(M,x,val + M[start][x],rangs)
    x += 1
  return rangs

def move_late(M,start,val,rangs):
  x = 0
  m = len(M)
  if rangs[start] > val:
    rangs[start] = val
  while x < m:
    if M[x][start] != None:
      rangs = move_late(M,x,val - M[x][start],rangs)
    x += 1
  return rangs

def is_inside(M,x):
  for i in M:
    if i == x:
      return True
  return False

def in_out(M):
  m = len(M)
  in_ = [0]*m
  out_ = [0]*m
  x = 0
  while x < m:
    y = 0
    s = 0
    while y < m:
      if M[y][x] != None:
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
      if M[x][y] != None:
        s += 1
      y += 1
    if s == 0:  
      out_[x] = 1
    x += 1  
  return [in_,out_]
      
def in_zero(M):
  in_ = in_out(M)[0].index(1)
  m = len(M)
  for i in M[in_]:
    if i != 0 and i != None:
      return False
  return True

def check_incident(M):
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

def copy(M):
  N = []
  for i in M:
    N.append(i)
  return N

def maxi(L):
  x = None
  for i in L:
    if i != None and x == None:
      x = i
    if i != None and x < i :
      x = i
  return x
    
def maxi_lst(L):
  M = []
  for i in L:
    M.append(maxi(i))
  return maxi(M)
    
    
def positif(M):
  for i in M:
    for j in i:
      if j != None and j < 0:
        return False
  return True
      
class Graph:
  def __init__(self,filename):
    self.brut = parse(my_open(filename))
    self.matrix = creat_matrix(self.brut[0],self.brut[2:])
  def get_matrix(self):
    return self.matrix
  def get_brut(self):
    return self.brut
  def cycle(self):
    M = self.matrix
    for i in M:
      if move_cycle(M,M.index(i),[M.index(i)]):
        return True
    return False
  def rang(self):
    if self.cycle():
      return False
    M = self.matrix
    m = self.brut[0]
    rangs = [0]*m
    in_ = in_out(M)[0]
    for i in range(m):
        rangs = move_rang(M,i,0,rangs)
    return rangs
  def ordonnance(self):
    M = self.matrix
    in_ = in_out(M)[0]
    out_ = in_out(M)[1]
    if not positif(M):
      return False , "one variable is negative"
    if self.cycle():
      return False , "is a cycle"
    if not sum(in_) == 1 :
      return False , "wrong number of input"
    if not sum(out_) == 1:
      return False , "wrong number of output"  
    if not in_zero(M):
      return False , "not 0 for out of first node"
    if not check_incident(M):
      return False , "incident arc value not equal" 
    return True

  def trajet_early(self):
    M = self.matrix
    m = self.brut[0]
    early = [0]*m
    in_ = in_out(M)[0]
    x = 0
    for i in early:
        early = move_early(M,x,0,early)
        x += 1
    return early  
  def trajet_late(self,early):
    M = self.matrix
    m = self.brut[0]
    late = []
    for i in early:
      late.append(1000)
    out_ = in_out(M)[1]
    x = 0
    for i in out_:
      if i == 1:
        late = move_late(M,x,early[x],late)
      x += 1
    return late   
  def tache(self):
    M = self.matrix
    N = []
    for i in M:
      N.append(maxi(i))
    return N
  def marge_min(self,early,arc):
    Mat = self.matrix
    m = self.brut[0]
    M = []
    n = 0
    for i in Mat:
      x = 0
      N = []
      for j in i:
        if j != None:
          N.append(early[x])
        x += 1
      if N!= []:
        M.append(min(N) - early[n] - arc[n])
      else:
        M.append(0)
      n += 1
    return M
          
  def trajet(self):
    if self.ordonnance() != True:
      return False    
    early = self.trajet_early()
    late = self.trajet_late(copy(early))
    tache = self.tache()
    marge_min = self.marge_min(early,tache)
    marge = []
    for i in range(len(self.matrix)):
      e = early[i]
      l = late[i]
      marge.append(l-e)
      
    return [early,late,marge,marge_min]
