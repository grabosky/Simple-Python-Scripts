import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

#################### WINDOW SETTINGS START #####################
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
#################### WINDOW SETTINGS END #####################


#################### WINDOW LAYOUT START #####################

#Examples: 

#Draw label1 widget for testing
#label1 = ttk.Label(window, text + 'Label 1', background = 'blue') 

#3 Forms in Layouting: Pack, Grid, Place:

#Pack Example ----- (ie. stack from top to bottom)
#label1.pack(side = 'left', expand = True, fill = 'y')    #fill might be "both"

#Grid Example ----- (ie. create invisible grid)
#window.columnconfigure(0, weight = 1)
#window.columnconfigure(1, weight = 1)
#window.columnconfigure(2, weight = 2)
#window.rowconfigure(0, weight = 1)
#window.rowconfigure(1, weight = 1)

#label1.grid(row = 0, column = 1, sticky = 'nsew')

#Place Example ----- (ie. specific pixels x,y)
#label1.place(x = 100, y = 100, width = 200, height = 100)
#label1.place(relx = 0.5, rely = 0.5)  #Can be also relwidth =1, anchor = 'center', 'se' etc. 


### Actual Layout: ###
#Grid: (Define two spaces/columns, the left one must be 1/7th the size of the right one)
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 7)
#window.rowconfigure(0, weight = 1)

## Left Menu
#Create Widgets
button001 = ttk.Button(window, text = 'ButtonTest')
button002 = ttk.Button(window, text = 'ButtonTest')
button003 = ttk.Button(window, text = 'ButtonTest')
button004 = ttk.Button(window, text = 'ButtonTest')
button005 = ttk.Button(window, text = 'ButtonTest')
button006 = ttk.Button(window, text = 'ButtonTest')
#Draw Widgets in Grid
button001.grid(row = 0, column = 0, sticky = 'nsew', padx = '20', pady ='20')  #relx = 0.5, rely = 0.5 
button002.grid(row = 1, column = 0, sticky = 'nsew', padx = '20', pady ='20')
button003.grid(row = 2, column = 0, sticky = 'nsew', padx = '20', pady ='20')
button004.grid(row = 3, column = 0, sticky = 'nsew', padx = '20', pady ='20')
button005.grid(row = 4, column = 0, sticky = 'nsew', padx = '20', pady ='20')
button006.grid(row = 5, column = 0, sticky = 'nsew', padx = '20', pady ='20')

## Right Menu


#################### WINDOW LAYOUT END  #####################



#Run
window.mainloop()
