import tkinter
class Opening:
    def __init__(self) -> None:
        self.wnd=tkinter.Tk()
        self.wnd.geometry("1024x1024")
        self.canvas=tkinter.Canvas()
        self.canvas.place(x=0,y=0,width=100,height=61)
        pass

Opening().wnd.mainloop()