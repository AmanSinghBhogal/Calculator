import tkinter as tk
from PIL import Image,ImageTk
from logic import *

app = tk.Tk()
app.title("Calculator")
app.geometry("500x600")
app.iconbitmap("im.ico")
app.resizable(False,False)
theme = "grey"
app.config(bg=theme)
square = 70
col1 = 90
col2 = col1 + square + 10
col3 =col2 + square + 10
col4 =col3 + square + 10
# row0 = 160
# row1 = 160
row1 = 180
row2 = row1 + square + 10
row3 = row2 + square + 10
row4 = row3 + square + 10
row5 = row4 + square + 10

inputLabel = tk.Label(app,text="Calculator: ", font=('Times',18), bg=theme).place(x=20,y=10)

displayValue = tk.StringVar()
displayValue.set('')
result = tk.StringVar()
result.set('')

disp = tk.Entry(app,textvariable=displayValue, font=('Times',18),justify='right',borderwidth=15,relief=tk.FLAT)
disp.place(x=20,y=60,width=460,height=50)
disp.focus_set()
dispResult = tk.Entry(app, textvariable=result,font=('Times',18),justify='right',borderwidth=15,relief=tk.FLAT)
dispResult.place(x=20,y=110,width=460,height=50)


def clear_scr():
    displayValue.set('')
    result.set('')

def run():
    inp = disp.get()
    ans = calculate(inp)
    result.set('= '+ str(ans))

def detectKey(e):
    # print(e.keycode)
    if(e.keycode == 27):
        clear_scr()
    elif(e.keycode == 13):
        run()


app.bind("<KeyPress>", detectKey)
clear1 = Image.open('numbers/clear.png')
clear1 = clear1.resize((square,square))
clear1 = ImageTk.PhotoImage(clear1)
clear = tk.Button(image=clear1, borderwidth=0, bg=theme, activebackground=theme, command=clear_scr)
clear.place(x=col1,y=row5)

def zero_press():
    disp.insert(tk.END, 0)

zero1 = Image.open('numbers/zero.png')
zero1 = zero1.resize((square,square))
zero1 = ImageTk.PhotoImage(zero1)
zero = tk.Button(image=zero1, borderwidth=0, bg=theme, activebackground=theme, command=zero_press)
zero.place(x=col2,y=row5)

def deli_press():
    result.set('')
    i = disp.get()
    j = len(i) - 1
    disp.delete(j,tk.END)

del1 = Image.open('numbers/delete.png')
del1 = del1.resize((square,square))
del1 = ImageTk.PhotoImage(del1)
deli = tk.Button(image=del1, borderwidth=0, bg=theme, activebackground=theme,command=deli_press)
deli.place(x=col4,y=row1)

def one_press():
    disp.insert(tk.END, 1)

one1 = Image.open('numbers/one.png')
one1 = one1.resize((square,square))
one1 = ImageTk.PhotoImage(one1)
one = tk.Button(image=one1, borderwidth=0, bg=theme, activebackground=theme, command= one_press)
one.place(x=col1,y=row2)

def two_press():
    disp.insert(tk.END, 2)

two1 = Image.open('numbers/two.png')
two1 = two1.resize((square,square))
two1 = ImageTk.PhotoImage(two1)
two = tk.Button(image=two1, borderwidth=0, bg=theme, activebackground=theme,command=two_press)
two.place(x=col2,y=row2)

def three_press():
    disp.insert(tk.END, 3)

three1 = Image.open('numbers/three.png')
three1 = three1.resize((square,square))
three1 = ImageTk.PhotoImage(three1)
three = tk.Button(image=three1, borderwidth=0, bg=theme, activebackground=theme, command=three_press)
three.place(x=col3,y=row2)

def four_press():
    disp.insert(tk.END, 4)

four1 = Image.open('numbers/four.png')
four1 = four1.resize((square,square))
four1 = ImageTk.PhotoImage(four1)
four = tk.Button(image=four1, borderwidth=0, bg=theme, activebackground=theme, command= four_press)
four.place(x=col1,y=row3)

def five_press():
    disp.insert(tk.END, 5)

five1 = Image.open('numbers/five.png')
five1 = five1.resize((square,square))
five1 = ImageTk.PhotoImage(five1)
five = tk.Button(image=five1, borderwidth=0, bg=theme, activebackground=theme, command=five_press)
five.place(x=col2,y=row3)

def six_press():
    disp.insert(tk.END, 6)

