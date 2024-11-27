import tkinter as tk
import os as o
import time as t
window = tk.Tk()

class quizz:
    def __init__(self):
        self.curQuestion = ""
        self.userInput = ""
        self.inputQuestion = ""
        self.num = 0
        self.quizz = []
        self.curQuizz = 0
        self.ans = ""
        self.playerAns = ""
        self.dirs = []
        self.score = 0
        self.q = 0
        self.modechoice = ""
        self.qnum = 0
        self.questionList = []
        self.quizzScores = []
        

        
    def choice(self):
        window.configure(bg="ghost white")
        title = tk.Label(master=window,text = "Welcome To Quiz HQ, what would you like to do?",fg = "gray13", font= 'Impact 45',bg = "ghost white")
        title.place(x=425,y=100)
        title = tk.Label(master=window,text = "Brought To You By Aidan !",fg = "gray13", font= 'Impact 30',bg = "ghost white")
        title.place(x=750,y=900)
        play_btn = tk.Button(master=window,text = "Play", command = self.homeQuizz,width = 45,height=15,bg = "DodgerBlue4", font= 'Impact 20',fg =  "white")
        play_btn.place(x=150,y=200)

        create_btn = tk.Button(master=window,text = "Create", command = self.createEdit,width = 45,height=15,bg = "goldenrod3", font= 'Impact 20',fg =  "white")
        create_btn.place(x=1200,y=200)
        
    
    def file_manger(self):
        self.fd1 = "quizz_1.txt"
        self.fd2 = "quizz_2.txt"
        self.fd3 = "quizz_3.txt"
        self.fd4 = "quizz_4.txt"
        self.fd5 = "quizz_5.txt"
        self.fd6 = "quizz_6.txt"
        self.fd7 = "quizz_7.txt"
        self.fd8 = "quizz_8.txt"
        self.fd9 = "quizz_9.txt"
        self.fd10 = "quizz_10.txt"
        self.h1 = "quizz1_highscores.txt"
        self.h2 = "quizz2_highscores.txt"
        self.h3 = "quizz3_highscores.txt"
        self.h4 = "quizz4_highscores.txt"
        self.h5 = "quizz5_highscores.txt"
        self.h6 = "quizz6_highscores.txt"
        self.h7 = "quizz7_highscores.txt"
        self.h8 = "quizz8_highscores.txt"
        self.h9 = "quizz9_highscores.txt"
        self.h10 = "quizz10_highscores.txt"
        self.dirs = [self.fd1,self.fd2,self.fd3,self.fd4,self.fd5,self.fd6,self.fd7,self.fd8,self.fd9,self.fd10,self.h1,self.h2,self.h3,self.h4,self.h5,self.h6,self.h7,self.h8,self.h9,self.h10]        

    def Quizz1(self):
        self.qnum = 0
        self.filePathDefiner()
        
    
    def Quizz2(self):
        self.qnum = 1
        self.filePathDefiner()
        
                
    def Quizz3(self):
        self.qnum = 2
        self.filePathDefiner()
        
    def Quizz4(self):
        self.qnum = 3
        self.filePathDefiner()
    
    def Quizz5(self):
        self.qnum = 4
        self.filePathDefiner()
        
    def Quizz6(self):
        self.qnum = 5
        self.filePathDefiner()
        
    def Quizz7(self):
        self.qnum = 6
        self.filePathDefiner()
        
    def Quizz8(self):
        self.qnum = 7
        self.filePathDefiner()
        
    
    def Quizz9(self):
        self.qnum = 8
        self.filePathDefiner()
    
    def Quizz10(self):
        self.qnum = 9
        self.filePathDefiner()
  
    def filePathDefiner(self):
        file = open(self.dirs[self.qnum], 'r')
        text = file.read()
        self.quizz = text.split(",")
        file.close()
        file = open(self.dirs[self.qnum + 10], 'r')
        text = file.read()
        self.quizzScores = text.split(",")
        file.close()
        self.Run()
  
    def back(self):
        for widget in window.winfo_children():
            widget.destroy()
        self.choice()
        
            
    def homeQuizz(self):
        self.modechoice = "play"
        self.groupButtons()
            
            
    def groupButtons(self):
        for widget in window.winfo_children():
            widget.destroy()
        if self.modechoice == "play":
            window.configure(bg="DodgerBlue4")
            self.bg = "DodgerBlue4"
        else:
            window.configure(bg="goldenrod3")
            self.bg = "goldenrod3"
        one_btn = self.gameButton("Quiz 1", self.Quizz1)
        one_btn.place(x=350,y=250)
        two_btn = self.gameButton("Quiz 2", self.Quizz2)
        two_btn.place(x=575,y=250)
        three_btn = self.gameButton("Quiz 3", self.Quizz3)
        three_btn.place(x=800,y=250)
        four_btn = self.gameButton("Quiz 4", self.Quizz4)
        four_btn.place(x=1025,y=250)
        five_btn = self.gameButton("Quiz 5", self.Quizz5)
        five_btn.place(x=1250,y=250)
        six_btn = self.gameButton("Quiz 6", self.Quizz6)
        six_btn.place(x=350,y=550)
        sev_btn = self.gameButton("Quiz 7", self.Quizz7)
        sev_btn.place(x=575,y=550)
        eig_btn = self.gameButton("Quiz 8", self.Quizz8)
        eig_btn.place(x=800,y=550)
        nine_btn = self.gameButton("Quiz 9", self.Quizz9)
        nine_btn.place(x=1025,y=550)
        ten_btn = self.gameButton("Quiz 10", self.Quizz10)
        ten_btn.place(x=1250,y=550)
        back_btn = tk.Button(master=window,text = "<-", command = self.back,width = 5,height=1,bg = "gray1",font= 'Impact 17',fg =  "white")
        back_btn.place(x=1700,y=50)
        
        
    def gameButton(self, name, command):
        return tk.Button(master=window,text = name, command = command,width = 20,height=10,bg = "light slate gray",font= 'Impact 17',fg =  "white")
        
    
    def quizzRun(self):
        self.score = 0
        self.num = 2
        for widget in window.winfo_children():
            widget.destroy()
        if len(self.quizz) == 1:
            title = tk.Label(master=window,text = "Sorry the quiz is empty choose another or go to create to make a new one!",fg = "gray13", font= 'Impact 17',bg = self.bg)
            title.place(x=700,y=100)
            back_btn = tk.Button(master=window,text = "->", command = self.homeQuizz,width = 70,height=15,bg = "gray1",font= 'Impact 17',fg =  "white")
            back_btn.place(x=700,y=400)
        else:   
            title = tk.Label(master=window,text = self.quizz[0],fg = "gray13", font= 'Impact 45',bg = self.bg)
            title.place(x=800,y=100)
            title = tk.Label(master=window,text =("By" , self.quizz[1]),fg = "gray13", font= 'Impact 25',bg = self.bg)
            title.place(x=800,y=200)
            back_btn = tk.Button(master=window,text = "->", command = self.gameStart,width = 70,height=15,bg = "gray1",font= 'Impact 17',fg =  "white")
            back_btn.place(x=700,y=400)
            back_btn = tk.Button(master=window,text = "<-", command = self.groupButtons ,width = 5,height=1,bg = "gray1",font= 'Impact 17',fg =  "white")
            back_btn.place(x=1700,y=50)
        
    
    def gameStart(self):
        for widget in window.winfo_children():
            widget.destroy()
        title = tk.Label(master=window,text = ("True Or False, " + self.quizz[self.num]),fg = "gray13", font= 'Impact 35',bg = self.bg)
        title.place(x=600,y=100)
        self.num = self.num + 1
        game.game_buttons()
        
    def con(self):
        if self.num == (len(self.quizz)-1):
            for widget in window.winfo_children():
                widget.destroy()
                game.highRead()
            if self.highscore > self.score:
                text = ("Quiz over, You got " + str(self.score) + "/"+ str(self.q + 1))
                text2 = ("High Score " + str(self.highscore) +"/"+ str(self.q + 1) )
                title = tk.Label(master=window,text = (text),fg = "gray13", font= 'Impact 35',bg = self.bg)
                title.place(x=600,y=100)
                title = tk.Label(master=window,text = (text2),fg = "gray13", font= 'Impact 35',bg = self.bg)
                title.place(x=600,y=300)
                back_btn = tk.Button(master=window,text = "->", command = self.homeQuizz,width = 70,height=15,bg = "gray1",font= 'Impact 17',fg =  "white")
                back_btn.place(x=700,y=400)
            else:
                text = ("Quiz over, You got " + str(self.score) + "/"+ str(self.q + 1)) 
                title = tk.Label(master=window,text = (text),fg = "gray13", font= 'Impact 35',bg = self.bg)
                title.place(x=600,y=100)
                title = tk.Label(master=window,text = ("New High Score"),fg = "gray13", font= 'Impact 20',bg = self.bg)
                title.place(x=600,y=300)
                back_btn = tk.Button(master=window,text = "->", command = self.homeQuizz,width = 70,height=15,bg = "gray1",font= 'Impact 17',fg =  "white")
                back_btn.place(x=700,y=400)
            self.highWrite()
            self.q = 0
        elif self.num % 2 == 0:
            self.gameStart()
            self.q = self.q + 1
        else:
            self.scoreAndisplay()
            
            
    def Run(self):
        if self.modechoice == "play":
            self.quizzRun()
        else:
            self.whatTask()
        
    def scoreAndisplay(self):
        for widget in window.winfo_children():
            widget.destroy()
        if self.ans == self.quizz[self.num]:
            self.score = self.score + 1
            title = tk.Label(master=window,text ="Corect ! :)",fg = "gray13", font= 'Impact 35',bg = self.bg)
            title.place(x=600,y=200)
            back_btn = tk.Button(master=window,text = "->", command = self.con,width = 70,height=15,bg = "gray1",font= 'Impact 17',fg =  "white")
            back_btn.place(x=700,y=400)
            self.num = self.num + 1
        else:
            title = tk.Label(master=window,text ="Incorect ! :(",fg = "gray13", font= 'Impact 35',bg = self.bg)
            title.place(x=600,y=200)
            back_btn = tk.Button(master=window,text = "->", command = self.con,width = 70,height=15,bg = "gray1",font= 'Impact 17',fg =  "white")
            back_btn.place(x=700,y=400)
            self.num = self.num + 1
    

        
    def createEdit(self):
        self.modechoice = "edit"
        game.groupButtons()
    
    def whatTask(self):
        self.x = len(self.quizz) - 1
        for widget in window.winfo_children():
            widget.destroy()
        if len(self.quizz) != 1:
            edit_btn = tk.Button(master=window,text = "Edit", command = self.editQuizz,width = 45,height=20,bg = "green",font= 'Impact 20',fg =  "white")
            edit_btn.place(x=350,y=150)
            delete_btn = tk.Button(master=window,text = "Delete", command = self.deleteFile,width = 45,height=20,bg = "red",font= 'Impact 20',fg =  "white")
            delete_btn.place(x=1150,y=150)
            back_btn = tk.Button(master=window,text = "<-", command = self.createEdit,width = 5,height=1,bg = "gray1",font= 'Impact 17',fg =  "white")
            back_btn.place(x=1700,y=50)
        else:
            self.createNew()
            

    def deleteFile(self):
        open(self.dirs[self.qnum], 'w').close()
        self.createEdit()
       
    def editQuizz(self):
        self.task = "edit"
        for widget in window.winfo_children():
            widget.destroy()
        back_btn = tk.Button(master=window,text = "<- ", command = self.createEdit,width = 7,height=1,bg = "gray1",font= 'Impact 20',fg =  "white")
        back_btn.place(x=1700,y=50)
        if self.x % 2 == 0:
            title = tk.Label(master=window,text =("Question " + str(self.x // 2)),fg = "gray13", font= 'Impact 45',bg = self.bg)
            title.place(x=825,y=200)
            title = tk.Label(master=window,text =("True Or False, "),fg = "gray13", font= 'Impact 25',bg = self.bg)
            title.place(x=225,y=300)
        else:
            title = tk.Label(master=window,text =("Question " + str(self.x // 2) , " Answer"),fg = "gray13", font= 'Impact 35',bg = self.bg)
            title.place(x=800,y=200)
        self.entry = tk.Entry(master=window,width = 70,fg = "gray13", font= 'Impact 25')
        button= tk.Button(window, text="Enter", command= self.get_value,width = 50,height=10,bg = "gray1",font= 'Impact 17',fg =  "white")
        button.place(x=700,y=500)
        self.entry.place(x=450,y=300)


    def false(self):
        self.ans = "false"
        self.con()
        
    def true(self):
        self.ans = "true"
        self.con()
            
    def game_buttons(self):
        true_btn = tk.Button(master=window,text = "True", command = self.true,width = 45,height=20,bg = "green",font= 'Impact 17',fg =  "white")
        true_btn.place(x=450,y=200)

        false_btn = tk.Button(master=window,text = "False", command = self.false,width = 45,height=20,bg = "red",font= 'Impact 17',fg =  "white")
        false_btn.place(x=1150,y=200)
        
        back_btn = tk.Button(master=window,text = "<-", command = self.homeQuizz,width = 5,height=1,bg = "gray1",font= 'Impact 17',fg =  "white")
        back_btn.place(x=1700,y=50)
            
        
    def createNew(self):
        self.x = 0 
        for widget in window.winfo_children():
            widget.destroy()
        title = tk.Label(master=window,text ="Create your new True or false Quiz",fg = "gray13", font= 'Impact 45',bg = self.bg)
        title.place(x=520,y=200)
        back_btn = tk.Button(master=window,text = "<-", command = self.createEdit,width = 5,height=1,bg = "gray1",font= 'Impact 17',fg = "white")
        back_btn.place(x=1700,y=50)
        next_btn = tk.Button(master=window,text = "->", command = self.creationStation,width = 30,height=5,bg = "gray1",font= 'Impact 35',fg =  "white")
        next_btn.place(x=600,y=500)
        self.questionList = ["Whats The Name Of Your Quiz? :","Whats the creator name :","q1 :","q1 answer :","q2 :","q2 answer :","q3 : ","q3 answer :","q4 :","q4 answer :","q5 :","q5 answer :"]
       
       
    def creationStation(self):
        self.task = "create"
        for widget in window.winfo_children():
            widget.destroy()
        if self.x != 12:
            back_btn = tk.Button(master=window,text = "<- Abort", command = self.deleteFile,width = 7,height=1,bg = "gray1",font= 'Impact 17',fg =  "white")
            back_btn.place(x=1700,y=50)
            title = tk.Label(master=window,text =self.questionList[self.x],fg = "gray13", font= 'Impact 35',bg = self.bg)
            title.place(x=700,y=200)
            self.entry = tk.Entry(master=window,width = 70,fg = "gray13", font= 'Impact 25')
            button= tk.Button(window, text="Enter", command= self.get_value,width = 50,height=10,bg = "gray1",font= 'Impact 17',fg =  "white")
            button.place(x=700,y=500)
            self.entry.place(x=425,y=300)
        else:
            title = tk.Label(master=window,text ="Your Quiz Has Been Created",fg = "gray13", font= 'Impact 17',bg = self.bg)
            title.place(x=800,y=200)
            back_btn = tk.Button(master=window,text = "<-", command = self.createEdit,width = 5,height=1,bg = "gray1",font= 'Impact 17',fg =  "white")
            back_btn.place(x=1700,y=50)
            
            
    def get_value(self):
       self.input=self.entry.get()
       self.x = self.x + 1
       self.addFile()
    
    
    
    def addFile(self):
        file = open(self.dirs[self.qnum], 'a')
        file.write(self.input + ",")
        file.close()
        if self.task == "edit":
            self.editQuizz()
        else:
            self.creationStation()
        
        
    def highWrite(self):
        file = open(self.dirs[self.qnum + 10], 'a')
        file.write(str(self.score) + ",")
        file.close()
 
    def highRead(self):
        high = 0
        for x in range(0,(len(self.quizzScores) - 1)):
            if int(self.quizzScores[x]) > int(high):
                high =  self.quizzScores[x]
        
        self.highscore = int(high)
            
            
        
        
     
        


game = quizz()
game.file_manger()
game.choice()