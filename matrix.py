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
    N = []
    x = 0
    while x < len(M):
      y = 0
      while y < len(M[x]):
        if M[x][y] != None:
          D = 0
          for i in [[1,1],[-1,1],[1,-1],[-1,-1]]:
            s = 0
            pos = [x,y]
            
            while s == 0:
              
                pos[0] += i[0]
                pos[1] += i[1]
                if  0 <= pos[1] < len(M[x]) and 0 <= pos[0] < len(M):
                  if M[pos[0]][pos[1]] != None:
                    D += 1
                else:
                  s = 1
            N.append(D)
        y += 1
      x += 1
    if max(N) > 1: 
      return True
    return False
