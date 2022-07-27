from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Project 166-167")
root.geometry("500x500")

canvas = Canvas(width = 590, height = 290, bg = "white", highlightbackground = "teal")
canvas.place(relx = 0.5, rely = 0.3, anchor = CENTER)
color_label = Label(root, text = "Choose your color.")
color_label.place(relx = 0.4, rely = 0.5, anchor = CENTER)
fillcolor = ["red", "blue", "green", "teal", "yellow", "orange", "purple"]
ttk = ttk.Combobox(root, state = "readonly", values = fillcolor, width = 5)
ttk.place(relx = 0.6, rely = 0.5, anchor = CENTER)
coordinates_values = [10, 50, 100, 200, 300, 400, 500, 600, 800, 900]
ttk2 = ttk.Combobox(root, state = "readonly", values = coordinates_values, width = 10)
ttk2.place(relx = 0.6, rely = 0.6, anchor = CENTER)
starty = Label(root, text = "Choose your y coordinate")
starty.place(relx = 0.4, rely = 0.7, anchor = CENTER)
ttk3 = ttk.Combobox(root, state = "readonly", values = coordinates_values, width = 10)
ttk3.place(relx = 0.6, rely = 0.7, anchor = CENTER)
endx = Label(root, text = "Choose your ending x coordinate")
endx.place(relx = 0.4, rely = 0.8, anchor = CENTER)
ttk4 = ttk.Combobox(root, state = "readonly", values = coordinates_values, width = 10)
ttk4.place(relx = 0.6, rely = 0.8, anchor = CENTER)
endy = Label(root, text = "Choose your end y coordinate")
endy.place(relx = 0.4, rely = 0.9, anchor = CENTER)
ttk5 = ttk.Combobox(root, state = "readonly", values = coordinates_values, width = 10)

startx = Label(root, text = "Chose your start x coordinate.")
startx.place(relx = 0.4, rely = 0.6, anchor = CENTER)
root.mainloop()