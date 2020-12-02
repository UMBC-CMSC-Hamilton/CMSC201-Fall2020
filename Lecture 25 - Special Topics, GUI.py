"""
NONE OF THIS APPLIES TO THE REST OF 201
DO NOT USE THIS IN ANY PROJECT (3) or the FINAL

But, in your future life, you could always make yourself little gui programs.

There's other graphical packages for python, Qt4, Qt5, bunch of others
It's always dependent on what you need.  Tk gets you there fast
Qt4, 5 look more professional.

Python -> other languages (functions, classes, variables, for loops, while loops, etc)
Tkinter -> Qt, Others (Buttons, Edits, window placement, etc)
"""

import tkinter as tk
import tkinter.messagebox as mb


def click_callback():
    print('you have clicked the button')


def get_the_text():
    # message boxes have title, text
    # tk.messagebox.showinfo
    mb.showinfo('Here is your string:', entry_string.get())


def does_it_blend(event):
    print(event)
    print('yep')


def radio_check():
    mb.showinfo('Favorite Color', 'Your favorite color is: {}'.format(selection.get()))
    main_window.configure(bg=selection.get())


if __name__ == '__main__':
    main_window = tk.Tk()
    main_window.title('Here is a window')
    main_window.geometry('1000x500')

    the_button = tk.Button(main_window, text='Click Me', command=click_callback)
    # first, notice that click_callback doesn't have parentheses on it.
    # because we don't actually want to call the function here.
    # the_button.pack(side=tk.RIGHT)
    # .place(x=200, y=400)
    the_button.grid(row=5, column=4)
    for i in range(6):
        main_window.rowconfigure(i, weight=1)

    # width is not in pixels, in characters.
    entry_string = tk.StringVar(main_window)
    my_entry = tk.Entry(main_window, width=20, textvariable=entry_string)
    # binding a callback function to a specific event (enter being pressed in this entry).
    my_entry.bind('<Return>', does_it_blend)
    my_entry.grid(row=0, column=0)
    # how do we get the the text out of the Entry?

    another_button = tk.Button(main_window, text='get text', command=get_the_text)
    another_button.grid(row=0, column=1)
    """
        fill = tk.BOTH, tk.X, tk.Y
    """
    # .pack() and .grid()

    # selection = tk.IntVar(main_window)
    selection = tk.StringVar(main_window, value="no color")

    tk.Radiobutton(main_window, text='Red', variable=selection, value="Red", command=radio_check).grid(row=3, column=0)
    tk.Radiobutton(main_window, text='Green', variable=selection, value='Green', command=radio_check).grid(row=4, column=0)
    tk.Radiobutton(main_window, text='Blue', variable=selection, value='Blue', command=radio_check).grid(row=5, column=0)
    tk.Radiobutton(main_window, text='Yellow', variable=selection, value='Yellow', command=radio_check).grid(row=6, column=0)
    tk.Radiobutton(main_window, text='Orange', variable=selection, value='Orange', command=radio_check).grid(row=7, column=0)
    tk.Radiobutton(main_window, text='Black', variable=selection, value='Black', command=radio_check).grid(row=8, column=0)

    file_menu = tk.Menu(tearoff=0)
    file_menu.add_checkbutton(label='Click Me')
    file_menu.add_command(label='Exit', command=main_window.destroy)
    # let's make a menu!
    the_main_menu_bar = tk.Menu(tearoff=0)
    # dont ask what tearoff=0 means

    # adds file_menu as a sub-menu of the menu bar
    the_main_menu_bar.add_cascade(label='File', menu=file_menu)
    the_main_menu_bar.add_command(label='Cool Stuff')
    the_main_menu_bar.add_command(label='Dont look here')
    the_main_menu_bar.add_checkbutton(label='Its not the worst')
    # this
    # main_window['menu'] = the_main_menu_bar
    # or this:
    main_window.configure(menu=the_main_menu_bar)
    """
        https://cs111.wellesley.edu/~cs111/archive/cs111_spring15/public_html/labs/lab12/colors.png
    """
    main_window.configure(bg='black')
    """
        99.9% of the program runs in this magical function here
    """
    main_window.mainloop()
