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
  M = cut(text,'\n')
  x = 0
  while x < len(M):
    if x < 2:
      M[x] = int(M[x])
    else:
      M[x] = mini_parse(M[x])
    x += 1
  return M 

def cut(text,car):
  M = []
  s = ""
  for i in text:
    if i == car:
      M.append(s)
      s = ""
    else:
      s += i
  M.append(s)
  return M

def mini_parse(text):
  
  M = cut(text,' ')
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
  if rangs[start] > val:
    rangs[start] = val
  for i in M[start]:
    if i != None:
      rangs = move_rang(M,x,val + 1,rangs)
    x += 1
  return rangs

def is_inside(M,x):
  for i in M:
    if i == x:
      return True
  return False

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
    rangs = [1000]*m
    x = 0
    while x < m:
      y = 0
      s = 0
      while y < m:
        if M[y][x] != None:
          s += 1
        y += 1
      if s == 0:
        rangs[x] = 0
        rangs = move_rang(M,x,0,rangs)
      x += 1
    return rangs
        
        
      
      
      
    
