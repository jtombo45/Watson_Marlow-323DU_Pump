# import libraries for serial port and Tkinter GUI
import serial
import Tkinter as tk
import time

class WatsonSerial:
#here to set pump speed which opens a new dialog 
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        self.myLabel = tk.Label(top, text='Enter a 3 digit number for Speed')
        self.myLabel.pack()
        self.myEntryBox = tk.Entry(top)
        self.myEntryBox.pack()
        self.myEntryBox.focus_set() #set focus to the input box
        self.mySubmitButton = tk.Button(top, text='Set Speed', command=self.send)
        self.mySubmitButton.pack()
        self.top.bind("<Return>", self.send) #binding to the top level. pass param to send func
        
    def send(self, parent):
        self.speed = self.myEntryBox.get() #entrybox set var 
        self.top.destroy()

# Open serial port
ser = serial.Serial(
    port='COM1',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

# Create the root window
root = tk.Tk()
root.geometry('600x300+100+100')
root.title('Pump Command Sender')

                        #Commands                   keyboard key
input_go = '1GO'        #Pump start                 z
input_stop = '1ST'      #Pump stop                  x
input_drop = '1SD'      #Pump decrease 1rpm         c
input_up = '1SI'        #Pump increase 1rpm         v
input_rev = '1RC'       #Pump reverse direction     s
input_clockw = '1RR'    #Pump clockwise             d
input_counter = '1RL'   #Pump counterclockwise      f

# Create a keystroke handler
def key(event):
    if (event.char == 'q'):  #q exits program
        root.quit()
        ser.close()
        exit()
    elif (event.char == 'p'):  #p prompts dialog to set speed. 
        inputDialog = WatsonSerial(root)  #Hit enter to add speed and close dialog
        root.wait_window(inputDialog.top)
        ser.write('1SP' + inputDialog.speed + '\r') #Pump Speed xxx
    elif (event.char == 'z'):
        ser.write(input_go + '\r')
    elif (event.char == 'x'):
        ser.write(input_stop + '\r')
    elif (event.char == 'c'):
        ser.write(input_drop + '\r')     
    elif (event.char == 'v'):
        ser.write(input_up + '\r')
    elif (event.char == 's'):
        ser.write(input_rev + '\r')        
    elif (event.char == 'd'):
        ser.write(input_clockw + '\r')
    elif (event.char == 'f'):
        ser.write(input_counter + '\r')
    elif (event.char == 'm'):  #m is simulated memo dose. starts and stops within time
        ser.write(input_go + '\r')
        time.sleep(1)
        ser.write(input_stop + '\r')
        
# Create a label with instructions
label = tk.Label(root, width=400, height=300, text='Press "z"=RUN,"x"=STOP,"c"=lower speed,"v"=up speed,"s"=reverse,"d"=CW,"f"=CC or "q" to quit')
label.pack(fill=tk.BOTH, expand=1)
label.bind('<Key>', key)
label.focus_set()

# Hand over to the Tkinter event loop
root.mainloop()

# Close serial port
ser.close()
