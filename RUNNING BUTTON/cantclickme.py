import tkinter as tk
import random

root = tk.Tk()
root.title("CATCH ME BITCH")
root.geometry('500x500')

button = tk.Button(root,text="CLICK ME!")
button.bind("<Motion>",lambda event:move_away(event,button))
button.pack(pady=20)

def move_away(event,button):
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    button_width = button.winfo_width()
    button_height = button.winfo_height()

    colors = [
    ('blue', 'red'),
    ('green', 'purple'),
    ('orange', 'blue'),
    ('yellow', 'green'),
    ('pink', 'teal'),
    ('brown', 'cyan'),
    ('magenta', 'lime'),
    ('maroon', 'navy'),
    ('olive', 'silver'),
    ('indigo', 'goldenrod')
    ]

    chosen_color = random.choice(colors)

    button.configure(bg=chosen_color[0])

    root.configure(bg=chosen_color[1])

    new_x = random.randint(0,window_width - button_width)
    new_y = random.randint(0,window_height - button_height)

    new_size_x = random.randint(0,60)
    new_size_y = random.randint(0,60)

    button.configure(padx=new_size_x,pady=new_size_y)

    button.place(x=new_x,y=new_y)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = root.winfo_width()
    window_height = root.winfo_height()

    max_x = screen_width - window_width
    max_y = screen_height - window_height

    new_x = random.randint(0, max_x)
    new_y = random.randint(0, max_y)

    root.geometry(f"+{new_x}+{new_y}")

root.mainloop()