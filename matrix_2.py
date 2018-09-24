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

def move(M,start,end):
  for i in M[start]:
    if i != None:
      if is_inside(end,M[start].index(i)):
        return True
      else:
        end.append(M[start].index(i))
        return move(M,M[start].index(i),end)
  return False

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
      if move(M,M.index(i),[M.index(i)]):
        return True
    return False
    
