import time
import asyncio

class runTaks():
    def __init__(self , perangkat , wind, text_log):
        self.d = perangkat
        self._taks = any
        self.text = text_log
        self.wind = wind
        
    
    def log(self , text):
        self.text.configure(state='normal')
        self.text.insert('end', f'{text} \n')
        self.text.configure(state='disabled')
        self.wind.update()

    def run(self):
        
        if self._taks['type'] == 'log' :
            self.log(self._taks['value'])

        elif self._taks['type'] == 'click':
            val = self._taks['value']
            self.log(f"Click Taks to {val['x']} , {val['y']}")
            self.d.klik(val['x'] , val['y'])
            
        elif self._taks['type'] == 'delay' :
            self.log(f"Delay Taks {self._taks['value']} Second")
            time.sleep(int(self._taks['value']))
            
        elif self._taks['type'] == 'text':
            self.log(f"Input Text Taks : {self._taks['value']}")
            self.d.text(self._taks['value'])
            
        elif self._taks['type'] == 'keyevent':
            self.log(f"Input Key Event : {self._taks['value']}")
            self.d.keyevent(self._taks['value'])
           


