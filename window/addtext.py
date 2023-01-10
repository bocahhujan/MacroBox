import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

class addText(ttk.Toplevel):
    def __init__(self, original):
        self.original_frame = original
        self.colors = original.style.colors
        ttk.Toplevel.__init__(self)
        self.title("Input Text")
        self.position_center()
        self.grab_set()
        self.text = ""
        self.txt_box = ttk.Text(self , height=6 , width=50)
        self.txt_box.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        
        frm_btn = ttk.Frame(master=self, border=1)
        frm_btn.pack(side="bottom", fill="x")

        btn = ttk.Button(frm_btn, text="SAVE", command=self.saveClick , bootstyle="success" )
        btn.pack( padx=10, pady=10 ,side = RIGHT)

        btn_c = ttk.Button(frm_btn, text="CANCEL", command=lambda:self.destroy() , bootstyle="danger" )
        btn_c.pack( padx=10, pady=10 ,side = RIGHT)

        self.wait_window() 
        
    
    def saveClick( self ):
        print(self.txt_box.get("1.0","end-1c"))
        if(self.txt_box.get("1.0",END)):
            self.text = self.txt_box.get("1.0",END)
            self.grab_release()
            self.destroy()
        else:
            Messagebox.show_error("Not Text To Save , Pleace Check Again !" , "No Texts")

