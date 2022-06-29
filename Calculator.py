import tkinter as tk
from PIL import Image,ImageTk

app = tk.Tk()
app.title("Calculator")
app.geometry("500x600")
app.iconbitmap("im.ico")
app.resizable(False,False)
theme = "#0b0138"
app.config(bg=theme)
square = 70
col1 = 90
col2 = col1 + square + 10
col3 =col2 + square + 10
col4 =col3 + square + 10
# row0 = 160
row1 = 160
# row1 = 250
row2 = row1 + square + 10
row3 = row2 + square + 10
row4 = row3 + square + 10
row5 = row4 + square + 10

inputLabel = tk.Label(app,text="Calculator: ", font=('Times',18), bg=theme, fg='white').place(x=20,y=10)
screen = tk.Entry(app, font=('Time',18),justify='right',borderwidth=15,relief=tk.FLAT).place(x=20,y=60,width=460,height=70)

clear1 = Image.open('numbers/clear.png')
clear1 = clear1.resize((square,square), Image.ANTIALIAS)
clear1 = ImageTk.PhotoImage(clear1)
clear = tk.Button(image=clear1, borderwidth=0, bg=theme, activebackground=theme)
clear.place(x=col1,y=row5)

zero1 = Image.open('numbers/zero.png')
zero1 = zero1.resize((square,square), Image.ANTIALIAS)
zero1 = ImageTk.PhotoImage(zero1)
zero = tk.Button(image=zero1, borderwidth=0, bg=theme, activebackground=theme)
zero.place(x=col2,y=row5)

percent1 = Image.open('numbers/percent.png')
percent1 = percent1.resize((square,square), Image.ANTIALIAS)
percent1 = ImageTk.PhotoImage(percent1)
percent = tk.Button(image=percent1, borderwidth=0, bg=theme, activebackground=theme)
percent.place(x=col1,y=row1)

one1 = Image.open('numbers/one.png')
one1 = one1.resize((square,square), Image.ANTIALIAS)
one1 = ImageTk.PhotoImage(one1)
one = tk.Button(image=one1, borderwidth=0, bg=theme, activebackground=theme)
one.place(x=col1,y=row2)

two1 = Image.open('numbers/two.png')
two1 = two1.resize((square,square), Image.ANTIALIAS)
two1 = ImageTk.PhotoImage(two1)
two = tk.Button(image=two1, borderwidth=0, bg=theme, activebackground=theme)
two.place(x=col2,y=row2)

three1 = Image.open('numbers/three.png')
three1 = three1.resize((square,square), Image.ANTIALIAS)
three1 = ImageTk.PhotoImage(three1)
three = tk.Button(image=three1, borderwidth=0, bg=theme, activebackground=theme)
three.place(x=col3,y=row2)

four1 = Image.open('numbers/four.png')
four1 = four1.resize((square,square), Image.ANTIALIAS)
four1 = ImageTk.PhotoImage(four1)
four = tk.Button(image=four1, borderwidth=0, bg=theme, activebackground=theme)
four.place(x=col1,y=row3)

five1 = Image.open('numbers/five.png')
five1 = five1.resize((square,square), Image.ANTIALIAS)
five1 = ImageTk.PhotoImage(five1)
five = tk.Button(image=five1, borderwidth=0, bg=theme, activebackground=theme)
five.place(x=col2,y=row3)

six1 = Image.open('numbers/six.png')
six1 = six1.resize((square,square), Image.ANTIALIAS)
six1 = ImageTk.PhotoImage(six1)
six = tk.Button(image=six1, borderwidth=0, bg=theme, activebackground=theme)
six.place(x=col3,y=row3)

seven1 = Image.open('numbers/seven.png')
seven1 = seven1.resize((square,square), Image.ANTIALIAS)
seven1 = ImageTk.PhotoImage(seven1)
seven = tk.Button(image=seven1, borderwidth=0, bg=theme, activebackground=theme)
seven.place(x=col1,y=row4)

eight1 = Image.open('numbers/eight.png')
eight1 = eight1.resize((square,square), Image.ANTIALIAS)
eight1 = ImageTk.PhotoImage(eight1)
eight = tk.Button(image=eight1, borderwidth=0, bg=theme, activebackground=theme)
eight.place(x=col2,y=row4)

nine1 = Image.open('numbers/nine.png')
nine1 = nine1.resize((square,square), Image.ANTIALIAS)
nine1 = ImageTk.PhotoImage(nine1)
nine = tk.Button(image=nine1, borderwidth=0, bg=theme, activebackground=theme)
nine.place(x=col3,y=row4)

plus1 = Image.open('numbers/plus.png')
plus1 = plus1.resize((square,square), Image.ANTIALIAS)
plus1 = ImageTk.PhotoImage(plus1)
plus = tk.Button(image=plus1, borderwidth=0, bg=theme, activebackground=theme)
plus.place(x=col4,y=row1)

remove1 = Image.open('numbers/remove.png')
remove1 = remove1.resize((square,square), Image.ANTIALIAS)
remove1 = ImageTk.PhotoImage(remove1)
remove = tk.Button(image=remove1, borderwidth=0, bg=theme, activebackground=theme)
remove.place(x=col4,y=row2)

divide1 = Image.open('numbers/divide.png')
divide1 = divide1.resize((square,square), Image.ANTIALIAS)
divide1 = ImageTk.PhotoImage(divide1)
divide = tk.Button(image=divide1, borderwidth=0, bg=theme, activebackground=theme)
divide.place(x=col4,y=row3)

multiply1 = Image.open('numbers/multiply.png')
multiply1 = multiply1.resize((square,square), Image.ANTIALIAS)
multiply1 = ImageTk.PhotoImage(multiply1)
multiply = tk.Button(image=multiply1, borderwidth=0, bg=theme, activebackground=theme)
multiply.place(x=col4,y=row4)


open_bracket1 = Image.open('numbers/open-bracket.png')
open_bracket1 = open_bracket1.resize((square,square), Image.ANTIALIAS)
open_bracket1 = ImageTk.PhotoImage(open_bracket1)
open_bracket = tk.Button(image=open_bracket1, borderwidth=0, bg=theme, activebackground=theme)
open_bracket.place(x=col2,y=row1)


close_bracket1 = Image.open('numbers/close-bracket.png')
close_bracket1 = close_bracket1.resize((square,square), Image.ANTIALIAS)
close_bracket1 = ImageTk.PhotoImage(close_bracket1)
close_bracket = tk.Button(image=close_bracket1, borderwidth=0, bg=theme, activebackground=theme)
close_bracket.place(x=col3,y=row1)


equal1 = Image.open('numbers/equal.png')
equal1 = equal1.resize((square,square), Image.ANTIALIAS)
equal1 = ImageTk.PhotoImage(equal1)
equal = tk.Button(image=equal1, borderwidth=0, bg=theme, activebackground=theme)
equal.place(x=col4,y=row5)


decimal1 = Image.open('numbers/decimal.png')
decimal1 = decimal1.resize((square,square), Image.ANTIALIAS)
decimal1 = ImageTk.PhotoImage(decimal1)
decimal = tk.Button(image=decimal1, borderwidth=0, bg=theme, activebackground=theme)
decimal.place(x=col3,y=row5)



app.mainloop()