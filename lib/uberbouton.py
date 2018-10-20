# creat_button

class Button():
    def __init__(self,canvas,pos,name,color):
        self.name = name
        self.pos = pos[0] , pos[1]
        self.rect = canvas.create_rectangle(self.pos[0] - 50,self.pos[1] - 15,self.pos[0] + 50,self.pos[1] + 15,fill=color,width = 0)
        self.text = canvas.create_text(self.pos[0],self.pos[1],text=name, font="10", fill="red")
        self.can = canvas
    def act (self,X,Y):
        if abs( X - self.pos[0] ) < 40 and abs( Y - self.pos[1] ) < 10:
            return 1
        else:
            return 0 
    def get_fct(self):
        return self.name
    def destroy(self):
        self.can.delete(self.text)
        self.can.delete(self.rect)        
    def __del__(self):
        return "BUTTON DESTROY"

# manage_button

class UberButton():
    def __init__(self,canvas):
        self.canvas = canvas
        self.lst = []
    def check_fct(self,X,Y):
        for i in self.lst:
            if i.act(X,Y):
                fct = i.get_fct()
                #i.destroy()
                return fct
        return 0
    def add_fct(self,pos,name,color):
        lst = self.lst
        lst.append(Button(self.canvas,pos,name,color))
        return 0
    def __del__(self):
        return "UBERBUTTON DESTROYED"
    def sup(self):
        for i in self.lst:
            del i
        self.lst = []
        
    
