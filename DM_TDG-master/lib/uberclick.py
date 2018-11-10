def reset():
    global X,Y
    X = 0
    Y = 0 

def click(event):
    global X,Y
    X = event.x
    Y = event.y
    print (X,Y)

