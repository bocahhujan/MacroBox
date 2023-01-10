import time
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.tableview import Tableview
from tkinter import filedialog as fd
import json
from window.imageclick import imageClick
from window.addtext import addText
from window.adddelay import addDelay
from window.addkeyevent import addKeyEvent

class createjob(ttk.Toplevel):
    def __init__(self, original , perangkat):
        self.original_frame = original
        self.colors = original.style.colors
        self.oriigin = original
        self.oriigin.withdraw()
        self.perangkat = perangkat
        ttk.Toplevel.__init__(self)
        
        self.title("Create a Task")
        #self.position_center()
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.onClose)

        p_x = self.oriigin.winfo_x()
        p_y = self.oriigin.winfo_y()
        print(p_x , "x", p_y)
        self.geometry(f"+{p_x}+{p_y}")

        frame = ttk.Frame(master=self, border=1)
        frame.pack(side="top", fill="x")
       
        menubtn = ttk.Menubutton( frame, text="ADD" , bootstyle="outline")
        menubtn.menu = ttk.Menu(menubtn)
        menubtn["menu"]= menubtn.menu
        menubtn.menu.add_command(label="Click" , command=self.addButton ) 
        menubtn.menu.add_command(label="Input Text" , command=self.addText )
        menubtn.menu.add_command(label="Key Event" , command=self.addkeyevent )
        menubtn.menu.add_separator()
        menubtn.menu.add_command(label="Delay" , command=self.addDelay) 
        
        menubtn.pack( padx=10, pady=10  , side = RIGHT)

    

        self.coldata = [
            {"text": "TYPE", "stretch": False},
            {"text": "VALUE", "stretch": False}
        ]

        self.rowdata = [
            ('A123', 'IzzyCo', 12),
            ('A136', 'Kimdee Inc.', 45),
        ]

        self.dt = Tableview(
            master=self,
            coldata=self.coldata,
            #rowdata=self.rowdata,
            paginated=True,
            searchable=False,
            #sorted = False,
            bootstyle=PRIMARY,
            height = 25 ,
            pagesize = 25 , 
            stripecolor=(self.colors.light, None),
        )
        self.dt._sorted = FALSE
        
        self.dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        frm_btn = ttk.Frame(master=self, border=1)
        frm_btn.pack(side="bottom", fill="x")

        btn = ttk.Button(frm_btn, text="SAVE", command=self.saveFile , bootstyle="success" )
        btn.pack( padx=10, pady=10 ,side = RIGHT)

        btn_cancel = ttk.Button(frm_btn, text="CANCEL", command=self.onClose , bootstyle="danger" )
        btn_cancel.pack( padx=10, pady=10 ,side = RIGHT)

        
       
    def saveFile(self):
        #self.wait_window()
        print('save fale')
        data_tb = self.dt.tablerows
        if(len(data_tb) > 0 ):
            data_tb = self.prosesData(data_tb)
            print(data_tb)
            f = fd.asksaveasfile(mode='w', defaultextension=".json")
            if f :
                f.write(data_tb)
                f.close()
                self.grab_release()
                self.destroy()
                self.oriigin.deiconify()
            else:
                Messagebox.show_error("File Not Selected , Please select File" , "No Selected")
        else:
            Messagebox.show_error("Not Taks to save , Pleace Check Again !" , "No Taks")


    
    def prosesData(self , data):
        lst = []
        for x in data:
            #print(x.values)
            item = x.values
            print(item[1]);
            
            if item[0] == 'click':
                item_val = json.loads(item[1])
            else:
                item_val = item[1]

            itms = {
                'type' : item[0] ,
                'value': item_val
            }
            lst.append(itms)
        
        return json.dumps(lst)


    def onClose(self):
        #self.dt.save_data_to_csv()
        print('close dialog')
        #self.saveFile
        self.grab_release()
        self.destroy()
        self.oriigin.deiconify()
        #self.original_frame.show()
    
    def addButton(self): 
        try:
            pilimg = self.perangkat.screenshot()
            print(pilimg)
            clik = imageClick(self)
            print(clik.x , clik.y)
            
            if( (int(clik.x) != 0 ) & (int(clik.y) != 0) ):
                d_j = json.dumps({
                    'x' : clik.x ,
                    'y' : clik.y
                })
                
                self.dt.insert_row('end', ['click', d_j])
                self.dt.load_table_data()
            else:
                print('cordinat 0')
        except :
            Messagebox.show_error( "Failed Screen Shoot , Please Tray Again " , "Screen Shoot")
            print("Scren Error");
            
            
        print('add button')

    def addText(self):
        txt = addText(self)
        print(txt.text)
        if(txt.text):
            self.dt.insert_row('end', ['text', txt.text])
            self.dt.load_table_data()

    def addDelay(self):
        txt = addDelay(self)
        if txt.text:
            self.dt.insert_row('end', ['delay', txt.text])
            self.dt.load_table_data()

    def addkeyevent(self):
        txt = addKeyEvent(self)
        if txt.text:
            self.dt.insert_row('end', ['keyevent', txt.text])
            self.dt.load_table_data()

   
        