from tkinter import *
from lib.uberscript import UberScript
from lib.uberbouton import UberButton
from math import sin,cos
X,Y = 0,0

class afs():
    def __init__(self,obj,canvas,fen):
        self.obj = obj
        but = UberButton(canvas)
        self.script =  UberScript(canvas,(10,10,500,100),'gray')   
        self.script.ad("graph initialiser","blue")
        name = ["number","rang","date tot","date tard","marge","marge min"]
        self.name = name
        x = 0
        Y = 950
        X = 100
        while x < len(name):
            but.add_fct((X + 150*x,Y),name[x],"blue","white")
            x += 1
        
        self.button = but
        self.obj = obj
        self.can = canvas
        self.fen = fen
        self.txt = []
        self.x = 0
        try:
            self.rang = [obj.rang(),max(obj.rang())]
            M = []
            N = []
            for i in range(0,self.rang[1]+1):
                M.append([])
            for i in self.rang[0]:
                x,y = i*1000/(self.rang[1]+1) + 50 ,len(M[i])*1000/(self.rang[1]+1) + 150 + 100 * (i%3)
                M[i].append([x,y])
                N.append([x,y,canvas.create_oval(x-30,y-30,x+30,y+30,fill = 'blue'),[]])
            self.place = N
            self.matrix = obj.get_matrix()
            i = 0
            while i < len(N):
                y = 0
                for ind in self.matrix[i]:
                    if ind != None:
                        x1,y1,x2,y2 = N[i][0] + 30,N[i][1],N[y][0] - 30,N[y][1]
                        line = canvas.create_line(x1,y1,x2,y2, fill="red",arrow=LAST,arrowshape=(4,4,4),width = 2)
                        canvas.create_text((x1+x2*3)/4,(y1+y2*3)/4,text = str(ind),font="Times 20 bold",fill = "blue")
                        #canvas.lower(line)
                        N[i][-1].append([x1,y1,x2,y2,line])
                    y += 1
                i += 1
        except:
            self.script.ad("erreur cycle","orange")
            

                
    def run(self):
        self.can.bind("<Button-1>", click)
        cmd = None
        if X + Y != 0:
            try:
                for i in self.txt:
                    self.can.delete(i)         
                txt = []
                cmd = self.name.index(self.button.check_fct(X,Y))
                self.script.ad(self.button.check_fct(X,Y),"blue")
                if cmd == 0:
                    line = []
                    for i in range(0,len(self.matrix)):
                        line.append(i)
                elif cmd == 1:
                    line = self.obj.rang()
                else:
                    line = self.obj.trajet()[cmd-2]
                x = 0
    
                for i in self.place:
                    txt.append(self.can.create_text(i[0],i[1],text = str(line[x]),font="Times 20 italic bold",fill = "white"))
                    x += 1
                self.txt = txt
            except:
                self.script.ad("commande impossible","red")

            
        reset()
        self.fen.after(10,self.run)
 

  
def reset():
    global X,Y
    X = 0
    Y = 0 

def click(event):
    global X,Y
    X = event.x
    Y = event.y

  