six1 = Image.open('numbers/six.png')
six1 = six1.resize((square,square))
six1 = ImageTk.PhotoImage(six1)
six = tk.Button(image=six1, borderwidth=0, bg=theme, activebackground=theme, command= six_press)
six.place(x=col3,y=row3)

def seven_press():
    disp.insert(tk.END, 7)

seven1 = Image.open('numbers/seven.png')
seven1 = seven1.resize((square,square))
seven1 = ImageTk.PhotoImage(seven1)
seven = tk.Button(image=seven1, borderwidth=0, bg=theme, activebackground=theme, command=seven_press)
seven.place(x=col1,y=row4)

def eight_press():
    disp.insert(tk.END, 8)

eight1 = Image.open('numbers/eight.png')
eight1 = eight1.resize((square,square))
eight1 = ImageTk.PhotoImage(eight1)
eight = tk.Button(image=eight1, borderwidth=0, bg=theme, activebackground=theme, command= eight_press)
eight.place(x=col2,y=row4)

def nine_press():
    disp.insert(tk.END, 9)

nine1 = Image.open('numbers/nine.png')
nine1 = nine1.resize((square,square))
nine1 = ImageTk.PhotoImage(nine1)
nine = tk.Button(image=nine1, borderwidth=0, bg=theme, activebackground=theme, command=nine_press)
nine.place(x=col3,y=row4)

def plus_press():
    disp.insert(tk.END, '+')

plus1 = Image.open('numbers/plus.png')
plus1 = plus1.resize((square,square))
plus1 = ImageTk.PhotoImage(plus1)
plus = tk.Button(image=plus1, borderwidth=0, bg=theme, activebackground=theme, command=plus_press)
plus.place(x=col4,y=row4)

def sub_press():
    disp.insert(tk.END, '-')

remove1 = Image.open('numbers/minus.png')
remove1 = remove1.resize((square,square))
remove1 = ImageTk.PhotoImage(remove1)
remove = tk.Button(image=remove1, borderwidth=0, bg=theme, activebackground=theme, command=sub_press)
remove.place(x=col4,y=row3)

def divide_press():
    disp.insert(tk.END, '/')

divide1 = Image.open('numbers/divide.png')
divide1 = divide1.resize((square,square))
divide1 = ImageTk.PhotoImage(divide1)
divide = tk.Button(image=divide1, borderwidth=0, bg=theme, activebackground=theme, command=divide_press)
divide.place(x=col3,y=row1)

def mul_press():
    disp.insert(tk.END, '*')

multiply1 = Image.open('numbers/multiply.png')
multiply1 = multiply1.resize((square,square))
multiply1 = ImageTk.PhotoImage(multiply1)
multiply = tk.Button(image=multiply1, borderwidth=0, bg=theme, activebackground=theme, command=mul_press)
multiply.place(x=col4,y=row2)

def obrack_press():
    disp.insert(tk.END, '(')

open_bracket1 = Image.open('numbers/open-bracket.png')
open_bracket1 = open_bracket1.resize((square,square))
open_bracket1 = ImageTk.PhotoImage(open_bracket1)
open_bracket = tk.Button(image=open_bracket1, borderwidth=0, bg=theme, activebackground=theme, command=obrack_press)
open_bracket.place(x=col1,y=row1)

def cbrack_press():
    disp.insert(tk.END, ')')

close_bracket1 = Image.open('numbers/close-bracket.png')
close_bracket1 = close_bracket1.resize((square,square))
close_bracket1 = ImageTk.PhotoImage(close_bracket1)
close_bracket = tk.Button(image=close_bracket1, borderwidth=0, bg=theme, activebackground=theme, command=cbrack_press)
close_bracket.place(x=col2,y=row1)

def equal_press():
    run()

equal1 = Image.open('numbers/equal.png')
equal1 = equal1.resize((square,square))
equal1 = ImageTk.PhotoImage(equal1)
equal = tk.Button(image=equal1, borderwidth=0, bg=theme, activebackground=theme, command= equal_press)
equal.place(x=col4,y=row5)

def dec_press():
    disp.insert(tk.END, '.')

decimal1 = Image.open('numbers/decimal.png')
decimal1 = decimal1.resize((square,square))
decimal1 = ImageTk.PhotoImage(decimal1)
decimal = tk.Button(image=decimal1, borderwidth=0, bg=theme, activebackground=theme, command=dec_press)
decimal.place(x=col3,y=row5)

app.mainloop()