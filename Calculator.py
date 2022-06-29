import tkinter as tk
from PIL import Image,ImageTk

app = tk.Tk()
app.title("Calculator")
app.geometry("500x500")
app.iconbitmap("im.ico")
app.resizable(False,False)
theme = "#0b0138"
app.config(bg=theme)
square = 70
col1 = 90
col2 = col1 + square + 10
col3 =col2 + square + 10
col4 =col3 + square + 10
row1 = 160
row2 = row1 + square + 10
row3 = row2 + square + 10
row4 = row3 + square + 10

inputLabel = tk.Label(app,text="Calculator: ", font=('Times',18), bg=theme, fg='white').place(x=20,y=10)
screen = tk.Entry(app, font=('Time',18)).place(x=20,y=60,width=450,height=70)

zero1 = Image.open('numbers/zero.png')
zero1 = zero1.resize((square,square), Image.ANTIALIAS)
zero1 = ImageTk.PhotoImage(zero1)
zero = tk.Button(image=zero1, borderwidth=0, bg=theme)
zero.place(x=col1,y=row1)

one1 = Image.open('numbers/one.png')
one1 = one1.resize((square,square), Image.ANTIALIAS)
one1 = ImageTk.PhotoImage(one1)
one = tk.Button(image=one1, borderwidth=0, bg=theme)
one.place(x=col2,y=row1)

two1 = Image.open('numbers/two.png')
two1 = two1.resize((square,square), Image.ANTIALIAS)
two1 = ImageTk.PhotoImage(two1)
two = tk.Button(image=two1, borderwidth=0, bg=theme)
two.place(x=col3,y=row1)

three1 = Image.open('numbers/three.png')
three1 = three1.resize((square,square), Image.ANTIALIAS)
three1 = ImageTk.PhotoImage(three1)
three = tk.Button(image=three1, borderwidth=0, bg=theme)
three.place(x=col1,y=row2)

four1 = Image.open('numbers/four.png')
four1 = four1.resize((square,square), Image.ANTIALIAS)
four1 = ImageTk.PhotoImage(four1)
four = tk.Button(image=four1, borderwidth=0, bg=theme)
four.place(x=col2,y=row2)

five1 = Image.open('numbers/five.png')
five1 = five1.resize((square,square), Image.ANTIALIAS)
five1 = ImageTk.PhotoImage(five1)
five = tk.Button(image=five1, borderwidth=0, bg=theme)
five.place(x=col3,y=row2)

six1 = Image.open('numbers/six.png')
six1 = six1.resize((square,square), Image.ANTIALIAS)
six1 = ImageTk.PhotoImage(six1)
six = tk.Button(image=six1, borderwidth=0, bg=theme)
six.place(x=col1,y=row3)

seven1 = Image.open('numbers/seven.png')
seven1 = seven1.resize((square,square), Image.ANTIALIAS)
seven1 = ImageTk.PhotoImage(seven1)
seven = tk.Button(image=seven1, borderwidth=0, bg=theme)
seven.place(x=col2,y=row3)

eight1 = Image.open('numbers/eight.png')
eight1 = eight1.resize((square,square), Image.ANTIALIAS)
eight1 = ImageTk.PhotoImage(eight1)
eight = tk.Button(image=eight1, borderwidth=0, bg=theme)
eight.place(x=col3,y=row3)

nine1 = Image.open('numbers/nine.png')
nine1 = nine1.resize((square,square), Image.ANTIALIAS)
nine1 = ImageTk.PhotoImage(nine1)
nine = tk.Button(image=nine1, borderwidth=0, bg=theme)
nine.place(x=col2,y=row4)

plus1 = Image.open('numbers/plus.png')
plus1 = plus1.resize((square,square), Image.ANTIALIAS)
plus1 = ImageTk.PhotoImage(plus1)
plus = tk.Button(image=plus1, borderwidth=0, bg=theme)
plus.place(x=col4,y=row1)

remove1 = Image.open('numbers/remove.png')
remove1 = remove1.resize((square,square), Image.ANTIALIAS)
remove1 = ImageTk.PhotoImage(remove1)
remove = tk.Button(image=remove1, borderwidth=0, bg=theme)
remove.place(x=col4,y=row2)

divide1 = Image.open('numbers/divide.png')
divide1 = divide1.resize((square,square), Image.ANTIALIAS)
divide1 = ImageTk.PhotoImage(divide1)
divide = tk.Button(image=divide1, borderwidth=0, bg=theme)
divide.place(x=col4,y=row3)


app.mainloop()