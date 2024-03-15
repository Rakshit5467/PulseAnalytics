from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Lenovo\Desktop\Mini Project f\assets")

cbc_graph = CTk()
cbc_graph.title("PulseAnalytics")
x = (cbc_graph.winfo_screenwidth() - 1250) // 2
y = (cbc_graph.winfo_screenheight() - 768) // 2
cbc_graph.geometry(f"1250x750+{x}+{y}")
cbc_graph.configure(bg="#000000")

frame1 = CTkScrollableFrame(master=cbc_graph, fg_color="#EBEEF6", corner_radius=0, width=1250,height=750)
frame1.place(relx=0, rely=0)


graphframe1 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe1.grid(row=0, column=0, pady=20, padx=12)

rbc_label = CTkLabel(master=graphframe1, text="RBC count:", font=CTkFont('Kanit Regular',30))
rbc_label.place(relx=0.5,rely=0.12,anchor='center')

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)
ax.plot(x, y, label='Sin(x)',color='blue',linewidth=2)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe1)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')

graphframe2 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe2.grid(row=0, column=1, pady=20, padx=12)

wbc_label = CTkLabel(master=graphframe2, text="WBC count:", font=CTkFont('Kanit Regular',30))
wbc_label.place(relx=0.5,rely=0.12,anchor='center')

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)
ax.plot(x, y, label='Sin(x)',color='blue',linewidth=2)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe2)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')

graphframe3 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe3.grid(row=1, column=0, pady=20, padx=12)

graphframe4 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe4.grid(row=1, column=1, pady=20, padx=12)

graphframe5 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe5.grid(row=2, column=0, pady=20, padx=12)

graphframe6 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe6.grid(row=2, column=1, pady=20, padx=12)





cbc_graph.resizable(False, False)
cbc_graph.mainloop()