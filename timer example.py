import tkinter as tk
import time as t
window = tk.Tk()

class f:
    def __init__(self):
        self.go = True
    
    
    def stoptimer(self):
        self.go = False
        


    def timer(self):
        self.go = True
        timeout = t.time() + 5
        r = t.time()
        x = timeout - t.time()
        title = tk.Label(master=window,text = "Time Left " + str(x))
        title.pack()
        true_btn = tk.Button(master=window,text = "Stop",command = self.stoptimer)
        true_btn.pack()
        while t.time() < timeout and self.go == True:
            if t.time() > r + 1:
                r = t.time()
                y = timeout - t.time()
                x = round(y)
                title.config(text = "Time Left " + str(x))
                title.update()
          
            
            
        title.config(text = "Time Left 0")
        title.update()
        if self.go == False:
            print("Button Pressed")
        else:
            print("Time Up")
        
        

game = f()
game.timer()