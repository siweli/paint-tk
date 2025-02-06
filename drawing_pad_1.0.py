from tkinter import *
from tkinter.colorchooser import askcolor



#create object
main = Tk()
main.title("Paint by Lewis")
main.geometry("1280x720")
main.iconbitmap("assets\\paint_icon.ico")



#load assets
eraser_image = PhotoImage(file = "assets\\eraser.png")
pen_image = PhotoImage(file = "assets\\black_pen.png")



#functions to call
#draw a line with mouse
def draw_line(event):
    x1, y1 = event.x, event.y
    if canvas.old_coords:
        x2, y2 = canvas.old_coords
        canvas.create_oval(x1,y1,x2,y2, width=int(pen_entry.get()), outline=colour_change_btn["bg"], fill=colour_change_btn["bg"])
    canvas.old_coords = x1, y1
    
#draw a dot at mouse
def draw_dot(event):
    x1=event.x
    y1=event.y
    x2=event.x
    y2=event.y
    canvas.create_oval(x1,y1,x2,y2, width=int(pen_entry.get()), outline=colour_change_btn["bg"], fill=colour_change_btn["bg"])

#reset pen so it doesn't continue line after letting go of M1
def reset_pen(event):
    canvas.old_coords = None

#clears the canvas
def clear():
    canvas.delete("all")

#updates entry value from scale
def scale_update(amount):
    pen_entry.delete(0, 'end')
    pen_entry.insert(0, amount)

#updates scale value from entry
def pen_entry_update(variable, index, mode):
    x = pen_entry.get()
    try:
        if x != "":
            pen_scale.set(int(x))
    except Exception:
        pass

#opens colour picker window
def colour_change():
    colour = askcolor(title="Choose colour")
    colour_change_btn.config(bg=colour[1])
    hex_entry.delete(0, 'end')
    hex_entry.insert(0, colour[1])
    main["cursor"] = "@black_pen.cur"

#specific hex code for colour entry
def hex_entry_update(variable, index, mode):
    x = hex_entry.get()
    try:
        if len(x) ==7:
            colour_change_btn.config(bg=x)
    except Exception:
        pass
    main["cursor"] = "@black_pen.cur"

#pen mode
def pen_mode():
    colour = "#000000"
    colour_change_btn.config(bg=colour)
    hex_entry.insert(0, colour)
    pen_scale.set(5)
    main["cursor"] = "@black_pen.cur"
    
#eraser mode
def eraser_mode():
    colour = "#FFFFFF"
    colour_change_btn.config(bg=colour)
    hex_entry.insert(0, colour)
    pen_scale.set(15)
    main["cursor"] = "@eraser.cur"

#drawing canvas stuff
canvas = Canvas(main, bg="#FFFFFF", width=1920, height=1080)
canvas.place(x=0,y=0)
canvas.old_coords = None

canvas.bind('<B1-Motion>', lambda event:draw_line(event))
canvas.bind('<ButtonRelease-1>', reset_pen)
#problem is to draw a dot you need this code but due to how laggy tkinter is, the dot appears separate to the line
canvas.bind('<Button-1>', lambda event:draw_dot(event))



#menu split up into sub menus to better organise
main_menu = Frame(main, bg='#C8C4C4')
main_menu.pack(side='right', anchor='ne')

clear_menu = Frame(main_menu, bg='#C8C4C4')
clear_menu.pack(pady=10)

pen_size_menu = Frame(main_menu, bg='#C8C4C4')
pen_size_menu.pack(pady=10)

colour_menu = Frame(main_menu, bg='#C8C4C4')
colour_menu.pack(pady=20)

modes_menu = Frame(main_menu, bg="#C8C4C4")
modes_menu.pack(pady=5, side="bottom")



#clear canvas frame stuff
sub_clear_all = Frame(clear_menu, bg="#C8C4C4")
sub_clear_all.pack(side="top")

#pen frame stuff
sub_pen_sizing = Frame(main_menu, bg="#C8C4C4")
sub_pen_sizing.pack()

sub_pen_label = Frame(sub_pen_sizing, bg="#C8C4C4")
sub_pen_label.pack(side="left")

sub_pen_entry = Frame(sub_pen_sizing, bg="#C8C4C4")
sub_pen_entry.pack(side="right")


sub_pen_slider = Frame(main_menu, bg="#C8C4C4")
sub_pen_slider.pack()

#colour frame stuff
sub_colour_texts = Frame(colour_menu, bg="#C8C4C4")
sub_colour_texts.pack(side="left")

sub_colour_entrys = Frame(colour_menu, bg="#C8C4C4")
sub_colour_entrys.pack(side="right")



#adding features
#empty label
empty_clear_label = Label(sub_clear_all
                      , height=1,width=10, bg="#C8C4C4")
empty_clear_label.pack(side="left")

#'clear all' button
clear_button = Button(sub_clear_all
                      , text="CLEAR ALL", command=clear)
clear_button.pack(anchor="ne")

#'pen size:' label
pen_size_text = Label(sub_pen_label
                      , text="pen size:")
pen_size_text.pack(side="right", padx=1)

#pen size entry label
pen_entry_var = StringVar()
pen_entry_var.trace_add("write", pen_entry_update)
pen_entry = Entry(sub_pen_entry
                  , textvariable=pen_entry_var, width=4)
pen_entry.pack(side="left", padx=1)
pen_entry.insert(0, "5")

#pen size slider
pen_scale = Scale(sub_pen_slider
                  , from_=1, to=100, orient=HORIZONTAL, activebackground='#FFFFFF',
                  command=scale_update, sliderlength=15, length=130, cursor='arrow')
pen_scale.pack(pady=2, side='top')
pen_scale.set(5)

#'current colour:' label
colour_label = Label(sub_colour_texts
                     , text="current colour:")
colour_label.pack(anchor='ne', padx=1)

#colour changer button
colour="#000000"
colour_change_btn = Button(sub_colour_entrys
                           , height=1, width=2, bg=colour, command=colour_change)
colour_change_btn.pack(anchor='nw', padx=1)

#'enter hex:' label
hex_label = Label(sub_colour_texts
                  , text="enter hex:")
hex_label.pack(anchor='se', padx=1)

#hex entry label
hex_entry_var = StringVar()
hex_entry_var.trace_add("write", hex_entry_update)
hex_entry = Entry(sub_colour_entrys
                  , textvariable=hex_entry_var, width=7)
hex_entry.pack(anchor='sw', padx=1)
hex_entry.insert(0, "#000000")

#pen mode button
pen_btn = Button(modes_menu
                           , height=30, width=30, image=pen_image, command=pen_mode)
pen_btn.pack(side="left", padx=3)

#eraser mode button
eraser_btn = Button(modes_menu
                           , height=30, width=30, image=eraser_image, command=eraser_mode)
eraser_btn.pack(side="right", padx=3)



#main
main["cursor"] = "@black_pen.cur"
main.mainloop()
