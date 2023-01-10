import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

class addDelay(ttk.Toplevel):
    def __init__(self, original):
        self.original_frame = original
        self.colors = original.style.colors
        ttk.Toplevel.__init__(self)
        self.title("Add Delay")
        self.position_center()
        self.grab_set()
        self.text = ""
        self.my_valid = self.register(self.validate)

        self.txt_box = ttk.Entry(self , validate='key',validatecommand=(self.my_valid,'%S') , width=6 )
        self.txt_box.insert(0 , 0)
        self.txt_box.grid(column=0, row=0, padx=10, pady=10 , sticky='w')
        
        label = ttk.Label(self , text="Second")
        label.grid(column=1, row=0, padx=5, pady=5 , sticky='w')

        btn = ttk.Button(self, text="SAVE", command=self.saveClick , bootstyle="success" )
        btn.grid(column=2, row=0, padx=10, pady=10 , sticky='w')

        self.wait_window() 
    
    def validate( self , u_input): # callback function
        return u_input.isdigit()
   

    def saveClick( self ):
        if(self.txt_box.get()): 
            self.text = self.txt_box.get()
            self.grab_release()
            self.destroy()
        else:
            Messagebox.show_error("Not Text To Save , Pleace Check Again !" , "No Texts")

