import tkinter
from tkinter import messagebox
from main import main
from corpus_info import TextOverview
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
        self.entryText.place(x=0,y=0,width=600,height=480)
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
        main().__main__(text)
        messagebox.showinfo('Success','check you question in file question.txt')
    def corpus_info(self):
        text=self.entryText.get(1.0,tkinter.END)
        TextOverview(text)
    def return_main(self):
        self.question_screen.destroy()
        mainscreen()
class AnswerFrame:
    def __init__(self) -> None:
        self.question_screen=tkinter.Tk()
        self.question_screen.resizable(0,0)
        self.question_screen.title('Answer my questions, mortal!!')
        self.question_screen['height']=480
        self.question_screen['width']=720
        self.questionList=self.process('question.txt')
    def process(self,txt):
        file=open(txt,'r')
        file.read
        
class questionaAnswerPair:
    def __init__(self,question,answer,loc) -> None:
        self.question=question
        self.answer=answer
        self.loc=loc

mainscreen()