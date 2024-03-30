from customtkinter import *
from pathlib import Path
from tkinter import *
import pymysql

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Lenovo\Desktop\Mini Project f\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def fetch_empids_from_database():
    conn = pymysql.connect(host='localhost', user='root', password='MH46AL5586', database='world')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Code FROM country limit 10")  # Fetch unique empids from the table
    ids = [emp_id[0] for emp_id in cursor.fetchall()]  # Extract empids from the fetched data
    conn.close()
    return ids

def fetch_row_from_database(empid_value):
    conn = pymysql.connect(host='localhost', user='root', password='MH46AL5586', database='world')
    cursor = conn.cursor()
    cursor.execute("select SurfaceArea,Population,LifeExpectancy,GNP,GNPOld,Capital from country where Code=%s", (empid_value,))
    row = cursor.fetchone()  # Fetch the first row that matches the empid
    conn.close()
    return row

def on_empid_selected():
    selected_empid = empid_var.get()
    row = fetch_row_from_database(selected_empid)
    if row:
        for i, value in enumerate(row[0:]):  # Skip the empid value (first column)
            text_fields[i].configure(state='normal')
            text_fields[i].delete(0, END)
            text_fields[i].insert(END, str(value) + "   " + units[i])
            text_fields[i].configure(state='readonly')
            if value >= lower[i] and value <= upper[i]:
                range_fields[i].configure(text="Normal", text_color="#00FF00")
            elif value > upper[i]:
                range_fields[i].configure(text="High", text_color="#FF0000")
                consult_field = CTkLabel(master=bottom_frame, text=consult_high[i], font=CTkFont('Kanit Regular', 18))
                consult_field.grid(column=1, row=1+len(consultations), sticky='w')
                consultations.append(consult_field)
            else:
                range_fields[i].configure(text="Low", text_color="#B01200")
                consult_field = CTkLabel(master=bottom_frame, text=consult_low[i], font=CTkFont('Kanit Regular', 18))
                consult_field.grid(column=1, row=1+len(consultations), sticky='w')
                consultations.append(consult_field)
            
    else:
        # Clear text fields if no matching row found
        for i, text_field in enumerate(text_fields):  # Fix is here
            text_field.configure(state='normal')
            text_field.delete(0, END)
            text_field.configure(state='readonly')
        

units=["10^6/µL","10^3/µL","10^3/µL","g/dL","%","fL"]

cbc_archive = CTk()
cbc_archive.title("PulseAnalytics")
x = (cbc_archive.winfo_screenwidth() - 900) // 2
y = (cbc_archive.winfo_screenheight() - 800) // 2
cbc_archive.geometry(f"900x800+{x}+{y}")
cbc_archive.configure(bg="#000000")

frame1 = CTkFrame(master=cbc_archive, fg_color="#EBEEF6", corner_radius=0, width=900,height=800)
frame1.place(x=0, y=0)

title = CTkLabel(master=frame1, text="CBC Archive", font=CTkFont('Typogaphy',35))
title.place(relx=0.5, rely=0.06,anchor='center')

top_frame = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20)
top_frame.place(relheight=0.06,relwidth=0.3,relx=0.5,rely=0.15,anchor='center')

months_label1 = CTkLabel(master=top_frame,text="Month-Year:",font=CTkFont('Kanit Regular', 16))
months_label1.place(relx=0.24,rely=0.5,anchor='center')
empid_var = StringVar()
empids = fetch_empids_from_database()
empid_dropdown = CTkComboBox(master=top_frame, variable=empid_var, values=[str(i) for i in empids], border_width=0, dropdown_fg_color="#FFFFFF", dropdown_hover_color="#EBEEF6", fg_color="#FFFFFF", corner_radius=10, button_color="#FFFFFF", button_hover_color="#EBEEF6")
empid_dropdown.place(relx=0.7, rely=0.5, anchor=CENTER)
empid_var.trace('w', lambda *args: on_empid_selected())

mid_frame = CTkFrame(master=frame1, fg_color="#BFACE2", corner_radius=20,)
mid_frame.place(relheight=0.55,relwidth=0.9,relx=0.05,rely=0.2)

text_fields = []
range_fields = []
consultations = []
consult_high = ["RBC is high. Ensure adequate hydration.",
                "WBC is high. High WBC count may indicate infection or inflammation.",
                "Platelet count is high. High Platelet count may indicate an underlying condition.",
                "Haemoglobin is high. Consult a doctor to investigate potential causes.",
                "Hematocrit is high. Ensure adequate hydration.",
                "MCV is high. Consult a doctor for further evaluation."]

