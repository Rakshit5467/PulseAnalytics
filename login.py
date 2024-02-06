from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Lenovo\Desktop\Mini Project f\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


login = CTk()
login.title("Login")
x = (login.winfo_screenwidth() - 1250) // 2
y = (login.winfo_screenheight() - 768) // 2
login.geometry(f"1250x768+{x}+{y}")
login.configure(bg="#FFFFFF")

def signin():
    username = user.get()
    password = passw.get()

    if username == 'admin' and password == '123':
        messagebox.showinfo("Success","Login Successful !")
    elif username != 'admin':
        messagebox.showerror("Error", "Invalid login id")
    elif password != '123':
        messagebox.showerror("Error", "Invalid password")
    else:
        messagebox.showerror("Error", "Invalid login id and password")
        
def show():
    eye.config(file=relative_to_assets("open_eye.png")),
    passw.configure(show='')
    eyebtn.config(command=hide)
    
def hide():
    eye.config(file=relative_to_assets("close_eye.png")),
    passw.configure(show='*')
    eyebtn.config(command=show)
    
def clear():
    user.delete(0, END)
    passw.delete(0, END)
    
def signup_page():
    login.destroy()
    import signup


frame1 = CTkFrame(master=login, fg_color="#4c87ca", corner_radius=0, width=1250,height=768)
frame1.place(x=0, y=0)

background_image = PhotoImage(file=relative_to_assets("bgimg.png"))
background_label = Label(frame1, image=background_image)
background_label.place(x=0, y=0, width=1250)
frame1.image = background_image


frame2 = CTkFrame( master=frame1, fg_color="#FFFFFF", corner_radius=30, height=700, width=480)
frame2.place( x=750,y=40)


btn1 = CTkButton(
    master=frame2,
    text="Sign in",
    corner_radius=30,
    fg_color="#5FBDFF",
    hover_color="#7B66FF",
    width=150,
    height=60,
    font=CTkFont(size=20, weight="bold"),
    command=signin,
    text_color="#000000",
)
btn1.place(relx=0.53,rely=0.78)


btn2 = CTkButton(
    master=frame2,
    text="Clear",
    text_color="#000000",
    corner_radius=30,
    fg_color="transparent",
    hover_color="#FF2D3F",
    border_width=2,
    border_color="black",
    width=150,
    height=60,
    font=CTkFont(size=20, weight="bold"),
    command=clear
)

btn2.place(relx=0.16,rely=0.78)

user = CTkEntry(
    master=frame2,
    corner_radius=100,
    width=400,
    height=70,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Login Id",
    font=CTkFont(family="Kanit Regular",size=20)
)
user.place(rely=0.45,relx=0.08
)

passw = CTkEntry(
    master=frame2,
    show='*',
    corner_radius=50,
    width=400,
    height=70,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Password",
    font=CTkFont(family="Kanit Regular",size=20),
)
passw.place(rely=0.59,relx=0.08)


eye = PhotoImage(file=relative_to_assets("close_eye.png"))
eyebtn = Button(
    frame2,
    borderwidth=0,
    image=eye,
    highlightthickness=0,
    highlightbackground="#D6D6D6",
    command=show,
    cursor="hand2"
)
eyebtn.place(x=380, y=428.5)

title1=CTkLabel(
    master=frame2,
    text="Sign in",
    text_color="#000000",
    font=CTkFont(family="Microsoft YaHei UI Light", size=50,weight="bold")
)
title1.place(x=155,y=210)

profile_img=PhotoImage(file=relative_to_assets("profile.png"))
profile=Label(
    master=frame2,
    image=profile_img,
    borderwidth=0,
).place(relx=0.32,y=28,)

label=Label(frame2,text="Don't have an account yet?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9)).place(x=130, y=640)
sign_up= Button(frame2,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8', command=signup_page).place(x=288, y=641)

login.resizable(False, False)
login.mainloop()