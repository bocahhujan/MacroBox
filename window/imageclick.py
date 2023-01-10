from tkinter import * 
from PIL import Image, ImageTk
import ttkbootstrap as ttk

class imageClick(ttk.Toplevel):
    def __init__(self, original):
        self.original_frame = original
        self.colors = original.style.colors
        ttk.Toplevel.__init__(self)
        self.title("Create Click")
        self.position_center()
        self.grab_set()

        

        self.x = 0
        self.y = 0

        pil_img = Image.open('screenshot.jpg')
        img = ImageTk.PhotoImage(pil_img)

        #original_w = img.width()
        #original_h = img.height()

        img_w = img.width() / 100
        img_h = img.height() / 100

        img_w = img_w * 50
        img_h = img_h * 50
        print(img_w  ,  "x", img_h)
        pil_img2 = pil_img.resize((int(img_w), int(img_h)))

        img2 = ImageTk.PhotoImage(pil_img2)

        canv = Canvas(self, width=img_w, height=img_h)
        obj1 = canv.create_image(0,0,anchor=NW,image=img2)
        print(obj1)
        canv.tag_bind(obj1, '<Double-1>', self.onObjectClick)
        canv.pack()
        self.wait_window() 
        #hasil = { 'x': self.x , 'y' : self.y }
        #return hasil

    def onObjectClick( self , event):                  
        print ('Clicked', event.x * 2 , event.y * 2 )
        self.x = event.x * 2
        self.y = event.y * 2
        print ('Clicked', self.x  , self.y  )
        self.grab_release()
        self.destroy()