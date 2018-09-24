print("partie_1" + '\n' )b #partie_1

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
  print(lst)
  for i in range(n):
    M.append([None]*n)
  for i in lst:
    M[i[0]][i[1]] = i[2]
  return M




class Graph:
  def __init__(self,filename):
    self.brut = parse(my_open(filename))
    self.matrix = creat_matrix(self.brut[0],self.brut[2:])
    print (self.matrix )

  

Graph("tests.txt")
