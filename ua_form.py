from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\uaers\Lenovo\Desktop\Mini Project f\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
    
def clear():
    date_entry.delete(0, END)
    uab_entry.delete(0, END)
    uau_entry.delete(0, END)
def submit():
    ua_forms.destroy()

ua_forms = CTk()
ua_forms.title("PulseAnalytics")
x = (ua_forms.winfo_screenwidth() - 650) // 2
y = (ua_forms.winfo_screenheight() - 450) // 2
ua_forms.geometry(f"650x450+{x}+{y}")
ua_forms.configure(bg="#000000")

frame1 = CTkFrame(master=ua_forms, fg_color="#96EFFF", corner_radiua=0, width=650,height=450)
frame1.place(x=0, y=0)

title_label = CTkLabel(master=frame1, text="Uric Acid Form", font=CTkFont('Microsoft YaHei UI Light',35,"bold",underline="true"))
title_label.place(relx=0.5, rely=0.15,anchor="center")

date_label = CTkLabel(master=frame1, text="Date:", font=CTkFont('Kanit Regular',20))
date_label.place(relx=0.1,rely=0.33)
date_entry = CTkEntry(master=frame1,corner_radiua=12,fg_color="#FFFFFF",border_width=0,placeholder_text="DD/MM/YYYY")
date_entry.place(relheight=0.08,relwidth=0.5,relx=0.4,rely=0.33)

uab_label = CTkLabel(master=frame1, text="Uric acid(Blood):", font=CTkFont('Kanit Regular',20))
uab_label.place(relx=0.1,rely=0.48)
uab_entry = CTkEntry(master=frame1,corner_radiua=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd")
uab_entry.place(relheight=0.08,relwidth=0.5,relx=0.4,rely=0.48)

uau_label = CTkLabel(master=frame1, text="Uric acid(Urine):", font=CTkFont('Kanit Regular',20))
uau_label.place(relx=0.1,rely=0.63)
uau_entry = CTkEntry(master=frame1,corner_radiua=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd")
uau_entry.place(relheight=0.08,relwidth=0.5,relx=0.4,rely=0.63)

submit_btn = CTkButton(master=frame1,text="Submit",corner_radiua=30,fg_color="#5FBDFF",hover_color="#7B66FF",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=submit)
submit_btn.place(relheight=0.08,relwidth=0.19,relx=0.65,rely=0.87,anchor="center")

clear_btn = CTkButton(master=frame1,text="Clear",corner_radiua=30,fg_color="transparent",hover_color="#FF2D3F",border_width=2,border_color="black",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=clear)
clear_btn.place(relheight=0.08,relwidth=0.18,relx=0.35,rely=0.87,anchor="center")




ua_forms.resizable(False, False)
ua_forms.mainloop()