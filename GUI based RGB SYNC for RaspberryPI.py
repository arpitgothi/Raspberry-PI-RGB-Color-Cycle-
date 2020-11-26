import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time # Import the sleep function from the time module
from tkinter import *
from tkinter import colorchooser
import tkinter as tk

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# make pins into an output
ledR =GPIO.setup(17,GPIO.OUT) #Set pin for RED color
ledG =GPIO.setup(27,GPIO.OUT) #Set pin for GREEN color
ledB =GPIO.setup(22,GPIO.OUT) #Set pin for BLUE color

#Set up outputs as PWM @ 144Hz
freq=60

ledR = GPIO.PWM(17,freq)
ledG = GPIO.PWM(27,freq)
ledB = GPIO.PWM(22,freq)

ledR.start(100)
ledG.start(0)
ledB.start(0)


def colorCycle():
    while True: # Run forever / infinity loop
        for r, g in zip(range(100), range(100,0,-1)):
            ledR.ChangeDutyCycle(r)
            ledG.ChangeDutyCycle(g)
            time.sleep(0.02)

        for g, b in zip(range(100), range(100,0,-1)):
            ledG.ChangeDutyCycle(g)
            ledB.ChangeDutyCycle(b)
            time.sleep(0.02)

        for b, r in zip(range(100), range(100,0,-1)):
            ledB.ChangeDutyCycle(b)
            ledR.ChangeDutyCycle(r)
            time.sleep(0.02)

def staticColor(r,g,b):
    ledR.ChangeDutyCycle(r)
    ledG.ChangeDutyCycle(g)
    ledB.ChangeDutyCycle(b)
    print("100")





def onclick(args):
    if args ==1:
        print("Color Cycle Mode")
        colorCycle()

    if args ==2:
        print("Static Light")
        for widget in root.winfo_children():
            widget.destroy()
        btn1.pack_forget()
        btn2.pack_forget()
        ColorPickerButton()    
        
def ColorPickerButton():                                                                          
    my_button = Button(root, text="Pick A Color", command=colorPicker).pack()

def colorPicker():
    RGB_value, color_code = colorchooser.askcolor()
    #my_label = Label(root, text=color_code).pack(pady=10)
    my_label2 = Label(root, text="Color is applied", font=("Helvetica",32),bg=color_code).pack()
    R,G,B=RGB_value
    r=100 - int(100*int(R)/255)
    g=100 - int(100*int(G)/255)
    b=100 - int(100*int(B)/255)
    staticColor(r,g,b)
    #print(r,g,b)
    


root=tk.Tk()
root.title("GUI Button")
root.geometry("300x300")

btn1 = tk.Button(root, text="Color Cycle Mode", command=lambda:onclick(1))
btn2 = tk.Button(root, text="Static Light", command=lambda:onclick(2))


btn1.pack()
btn2.pack()

root.mainloop()
