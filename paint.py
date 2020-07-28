from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageGrab, ImageTk
import PIL
from tkinter import messagebox

root = Tk()

root.title('paint program')
root.geometry("750x650")
root.config(bg='#303040')

# default brush color
brush_color = 'black'


def paint(e):

    # brush parameters
    brush_width = int(my_slider.get())

    # brush_types: BUTT, ROUND, PROJECTING
    brush_type = brush_var.get()

    # startin position
    x1 = e.x - 1
    y1 = e.y - 1

    # ending position
    x2 = e.x + 1
    y2 = e.y + 1

    #draw on canvas
    my_canvas.create_line(x1,
                          y1,
                          x2,
                          y2,
                          fill=brush_color,
                          width=brush_width,
                          capstyle=brush_type,
                          smooth=True)


def change_brush_size(default):
    my_slider_label.config(text=int(my_slider.get()))


def change_brush_color():
    global brush_color
    brush_color = 'black'
    brush_color = colorchooser.askcolor(color=brush_color)[1]


def change_canvas_color():
    global canvas_color
    canvas_color = 'white'
    canvas_color = colorchooser.askcolor(color=canvas_color)[1]
    my_canvas.config(bg=canvas_color)


def clear_screen():
    my_canvas.delete(ALL)
    my_canvas.config(bg='white')


def save_image():
    result = filedialog.asksaveasfilename(initialdir='./',
                                          filetypes=(('png file', '*.png'),
                                                     ('all files', '*.*')))
    if not result.endswith('.png'):
        result = result + '.png'

    if result:
        x = root.winfo_rootx() + my_canvas.winfo_x()
        y = root.winfo_rooty() + my_canvas.winfo_y()
        x1 = x + my_canvas.winfo_width()
        y1 = y + my_canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(result)

        # saved pop up message box
        messagebox.showinfo('Saved Image', 'your image was saved sucessfully')


# canvas properties
width = 600
height = 400

style = ttk.Style()
style.configure("TButton", padding=3, relief="flat", bg="#ccc")

my_canvas = Canvas(root, width=width, height=height, bg='white')
my_canvas.pack(pady=20)

my_canvas.bind('<B1-Motion>', paint)

# create brush options frame
brush_options = Frame(root)
brush_options.pack(pady=5)

# brush size
brush_size_frame = LabelFrame(brush_options, text="Brush Size")
brush_size_frame.grid(row=0, column=0, padx=50)

# brush slider
my_slider = ttk.Scale(brush_size_frame,
                      command=change_brush_size,
                      from_=1,
                      to=100,
                      value=10,
                      orient=VERTICAL)
my_slider.pack(padx=10, pady=10)

my_slider_label = Label(brush_size_frame, text=my_slider.get())
my_slider_label.pack(pady=5)

# brush color
brush_color_frame = LabelFrame(brush_options, text="Change Colors")
brush_color_frame.grid(row=0, column=1, padx=50)

brush_color_button = ttk.Button(brush_color_frame,
                                text='Brush Color',
                                command=change_brush_color)
brush_color_button.pack(padx=10, pady=10)

canvas_color_button = ttk.Button(brush_color_frame,
                                 text='Canvas Color',
                                 command=change_canvas_color)
canvas_color_button.pack(padx=10, pady=10)

# brush type
brush_type_frame = LabelFrame(brush_options, text="Brush Type", height=400)
brush_type_frame.grid(row=0, column=2, padx=50)

brush_var = StringVar()
brush_var.set('round')

# radio buttons for brush type
brush_type_radio1 = Radiobutton(brush_type_frame,
                                text='Round',
                                variable=brush_var,
                                value='round')
brush_type_radio2 = Radiobutton(brush_type_frame,
                                text='Slash',
                                variable=brush_var,
                                value='butt')
brush_type_radio3 = Radiobutton(brush_type_frame,
                                text='Diamond',
                                variable=brush_var,
                                value='projecting')

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# clear screen
canvas_options = LabelFrame(brush_options, text='canvas options')
canvas_options.grid(row=0, column=3, padx=50)

clear_screen_button = ttk.Button(canvas_options,
                                 text='clear screen',
                                 command=clear_screen)
clear_screen_button.pack(pady=10, padx=10)

save_image_button = ttk.Button(canvas_options,
                               text='save image',
                               command=save_image)
save_image_button.pack(pady=10, padx=10)

root.mainloop()
