# import libraries for serial port and Tkinter GUI
import serial
import Tkinter
import time

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
root = Tkinter.Tk()
root.geometry('600x300+100+100')
root.title('Pump Command Sender')

input_go = '1GO'
input_stop = '1ST'
input_drop = '1SD'
input_up = '1SI'
input_rev = '1RC'
input_clockw = '1RR'
input_counter = '1RL'

# Create a keystroke handler TODO...handle exit hangup with tkinter
def key(event):
    if (event.char == 'q'):
        root.quit()
        ser.close()
        exit()
    elif event.char >= '0' and event.char <= '9':
        ser.write(event.char)
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
    elif (event.char == 'm'):
        ser.write(input_go + '\r')
        time.sleep(1)
        ser.write(input_stop + '\r')
        
# Create a label with instructions
label = Tkinter.Label(root, width=400, height=300, text='Press "z"=RUN,"x"=STOP,"c"=lower speed,"v"=up speed,"s"=reverse,"d"=CW,"f"=CC or "q" to quit')
label.pack(fill=Tkinter.BOTH, expand=1)
label.bind('<Key>', key)
label.focus_set()

# Hand over to the Tkinter event loop
root.mainloop()

# Close serial port
ser.close()
