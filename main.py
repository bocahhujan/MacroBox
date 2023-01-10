import json
import time
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from tkinter import filedialog as fd

from window.createjobs import createjob
from remote import perangkat
from remote.runtaks import runTaks


class winmain:
    def __init__(self):
        self.de = perangkat()
        self.li = self.de.list()
        self.file_url = ""
        self._taks = any 
        self.status = 'start'
        print(self.li)
        #klik(100 , 100)
        #d.keyevent('volume up')

        #pilimg = d.screenshot()
        #time.sleep(5) 
        #pilimg.save("tmp/screenshot.jpg")

        # create main window (parent window)
        #win = tk.Tk()
        self.win = ttk.Window(themename="cosmo")
        #win.theme_use('aqua')
        self.win.geometry("450x650")
        self.win.resizable(False, False)
        self.win.title('Device Farm Controller')

        # Label() it display box
        # where you can put any text. 

        frm = ttk.Frame(self.win, padding=10 )
        frm.grid()

        txt = ttk.Label(frm,
                    text="DEVICES")
        #txt.pack(pady=30, ipadx=20)
        txt.grid(column=0, row=0, padx=10, pady=10,  sticky='w')

        # pack() It organizes the widgets
        # in blocks before placing in the parent widget.
        self.combobox = ttk.Combobox(frm,state= "readonly" , bootstyle = 'success')
        self.combobox['values'] = self.li
        #combobox.current(2)
        #combobox.pack(pady=30, ipadx=10)
        self.combobox.grid(column=1, row=0, padx=10, pady=10,  sticky='w')

        #fram combo
        self.framlbel = ttk.Labelframe( frm ,  text="Device")
        self.framlbel.grid(row=1, column=0,  padx=10, pady=10, columnspan=3, sticky="w")

        self.title_name = ttk.Label( self.framlbel   , text="Name")
        self.title_name.grid(column=1, row=0, padx=5, pady=5 , sticky='w')

        self.title_model = ttk.Label( self.framlbel   , text="Model")
        self.title_model.grid(column=1, row=1, padx=5, pady=5 , sticky='w')

        self.title_device = ttk.Label( self.framlbel   , text="Serial")
        self.title_device.grid(column=1, row=2, padx=5, pady=5 , sticky='w')

        self.text_name = ttk.Label( self.framlbel   , text=":")
        self.text_name.grid(column=2, row=0, padx=5, pady=5 , sticky='w' , columnspan=2)

        self.text_model = ttk.Label( self.framlbel   , text=":")
        self.text_model.grid(column=2, row=1, padx=5, pady=5 , sticky='w' , columnspan=2)

        self.text_device = ttk.Label( self.framlbel   , text=":")
        self.text_device.grid(column=2, row=2, padx=5, pady=5 , sticky='w' , columnspan=2)



        self.btn_load = ttk.Button(self.framlbel, text='LOAD JOB' , command = self.load_data)
        self.btn_load.grid(column=1, row=3, padx=10, pady=10 , sticky='w')

        self.btn_start = ttk.Button(self.framlbel, text='START' , bootstyle="success" , command= self.startbtn )
        self.btn_start.grid(column=2, row=3, padx=10, pady=10 ,   sticky='w')

        self.btn_stop = ttk.Button(self.framlbel, text='STOP' , bootstyle="danger" , command= self.stopbtn)
        self.btn_stop.grid(column=3, row=3,  padx=10, pady=10 , sticky='w' )

        self.btn_create = ttk.Button(self.framlbel, text='CREATE TASK' ,   bootstyle="info" , command= self.create_job )
        self.btn_create.grid(column=4, row=3, padx=10, pady=10 , sticky='w')



       

        framllog = ttk.Labelframe( frm ,  text="Log Job")
        framllog.grid(row=2, column=0,  padx=10, pady=10, columnspan=3, sticky="w")

        self.title_taks = ttk.Label( framllog   , text="Taks File :")
        self.title_taks.grid(column=1, row=0, padx=5, pady=5 , sticky='w')


        scrolly = ttk.Scrollbar(framllog )
        scrolly.grid(column=2 , row = 1 , sticky=N+S+W)

        self.text_log = ttk.Text(framllog, state='disabled', width=48, height=15 , yscrollcommand = scrolly.set)
        self.text_log.grid(column=1, row=1, padx=5, pady=5 , sticky='w')


        scrolly.config(command = self.text_log.yview)


        for child in self.framlbel.winfo_children():
            child.configure(state='disable')

        btn = ttk.Button(frm, text='CONNECT' , command=self.submit)
        btn.grid(column=2, row=0, padx=10, pady=10,  sticky='w')

        self.win.position_center()
        self.win.deiconify()

        # running the main loop
        self.win.mainloop()

    def load_data(self):
        #de.klik(100,100) 
        filetypes = (
            ('text files', '*.json'),
            #('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        if(filename):
            self.file_url = filename
            self.title_taks.config(text = f"File Taks : {filename}")
            self.btn_start.config(state="enable")
            Messagebox.show_info( f"File Name {filename} " , "Select File") 
        else:
            Messagebox.show_error("File Not Selected , Please select File" , "No Selected")

    def create_job(self):
        subFrame = createjob(self.win , self.de)
        print(subFrame)
        #handler = lambda: win.onCloseOtherFrame(subFrame)

    def startbtn(self):
        self.btn_create.config(state="disable")
        self.btn_load.config(state="disable")
        self.btn_start.config(state="disable")
        self.btn_stop.config(state="enable")
        self.run_taks()

    def run_taks(self):
        file_open = open(self.file_url)
        json_taks = json.load(file_open)
        print(json_taks)
        self._taks = runTaks(self.de , self.win , self.text_log)
        i = 1
        self.status = "start"
        while self.status == 'start':
            print('start')
            self._taks._taks = {'type': 'log' , 'value': f'Loop Number {i}'}
            self._taks.run()

            for t in json_taks:
                self._taks._taks = t
                self._taks.run()
            
            i += 1
            time.sleep(1)
            

    def stopbtn(self):
        self.btn_create.config(state="enable")
        self.btn_load.config(state="enable")
        self.btn_start.config(state="enable")
        self.btn_stop.config(state="disable")
        #print(self._taks.i)
        self.status = "stop"
        self.win.update()

    def submit(self):
        cmb_val = self.combobox.get()
        if(cmb_val):
            self.de.connect(cmb_val)
            self.text_device.config(text= f": {cmb_val}" )
            self.text_model.config(text= f": {self.de.d.prop.model}" )
            self.text_name.config(text= f": {self.de.d.prop.name }")

            for child in self.framlbel.winfo_children():
                if((child['text'] != 'STOP') and (child['text'] != 'START') ):
                    print(child['text'])
                    child.configure(state='enable')
            #framlbel.grid(row=1, column=0,  padx=10, pady=10, columnspan=3, sticky="nsew")
            #Messagebox.show_info( f"Your Select Devices id {cmb_val} " , "Select Device") 
        else:
            Messagebox.show_error("Device Not Selected , Please select device in combobox" , "No Selected")



app = winmain()