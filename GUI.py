import tkinter
from tkinter import messagebox
from main import main
from corpus_info import TextOverview
import os
import time
class mainscreen:
    def __init__(self) -> None:
        self.screen=tkinter.Tk()
        self.screen.title('Who wants to be a billionare!!')
        self.screen['height']=480
        self.screen['width']=720
        self.screen.resizable(0,0)
        self.button1=tkinter.Button(text='I want to ask questions',command=self.questionFrame)
        self.button1.place(x=0,y=0,width=720,height=240)
        self.button2=tkinter.Button(text='I want to answer questions',command=self.answerFrame)
        self.button2.place(x=0,y=240,width=720,height=240)
        self.screen.mainloop()
    def questionFrame(self):
        self.screen.destroy()
        questionFrame()
    def answerFrame(self):
        a=messagebox.askyesno('confirm','are you sure? ')
        if a:
            AnswerFrame()

class questionFrame:
    def __init__(self):
        self.question_screen=tkinter.Tk()
        self.question_screen.resizable(0,0)
        self.question_screen.title('make your own questions!')
        self.question_screen['height']=480
        self.question_screen['width']=720
        self.entryText=tkinter.Text(self.question_screen,width=600)
        self.entryText.place(x=0,y=80,width=600,height=400)
        self.entryText1=tkinter.Text(self.question_screen,width=600)
        self.entryText1.place(x=0,y=0,width=600,height=80)
        self.button4= tkinter.Button(self.question_screen,text='Generate',command=self.runMainFunction)
        self.button4.place(x=600,y=0,width=120,height=160)
        self.button5=tkinter.Button(self.question_screen,text='corpus info',command=self.corpus_info)
        self.button5.place(x=600,y=160,width=120,height=160)
        self.button6=tkinter.Button(self.question_screen,text='return',command=self.return_main)
        self.button6.place(x=600,y=320,width=120,height=160)
        self.question_screen.bind('<Return>',self.runMainFunction)
        self.question_screen.mainloop()
    def runMainFunction(self,*args):
        text=self.entryText.get(1.0,tkinter.END)
        filename=self.entryText1.get(1.0,tkinter.END)
        filename=filename.replace('\n','')
        if filename=='':
            filename='question'
        print(filename)
        while self.checkRepeat(filename+'.txt'):
            i=0
            filename+=str(i)
            i+=1
        main().__main__(text,filename)
        messagebox.showinfo('Success',f'check you question in file {filename}.txt')
    def corpus_info(self):
        text=self.entryText.get(1.0,tkinter.END)
        TextOverview(text)
    def return_main(self):
        self.question_screen.destroy()
        mainscreen()
    def checkRepeat(self,filename):
        list_directory = os.listdir('.')
        filelists = []
        for directory in list_directory:
            if(os.path.isfile(directory)):
                filelists.append(directory)
        if filename in filelists:
            return True
        return False

class AnswerFrame:
    def __init__(self) -> None:
        self.question_screen=tkinter.Tk()
        self.question_screen.resizable(0,0)
        self.question_screen.title('Answer my questions, mortal!!')
        self.question_screen['height']=480
        self.question_screen['width']=720
        self.listbox1=tkinter.Listbox(self.question_screen)
        self.listbox1.place(x=0,y=0,height=400,width=720)
        self.button1=tkinter.Button(self.question_screen,text="Let's GOOOOO!!!",command=self.openChallenge)
        self.button1.place(x=0,y=400,height=100,width=720)
        self.questionlst=self.getFilelist('-q')
        for i in range(len(self.questionlst)):
            self.listbox1.insert(tkinter.END,self.questionlst[i])
        self.questionset={}
        for files in self.questionlst:
            text=open(files,'r').readlines()
            for j in range(len(text)):
                text[j]=text[j].split('\t')
            self.questionset[files]=text
        
    def getFilelist(self,tar):
        list_directory = os.listdir('.')
        filelists = []
        for directory in list_directory:
            if(os.path.isfile(directory)and tar in directory):
                filelists.append(directory)
        return filelists
    
    def openChallenge(self,*args):
        filename=self.listbox1.get('active')
        filename=filename.replace('-q','-t')
        self.question_screen.destroy()
        TextFrame(filename,self.questionset)

class TextFrame():
    def __init__(self,file,question) -> None:
        self.textFrame=tkinter.Tk()
        self.textFrame.resizable(0,0)
        self.textFrame.title('Read!!!')
        self.textFrame['height']=480
        self.textFrame['width']=720
        self.listbox1=tkinter.Listbox(self.textFrame)
        self.listbox1.place(x=0,y=0,height=480,width=720)
        self.text=open(file,'r').readlines()
        for i in range(len(self.text)):
            self.text[i]=self.text[i].split('\t')
        for i in self.text:
            self.listbox1.insert(tkinter.END,i[0])
        self.time=5
        self.countdown()
        self.file=file.replace('-t','-q')
        WhowantsToBeAMillionaire(question[self.file])

    def countdown(self):
        for i in range(self.time):
            self.time-=1
            self.textFrame.update()
            time.sleep(1)
        self.textFrame.destroy()

class WhowantsToBeAMillionaire:
    def __init__(self,questionlst):
        self.questionAnswering=tkinter.Tk()
        self.questionAnswering.resizable(0,0)
        self.questionAnswering.title('')
        self.questionAnswering['height']=480
        self.questionAnswering['width']=720
        self.question=tkinter.Label(self.questionAnswering,text=questionlst[0][0])
        self.question.place(x=0,y=80,width=720,height=400)
        self.entryText1=tkinter.Text(self.questionAnswering,width=720)
        self.entryText1.place(x=0,y=0,width=720,height=80)

        
        
        


mainscreen()