# Code for Digital Clock

#importing modules
import time
from tkinter import Label, Tk 


# Setting the size/title/font/bg color of the clock
app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("720x150")
app_window.resizable(1,1)
text_font= ("Boulder", 250, 'bold')
background = "#000000"
foreground= "#ffffff"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
