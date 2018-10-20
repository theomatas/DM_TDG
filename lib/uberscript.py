class Script():
    def __init__(self,canvas,text,pos,color):
        self.canvas = canvas
        self.text = text
        self.pos = pos
        self.color = color
        self.ent = 0
        self.creat()
    def creat(self):
        if not self.ent:
            self.ent = self.canvas.create_text(self.pos ,text= self.text, font="10", fill= self.color , anchor= 'w')
    def move(self,height):
        self.pos = [self.pos[0],height]
        self.destroy()
        self.creat()
    def destroy(self):
        if self.ent: 
            self.canvas.delete(self.ent)
            self.ent = 0
    def __del__(self):
        try:
            self.destroy()
            return "line destroye -> " + str(self.text)
        except:
            pass
    def get_height(self):
        return self.pos[1]
    
class UberScript():
    def __init__(self,canvas,pos,color):
        self.canvas = canvas
        self.pos = pos
        self.lst = []
        self.rect = canvas.create_rectangle(self.pos[0],self.pos[1],self.pos[2],self.pos[3],fill=color,width = 0)
    def ad(self,text,color):
        new_line = Script(self.canvas,text,(self.pos[0] + 5 , self.pos[3] - 15),color)
        lst = self.lst
        x = 0
        while x < len(lst):
            i = lst[x]
            i.move(i.get_height() - 20 )
            if i.get_height() < self.pos[1] + 15:
                lst.pop(x)
                i.destroy()
                x -= 1
            x += 1
        lst.append(new_line)
        self.lst = lst
    def sup(self):
        for i in self.lst:
            del i
        self.lst = []
    def destroy(self):
        try:
            self.canvas.delete(self.rect)
        except:
            pass
    def __del__(self):
        self.destroy()
        return "FEN DESTROY"
        
            