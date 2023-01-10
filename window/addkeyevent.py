import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

class addKeyEvent(ttk.Toplevel):
    def __init__(self, original):
        self.original_frame = original
        self.colors = original.style.colors
        ttk.Toplevel.__init__(self)
        self.title("Input Key Event")
        self.position_center()
        self.grab_set()
        self.text = ""
        self.combobox = ttk.Combobox(self,state= "readonly" , bootstyle = 'success')
        self.combobox['values'] = ['ENTER' ,  'HOME'  , 'BACK']
        self.combobox.current(1)
        self.combobox.pack(fill=BOTH, expand=YES, padx=10, pady=5 )

        frm_btn = ttk.Frame(master=self, border=1)
        frm_btn.pack(side="bottom", fill="x")
      

        btn = ttk.Button(frm_btn, text="SAVE", command=self.saveClick , bootstyle="success" )
        btn.pack( padx=10, pady=5 ,side = RIGHT)

        btn_c = ttk.Button(frm_btn, text="CANCEL", command=lambda:self.destroy() , bootstyle="danger" )
        btn_c.pack( padx=10, pady=5 ,side = RIGHT)

        self.wait_window() 
    

    def saveClick( self ):
        if(self.combobox.get()):
            self.text = self.combobox.get()
            self.grab_release()
            self.destroy()
        else:
            Messagebox.show_error("Not Text To Save , Pleace Check Again !" , "No Texts")

