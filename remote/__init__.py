import time
from adbutils import adb

class perangkat():
    def __init__(self):
        self.d = ""

   

    def list(self):
        li = []
        div = adb.device_list()
        for dl in div:
            li.append(dl.serial)
        return li
        #return True

    def connect(self , d_id):
        self.d = adb.device(d_id)

        
    def klik(self , x,y):
        l = self.d.click(x,y)
        print(l)

    def text(self, text):
        l = self.d.send_keys(text)
        print(l)
        
    def keyevent(self, text):
        self.d.keyevent(text)

    def screenshot(self):
        pilimg = self.d.screenshot()
        #time.sleep(5)
        pilimg.save("screenshot.jpg")
        return pilimg
    
    def switch(self , sx , sy  , ex , ey,duration):
        self.d.switch(sx , sy  , ex , ey, duration)


