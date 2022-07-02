from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import numpy as np
from PIL import Image, ImageTk
import imutils
from PIL import Image
from uritemplate import partial
class Application(tk.Frame):
    

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.img=cv2.imread('raptorClaro.jpg',1)
       
        self.__createWidgets()
    
    def __createWidgets(self):
        self.window=tk.Frame(self)
        self.window.grid(row=0,column=0)
        self.picture=Label(self.window)
        self.picture.grid(row=0,column=0,pady=2)
        self.scaladorPlus = Scale(self.window, from_=0,tickinterval=1,resolution=0.2,length=300,showvalue=0, to=10,orient=HORIZONTAL, label="alpha",command=self.__histEcu)
        self.scaladorPlus.grid(row=1,column=0,pady=2)
        
        self.__histEcu(5)
    def __histEcu(self,int):
        
        grid=(5,5)
        alpha=float(self.scaladorPlus.get())
        

        if alpha!=0:
            


            img=cv2.cvtColor(self.img, cv2.COLOR_BGR2LAB)
            L,A,B=cv2.split(img)
            clahe = cv2.createCLAHE(clipLimit=alpha, tileGridSize=grid)
            cl = clahe.apply(L)
            img = cv2.merge((cl,A,B))
            img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
            print('hello')
        else:
            img=self.img
            
        img=cv2.resize(img,(300,300))
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img=Image.fromarray(img)
        myimg=ImageTk.PhotoImage(image=img)
        self.picture.configure(image=myimg)
        self.picture.image=myimg
        
    
    

root=tk.Tk()
root.title('Ejemplo para graduar el contraste')

with_val=root.winfo_screenwidth()
height_val=root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(with_val/2,height_val/2))
app = Application(master=root)
app.mainloop()
