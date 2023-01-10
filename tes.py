import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from PIL import Image, ImageTk
from ttkbootstrap.toast import ToastNotification

class App:
    def __init__(self):

        self.app = ttk.Window()
        colors = self.app.style.colors

        coldata = [
            {"text": "LicenseNumber", "stretch": False},
            "CompanyName",
            {"text": "UserCount", "stretch": False},
        ]

        rowdata = [
            ('A123', 'IzzyCo', 12),
            ('A136', 'Kimdee Inc.', 45),
            ('A158', 'Farmadding Co.', 36)
        ]


        self.dt = Tableview(
            master=self.app,
            coldata=coldata,
            rowdata=rowdata,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(colors.light, None),
        )
        

        self.dt.view.bind( "<Double-1>" , self.onSelect)

        #print(dt.view.index)


        self.dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        toast = ToastNotification(
            title="ttkbootstrap toast message",
            message="This is a toast message",
            duration=3000,
        )
        toast.show_toast()

        self.app.mainloop()

    def onSelect(self , event):
        item = self.dt.view.selection()
        print(self.dt.view.item(item[0] , 'values'))
        for i in item:
            print("you clicked on", self.dt.view.item(i, "values")[0])


app = App()