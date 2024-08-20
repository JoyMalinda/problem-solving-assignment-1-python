from tkinter import Toplevel, Label, Button, StringVar, Tk, X

root = Tk()
USERNAME = StringVar()
PASSWORD = StringVar()
lbl_text = Label(root, text="")
lbl_text.pack()

def Database():
    global conn, cursor
    import sqlite3
    conn = sqlite3.connect()
    cursor = conn.cursor

def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM member WHERE username = ? AND password = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()
 
def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Python: Simple Login Application")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20))
    lbl_home.pack()
    btn_back = Button(Home, text='Back', command=Back)
    btn_back.pack(pady=20, fill=X)
 
def Back():
    Home.destroy()
    root.deiconify()

root.mainloop()