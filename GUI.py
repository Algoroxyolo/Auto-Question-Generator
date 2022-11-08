import tkinter
import tkinter.ttk
from tkinter import messagebox
from main import main
from corpus_info import TextOverview
import os
import time
import pyaudio
import wave
import speech_recognition as sr
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
    '''
        This is the widget where you generate questions.
    '''
    def __init__(self):
        self.question_screen=tkinter.Tk()
        self.question_screen.resizable(0,0)
        self.question_screen.title('make your own questions!')
        self.question_screen['height']=480
        self.question_screen['width']=720
        self.Text=tkinter.Text(self.question_screen,width=600)
        self.Text.place(x=0,y=80,width=600,height=400)
        self.title=tkinter.Text(self.question_screen,width=600)
        self.title.place(x=0,y=0,width=600,height=80)
        self.generateButton= tkinter.Button(self.question_screen,text='Generate',command=self.runMainFunction)
        self.generateButton.place(x=600,y=0,width=120,height=120)
        self.corpusInfo=tkinter.Button(self.question_screen,text='corpus info',command=self.corpus_info)
        self.corpusInfo.place(x=600,y=120,width=120,height=120)
        self.audio=tkinter.Button(self.question_screen,text='Too lazy to type',command=self.audioToWord)
        self.audio.place(x=600,y=240,width=120,height=120)
        self.GoBack=tkinter.Button(self.question_screen,text='return',command=self.return_main)
        self.GoBack.place(x=600,y=360,width=120,height=120)
        self.question_screen.bind('<Return>',self.runMainFunction)
        self.question_screen.mainloop()
    '''
        This function runs the mainfunction which has a bunch of
        other functions as well, and create the text corpus file 
    '''
    def runMainFunction(self,*args):
        text=self.Text.get(1.0,tkinter.END)
        filename=self.title.get(1.0,tkinter.END)
        filename=filename.replace('\n','')
        if filename=='':
            filename='question'
        while self.checkRepeat(filename+'.txt'):
            i=0
            filename+=str(i)
            i+=1
        main().__main__(text,filename)
        messagebox.showinfo('Success',f'check you question in file {filename}.txt')
   
    def corpus_info(self):
        '''
            Gets important info for the text 
        '''
        text=self.Text.get(1.0,tkinter.END)
        TextOverview(text)
    
    def return_main(self):
        self.question_screen.destroy()
        mainscreen()
   
    def audioToWord(self):
        AudioScreen()
    
    def checkRepeat(self,filename):
        '''
            Check if the file is overwriting something or not
        '''
        list_directory = os.listdir('.')
        filelists = []
        for directory in list_directory:
            if(os.path.isfile(directory)):
                filelists.append(directory)
        if filename in filelists:
            return True
        return False
