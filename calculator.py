from tkinter import *

win = Tk()
win['bg'] = '#1a1a1a'
win.title('Calculator')
win.resizable(False, False)


monitor = Entry(win, width=22, borderwidth=7,
                highlightthickness=0, bd=8, font=("Arial", 28, 'bold'),)
monitor.place(x=11, y=30)
monitor.grid(row=0, column=0, columnspan=6)


def button_click(number):
    string = monitor.get()
    monitor.delete(0, END)
    monitor.insert(0, str(string) + str(number))


def knopkaclear():
    monitor.delete(0, END)


def knopkaplus():
    get_number = monitor.get()
    global saved_number
    global action
    action = 'qushish'
    saved_number = float(get_number)
    monitor.delete(0, END)


def knopkaminus():
    get_number = monitor.get()
    global saved_number
    global action
    action = 'ayirish'
    saved_number = float(get_number)
    monitor.delete(0, END)


def knopkakop():
    get_number = monitor.get()
    global saved_number
    global action
    action = "ko'paytirish"
    saved_number = float(get_number)
    monitor.delete(0, END)


def knopkabol():
    get_number = monitor.get()
    global saved_number
    global action
    action = "bo'lish"
    saved_number = float(get_number)
    monitor.delete(0, END)


def knopkabackspace():
    get_number = monitor.get()
    global saved_number
    global action
    monitor.delete(0, END)
    monitor.insert(0, get_number[0:-1])


def knopkapm():
    get_number = monitor.get()
    global action
    global saved_number
    saved_number = int(get_number)
    monitor.delete(0, END)
    if saved_number > 0:
        action = "minus"
    elif saved_number < 0:
        action = "plus"
    if action == 'minus':
        monitor.insert(0, saved_number * -1)
    if action == 'plus':
        monitor.insert(0, saved_number * -1)


def knopkadaraja():
    global action
    global saved_number
    action = 'daraja'
    saved_number = monitor.get()
    monitor.delete(0, END)


def knopkaequal():
    summa = monitor.get()
    monitor.delete(0, END)
    if action == "qushish":
        a = saved_number + float(summa)
        if a % 1 == 0:
            monitor.insert(0, int(a))
        else:
            monitor.insert(0, float(a))
    if action == "ayirish":
        a = saved_number - float(summa)
        if a % 1 == 0:
            monitor.insert(0, int(a))
        else:
            monitor.insert(0, float(a))
    if action == "ko'paytirish":
        a = saved_number * float(summa)
        if a % 1 == 0:
            monitor.insert(0, int(a))
        else:
            monitor.insert(0, float(a))
    if action == "bo'lish":
        a = saved_number / float(summa)
        if a % 1 == 0:
            monitor.insert(0, int(a))
        else:
            monitor.insert(0, float(a))
    if action == "daraja":
        a = pow(float(saved_number), float(summa))
        if a % 1 == 0:
            monitor.insert(0, int(a))
        else:
            monitor.insert(0, float(a))


knopka1 = Button(win, text="1", bg='orange', font=("Arial", 21, 'bold'), padx=30, pady=10, command=lambda: button_click(1)).grid(
    row=4, column=1, stick='wens')
knopka2 = Button(win, text="2", bg='orange', font=("Arial", 21, 'bold'), padx=40, pady=20, command=lambda: button_click(2)).grid(
    row=4, column=2, stick='wens')
knopka3 = Button(win, text="3", bg='orange', font=("Arial", 21, 'bold'), padx=40, pady=20, command=lambda: button_click(3)).grid(
    row=4, column=3, stick='wens')
knopka4 = Button(win, text="4", bg='orange', font=("Arial", 21, 'bold'), padx=40, pady=20, command=lambda: button_click(4)).grid(
    row=3, column=1, stick='wens')
knopka5 = Button(win, text="5", bg='orange', font=("Arial", 21, 'bold'), padx=40, pady=20, command=lambda: button_click(5)).grid(
    row=3, column=2, stick='wens')
knopka6 = Button(win, text="6", bg='orange', font=("Arial", 21, 'bold'), padx=40, pady=20, command=lambda: button_click(6)).grid(
    row=3, column=3, stick='wens')
knopka7 = Button(win, text="7", bg='orange', font=("Arial", 21, 'bold'), padx=40, pady=20, command=lambda: button_click(7)).grid(
    row=2, column=1, stick='wens')
knopka8 = Button(win, text="8", bg='orange', font=("Arial", 21, 'bold'), padx=10, pady=20, command=lambda: button_click(8)).grid(
    row=2, column=2, stick='wens')
knopka9 = Button(win, text="9", bg='orange', font=("Arial", 21, 'bold'), padx=30, pady=12, command=lambda: button_click(9)).grid(
    row=2, column=3, stick='wens')
knopka0 = Button(win, text="0", bg='orange', font=("Arial", 21, 'bold'), padx=30, pady=15, command=lambda: button_click(0)).grid(
    row=5, column=2, stick='wens')
knopkadot = Button(win, text=".", bg='#1a0900', fg='#ffffff', padx=40, pady=20, command=lambda: button_click('.')).grid(
    row=5, column=1, stick='wens')
knopkapm = Button(win, text="+/-", bg='#1a0900', fg='#ffffff', padx=40, pady=20, command=knopkapm).grid(row=5,
                                                                                                        column=3, stick='wens')
knopkaequal = Button(win, text="=", bg='#e62e00', padx=20, pady=10, command=knopkaequal).grid(
    row=5, column=4, stick='wens')
knopkaplus = Button(win, text="+", bg='#1a0900', fg='#ffffff', padx=50, pady=20, command=knopkaplus).grid(row=4,
                                                                                                          column=4, stick='wens')
knopkaminus = Button(win, text="-", bg='#1a0900', fg='#ffffff', command=knopkaminus).grid(row=3,
                                                                                          column=4, stick='wens')
knopkabol = Button(win, text="/", bg='#1a0900', fg='#ffffff', padx=10, pady=20, command=knopkabol).grid(row=2,
                                                                                                        column=4, stick='wens')
knopkakop = Button(win, text="*", bg='#1a0900', fg='#ffffff', padx=40, pady=20, command=knopkakop).grid(row=1,
                                                                                                        column=3, stick='wens')
knopkadaraja = Button(win, text="x^y", bg='#1a0900', fg='#ffffff', padx=40, pady=20, command=knopkadaraja).grid(
    row=1, column=2, stick='wens')
knopkaclear = Button(win, text="Clear", bg='#1a0900',  fg='#ffffff', padx=35, pady=30, command=knopkaclear).grid(
    row=1, column=1, stick='wens')
knopkabackspace = Button(win, text='<- Backspace', bg='#1a0900', fg='#ffffff',
                         padx=20, pady=10, command=knopkabackspace).grid(row=1, column=4, stick='wens')


win.mainloop()
