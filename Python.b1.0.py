import serial
import time
import tkinter as tk

ser = serial.Serial('COM4', 9600)

def oeffnen():
    ser.write(b'1')
    
def zu():
    ser.write(b'0')

def gucken():
    x = ser.readline()
    y = x.decode('utf-8')
    label1.configure(text=(y))
    fenster.after(2000, gucken)
    if y == 'Briefkarsten wird geschlossen':
        zu()

fenster = tk.Tk()
fenster.title('Briefkarsten') 
fenster.geometry('200x100') 

button1 = tk.Button(fenster, text="Öffnen", command = oeffnen)
button1.pack()

button2 = tk.Button(fenster, text="Schließen", command = zu)
button2.pack()


label1 = tk.Label(fenster, text='')
label1.pack()

gucken()


tk.mainloop()