class AudioScreen:
    '''
        This is the widget where
        you record yourself and 
        gain the text version of what 
        you spoke
    '''
    def __init__(self) -> None:
        self.root=tkinter.Tk()
        self.root.resizable(0,0)
        self.root.title('Answer my questions, mortal!!')
        self.root['height']=240
        self.root['width']=240
        self.entryText=tkinter.Text(self.root,width=600)
        self.entryText.place(x=0,y=120,width=240,height=60)
        self.Audio2Text()
        self.returnButton=tkinter.Button(self.root,text="I'm sure",command=self.TurnBack)
        self.returnButton.place(x=0,y=180,width=120,height=60)
        self.returnButton=tkinter.Button(self.root,text="Go again",command=self.Audio2Text)
        self.returnButton.place(x=120,y=180,width=120,height=60)
    
    def TurnBack(self):
        self.entryText.clipboard_clear()
        self.entryText.clipboard_append(self.entryText.get(1.0,tkinter.END))
        self.root.destroy()

    def Audio2Text(self):
        self.progressbar=tkinter.ttk.Progressbar(self.root,length=240)
        self.progressbar['maximum']=100
        self.progressbar.place(x=0,y=80)
        self.entryText.delete(1.0,tkinter.END)
        self.entryText.insert('1.0',self.record_audio())
    def record_audio(self,wave_out_path="audio\output.wav",record_second=10):
        '''
            record audio and recognize the audio to text 
        '''
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16,channels=1,
                        rate=44100,input=True,
                        frames_per_buffer=1024)
        wf = wave.open(wave_out_path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        for i in (range(0, int(44100 / 1024 * record_second))):
            data = stream.read(1024)
            wf.writeframes(data)
            self.progressbar['value']=i/int(44100 / 1024 * record_second)*100
            self.root.update()
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf.close()
        r=sr.Recognizer()
        audio=sr.AudioFile('audio\output.wav')
        with audio as source:
            audio=r.record(source)
            return(r.recognize_google(audio))

class AnswerFrame:
    '''
        Get a list of question set allowing
        the user to choose from
    '''
    def __init__(self) -> None:
        self.question_screen=tkinter.Tk()
        self.question_screen.resizable(0,0)
        self.question_screen.title('Answer my questions, mortal!!')
        self.question_screen['height']=480
        self.question_screen['width']=720
        self.questionSet=tkinter.Listbox(self.question_screen)
        self.questionSet.place(x=0,y=0,height=400,width=720)
        self.start=tkinter.Button(self.question_screen,text="Let's GOOOOO!!!",command=self.openChallenge)
        self.start.place(x=0,y=400,height=100,width=720)
        self.questionlst=self.getFilelist()
        for i in range(len(self.questionlst)):
            self.questionSet.insert(tkinter.END,self.questionlst[i])
        self.questionset={}
        for files in self.questionlst:
            text=open(f'.\QuestionFile\{files}','r').readlines()
            for j in range(len(text)):
                text[j]=text[j].split('\t')
            self.questionset[files]=text
        
    def getFilelist(self):
        '''
            gets the file lists
        '''
        list_directory = os.listdir('.\QuestionFile')
        filelists = []
        for directory in list_directory:
            if('.txt'in directory):
                filelists.append(directory)
        return filelists
    
    def openChallenge(self,*args):
        '''
            Opens the text frame
        '''
        filename=self.questionSet.get('active')
        filename=filename.replace('-q','-t')
        self.question_screen.destroy()
        TextFrame(filename,self.questionset)

class TextFrame():
    '''
        The frame for text corpus. You will 
        have questions based on the text
    '''
    def __init__(self,file,question) -> None:
        self.textFrame=tkinter.Tk()
        self.textFrame.resizable(0,0)
        self.textFrame.title('Read!!!')
        self.textFrame['height']=480
        self.textFrame['width']=720
        self.textBox=tkinter.Listbox(self.textFrame)
        self.textBox.place(x=0,y=0,height=480,width=720)
        self.text=open(f'.\TextFile\{file}','r').readlines()
        for i in range(len(self.text)):
            self.text[i]=self.text[i].split('\t')
        for i in self.text:
            self.textBox.insert(tkinter.END,i[0])
        self.time=3
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
    """
        The widget for questions
        The user will be asked based on 
        what read a few seconds ago. 
    """
    def __init__(self,questionlst,score=0):
        self.questionAnswering=tkinter.Tk()
        self.questionAnswering.resizable(0,0)
        self.questionAnswering.title('')
        self.questionAnswering['height']=480
        self.questionAnswering['width']=720
        self.questionIndex=0
        self.attempt=3
        self.questionlst=questionlst
        self.question=tkinter.Label(self.questionAnswering,text=self.questionlst[self.questionIndex][0])
        self.question.place(x=0,y=0,width=720,height=300)
        self.answerInput=tkinter.Text(self.questionAnswering,width=720)
        self.answerInput.place(x=0,y=300,width=720,height=80)
        self.check=tkinter.Button(self.questionAnswering,text="Check Answer!!!",command=self.checkAnswer)
        self.check.place(x=0,y=380,height=100,width=720)
        self.score=score
    
    def checkAnswer(self,*args):
        '''
            Gets the answer
        '''
        answer=self.answerInput.get(1.0,tkinter.END)
        if answer==self.questionlst[self.questionIndex][2]:
            self.questionAnswering.destroy()
            if len(self.questionlst)>1:
                WhowantsToBeAMillionaire(self.questionlst[1:],self.score+1)
            else:
                EndFrame(self.score)
        else:
            self.score-=1
            if self.attempt>0:
                self.attempt-=1
            else:
                if len(self.questionlst)>1:
                    self.questionAnswering.destroy()
                    WhowantsToBeAMillionaire(self.questionlst[1:],self.score)
                else:
                    EndFrame(self.score)

class EndFrame:
    '''
        This Frame gave the score of the quiz
    '''
    def __init__(self,score) -> None:
        self.EndFrame=tkinter.Tk()
        self.EndFrame.resizable(0,0)
        self.EndFrame.title('your score!!')
        self.EndFrame['height']=480
        self.EndFrame['width']=720
        self.question=tkinter.Label(self.EndFrame,text='Your Score:'+str(score))
        self.question.place(x=0,y=0,width=720,height=300)
        self.goBack=tkinter.Button(self.EndFrame,text="Go Back",command=self.Goback)
        self.goBack.place(x=0,y=300,height=180,width=720)

    def Goback(self):
        self.EndFrame.destroy()
        AnswerFrame()
        
mainscreen()