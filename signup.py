from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Lenovo\Desktop\Mini Project f\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


signup = CTk()
signup.title("Signup") 
x = (signup.winfo_screenwidth() - 1250) // 2
y = (signup.winfo_screenheight() - 768) // 2
signup.geometry(f"1250x768+{x}+{y}")
signup.configure(bg="#FFFFFF")

def login_page():
    signup.destroy()
    import login
    
def login_page2():
    pass1 = password.get()
    confirmpass = confirm_password.get()
    phoneno = phone.get()
    check = 0
    if pass1!=confirmpass :
        messagebox.showerror("Error","Password Mismatch")
        check+=1
    if len(phoneno)!=10 :
        messagebox.showerror("Error","Invalid Phone Number")
        check+=1
    if check==0:
        messagebox.showinfo("Success","Account Created Successfully !")
        signup.destroy()
        import login
        
        
    

frame1 = CTkFrame(master=signup, fg_color="#4c87ca", corner_radius=0, width=1250,height=768)
frame1.place(x=0, y=0)

background_image = PhotoImage(file=relative_to_assets("bgimg2.png"))
background_label = Label(frame1, image=background_image)
background_label.place(x=0, y=0, width=1250)
frame1.image = background_image


frame2 = CTkFrame( master=frame1, fg_color="#FFFFFF", corner_radius=30, height=700, width=700)
frame2.place( relx=0.25,y=35)

title1=CTkLabel(
    master=frame2,
    text="Create an Account",
    text_color="#000000",
    font=CTkFont(family="Microsoft YaHei UI Light", size=50,weight="bold")
)
title1.place(relx=0.51,y=65, anchor="center")

name = CTkEntry(
    master=frame2,
    corner_radius=50,
    width=400,
    height=50,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Name",
    font=CTkFont(family="Kanit Regular",size=20),
)
name.place(y=165,relx=0.51,anchor="center")

username = CTkEntry(
    master=frame2,
    corner_radius=50,
    width=400,
    height=50,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Login Id",
    font=CTkFont(family="Kanit Regular",size=20),
)
username.place(y=245,relx=0.51,anchor="center")

phone = CTkEntry(
    master=frame2,
    corner_radius=100,
    width=400,
    height=50,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Phone No",
    font=CTkFont(family="Kanit Regular",size=20)
)
phone.place(y=325,relx=0.51,anchor="center")

password = CTkEntry(
    master=frame2,
    corner_radius=50,
    width=400,
    height=50,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Password",
    font=CTkFont(family="Kanit Regular",size=20),)
password.place(y=405,relx=0.51,anchor="center")

confirm_password = CTkEntry(
    master=frame2,
    corner_radius=100,
    width=400,
    height=50,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Confirm Password",
    font=CTkFont(family="Kanit Regular",size=20)
)
confirm_password.place(y=485,relx=0.51,anchor="center")

btn1 = CTkButton(
    master=frame2,
    text="Sign Up",
    corner_radius=30,
    fg_color="#5FBDFF",
    hover_color="#7B66FF",
    width=150,
    height=60,
    font=CTkFont(size=20, weight="bold"),
    command=login_page2,
    text_color="#000000"
)
btn1.place(relx=0.5,y=585, anchor="center")

label=Label(frame2,text="Already have an account ?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9)).place(x=250, y=640)
log_in= Button(frame2,width=6,text='Login',border=0,bg='white',cursor='hand2',fg='#57a1f8', command=login_page).place(x=400, y=641)



signup.resizable(False,False)
signup.mainloop()