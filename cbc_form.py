from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Lenovo\Desktop\Mini Project f\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
    
def clear():
    rbc_entry.delete(0, END)
    wbc_entry.delete(0, END)
    plt_entry.delete(0, END)
    hmg_entry.delete(0, END)
    hmt_entry.delete(0, END)
    mcv_entry.delete(0, END)

def submit():
    cbc_forms.destroy()

cbc_forms = CTk()
cbc_forms.title("PulseAnalytics")
x = (cbc_forms.winfo_screenwidth() - 650) // 2
y = (cbc_forms.winfo_screenheight() - 700) // 2
cbc_forms.geometry(f"650x700+{x}+{y}")
cbc_forms.configure(bg="#000000")

frame1 = CTkFrame(master=cbc_forms, fg_color="#96EFFF", corner_radius=0, width=650,height=700)
frame1.place(x=0, y=0)

title_label = CTkLabel(master=frame1, text="CBC Form", font=CTkFont('Microsoft YaHei UI Light',35,"bold",underline="true"))
title_label.place(relx=0.5, rely=0.1,anchor="center")

rbc_label = CTkLabel(master=frame1, text="RBC count:", font=CTkFont('Kanit Regular',20))
rbc_label.place(relx=0.1,rely=0.25)
rbc_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0)
rbc_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.25)

wbc_label = CTkLabel(master=frame1, text="WBC count:", font=CTkFont('Kanit Regular',20))
wbc_label.place(relx=0.1,rely=0.35)
wbc_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0)
wbc_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.35)

plt_label = CTkLabel(master=frame1, text="Platelet Level:", font=CTkFont('Kanit Regular',20))
plt_label.place(relx=0.1,rely=0.45)
plt_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0)
plt_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.45)

hmg_label = CTkLabel(master=frame1, text="Hemoglobin Level:", font=CTkFont('Kanit Regular',20))
hmg_label.place(relx=0.1,rely=0.55)
hmg_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0)
hmg_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.55)

hmt_label = CTkLabel(master=frame1, text="Hematocrit Level:", font=CTkFont('Kanit Regular',20))
hmt_label.place(relx=0.1,rely=0.65)
hmt_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0)
hmt_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.65)

mcv_label = CTkLabel(master=frame1, text="MCV Level:", font=CTkFont('Kanit Regular',20))
mcv_label.place(relx=0.1,rely=0.75)
mcv_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0)
mcv_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.75)


submit_btn = CTkButton(master=frame1,text="Submit",corner_radius=30,fg_color="#5FBDFF",hover_color="#7B66FF",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=submit)
submit_btn.place(relheight=0.06,relwidth=0.18,relx=0.65,rely=0.92,anchor="center")

clear_btn = CTkButton(master=frame1,text="Clear",corner_radius=30,fg_color="transparent",hover_color="#FF2D3F",border_width=2,border_color="black",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=clear)
clear_btn.place(relheight=0.06,relwidth=0.18,relx=0.35,rely=0.92,anchor="center")




cbc_forms.resizable(False, False)
cbc_forms.mainloop()