consult_low = ["RBC is low. Eat vegetables rich in iron.",
               "WBC is low. Improve immune system by eating a balanced diet and getting enough sleep.",
               "Platelet count is low. Avoid activities that could cause injury and consult a doctor.",
               "Haemoglobin is low. Eat iron-rich foods such as spinach and red meat.",
               "Hematocrit is low. Increase iron intake or consult a doctor.",
               "MCV is low. Increase intake of foods rich in iron or consult a doctor."]

for i in range(6):
    text_field = CTkEntry(master=mid_frame, border_width=0, fg_color="#FFFFFF", corner_radius=20)
    text_field.place(relx=0.31, rely=0.1+(i*0.15), relheight=0.08, relwidth=0.25)
    text_fields.append(text_field)
    
lower = [4,4,150,12,38,80]
upper = [4.5,10,400,16,52,100]

rbc_label = CTkLabel(master=mid_frame, text="RBC Count:", font=CTkFont('Kanit Regular', 20))
rbc_label.place(relx=0.07, rely=0.1)
rbc_range = CTkLabel(master=mid_frame, text=("(Normal: " + str(lower[0]) + "-" + str(upper[0]) +" "+ units[0] + ")"), font=CTkFont('Kanit Regular', 15))
rbc_range.place(relx=0.74, rely=0.1)
range = CTkLabel(master=mid_frame, text="NA", font=CTkFont('Kanit Regular', 17))
range.place(relx=0.64, rely=0.1)
range_fields.append(range)

wbc_label = CTkLabel(master=mid_frame,text="WBC Count:",font=CTkFont('Kanit Regular', 20))
wbc_label.place(relx=0.07,rely=0.25)
wbc_range = CTkLabel(master=mid_frame, text=("(Normal: " + str(lower[1]) + "-" + str(upper[1]) +" "+ units[1] + ")"), font=CTkFont('Kanit Regular', 15))
wbc_range.place(relx=0.74, rely=0.25)
range = CTkLabel(master=mid_frame, text="NA", font=CTkFont('Kanit Regular', 17))
range.place(relx=0.64, rely=0.25)
range_fields.append(range)

plt_label = CTkLabel(master=mid_frame,text="Platelet Level:",font=CTkFont('Kanit Regular', 20))
plt_label.place(relx=0.07,rely=0.4)
plt_range = CTkLabel(master=mid_frame, text=("(Normal: " + str(lower[2]) + "-" + str(upper[2]) +" "+ units[2] + ")"), font=CTkFont('Kanit Regular', 15))
plt_range.place(relx=0.74, rely=0.4)
range = CTkLabel(master=mid_frame, text="NA", font=CTkFont('Kanit Regular', 17))
range.place(relx=0.64, rely=0.4)
range_fields.append(range)

hmg_label = CTkLabel(master=mid_frame,text="Heamoglobin Level:",font=CTkFont('Kanit Regular', 20))
hmg_label.place(relx=0.07,rely=0.55)
hmg_range = CTkLabel(master=mid_frame, text=("(Normal: " + str(lower[3]) + "-" + str(upper[3]) +" "+ units[3] + ")"), font=CTkFont('Kanit Regular', 15))
hmg_range.place(relx=0.74, rely=0.55)
range = CTkLabel(master=mid_frame, text="NA", font=CTkFont('Kanit Regular', 17))
range.place(relx=0.64, rely=0.55)
range_fields.append(range)

hmt_label = CTkLabel(master=mid_frame,text="Hematocrit Level:",font=CTkFont('Kanit Regular', 20))
hmt_label.place(relx=0.07,rely=0.7)
hmt_range = CTkLabel(master=mid_frame, text=("(Normal: " + str(lower[4]) + "-" + str(upper[4]) +" "+ units[4] + ")"), font=CTkFont('Kanit Regular', 15))
hmt_range.place(relx=0.74, rely=0.7)
range = CTkLabel(master=mid_frame, text="NA", font=CTkFont('Kanit Regular', 17))
range.place(relx=0.64, rely=0.7)
range_fields.append(range)

mcv_label = CTkLabel(master=mid_frame,text="MCV Level:",font=CTkFont('Kanit Regular', 20))
mcv_label.place(relx=0.07,rely=0.85)
mvc_range = CTkLabel(master=mid_frame, text=("(Normal: " + str(lower[5]) + "-" + str(upper[5]) +" "+ units[5] + ")"), font=CTkFont('Kanit Regular', 15))
mvc_range.place(relx=0.74, rely=0.85)
range = CTkLabel(master=mid_frame, text="NA", font=CTkFont('Kanit Regular', 17))
range.place(relx=0.64, rely=0.85)
range_fields.append(range)


bottom_frame = CTkScrollableFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20)
bottom_frame.place(relheight=0.195,relwidth=0.9,relx=0.5,rely=0.88,anchor='center')


cbc_archive.resizable(False, False)
cbc_archive.mainloop()