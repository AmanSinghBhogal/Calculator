import tkinter as tk

app = tk.Tk()
app.title("Calculator")
app.geometry("720x720")
app.iconbitmap("im.ico")
app.resizable(False,False)

screen = tk.Entry(app,width=75).place(x=20,y=20)

app.mainloop()