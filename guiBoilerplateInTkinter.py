import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

#################### WINDOW START #####################
window = tk.Tk()
window.title('NewSoftwareProject')
#window.iconbitmap("python.ico")

#Create Window in the middle of the screen
window_width = 1000
window_height = 600
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()
left  = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

#Window Sizes Attributes
window.minsize(600,400)
window.maxsize(1200,800) 
window.resizable(True,True)  #width,height

#Screen Attributes
#print(window.winfo_screenwidth())
#print(window.winfo_screenheight())
window.attributes('-alpha', 1)   #Screen Opacity from 0 to 1
#window.attributes('-fullscreen', True)  #Enters fullscreen - use only if Exit event coded in

#TitleBar
#window.overrideredirect(True)   #Dissapears Title Bar
#grip = ttk.Sizegrip(window)  #Makes window being able to resize if doesn't have Title Bar
#grip.place(relx = 1.0, rely = 1.0, anchor = 'se' )  #Places grip

#Window Key Events
window.bind('<Escape>', lambda event: window.quit()) #Exit window when pushed ESC
#################### WINDOW END #####################




#Run
window.mainloop()
