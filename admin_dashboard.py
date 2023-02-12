from pathlib import Path
from tkinter import Tk, Canvas, Entry,  Button, PhotoImage, messagebox
from tkinter.constants import BOTH, LEFT, YES
from tkinter import *
import tkinter as tk
from datetime import datetime
import cx_Oracle as oc
from matplotlib.pyplot import text
con = oc.connect('zoom/admin@localhost:1521/xe')
cursor= con.cursor()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./admindashboard_assets")

#====================================================Functions=================================================================================================#
#==============================================================================================================================================================#

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def ttf():
    window.destroy()
    import admin_tt

def compf():
    window.destroy()
    import admin_complaint  

def entryf():
    window.destroy()
    import admin_entry  

def logout():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
        cursor.execute("UPDATE admin_log SET log_out=sysdate where uname= '{}'".format(s1))
        con.commit()
        window.destroy()
        import admin_login
    else:
        messagebox.showinfo('Return','You will now return to the application screen')
    

#==============================================================================================================================================================#
#==========================================================Window==============================================================================================#

#window
window = Tk()
window.title("ONLINE CLASS AUTOMATION")
window.geometry("1536x864+0+0")
fullScreenState = False
window.attributes("-fullscreen", fullScreenState)
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d" % (w, h))
window.configure(bg = "#FFFFFF")

#==============================================================================================================================================================#
#==========================================================Canvas==============================================================================================#

#texts and title 
canvas = Canvas(window,bg = "#FFFFFF",height = 864,width = 1536,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.pack(fill= BOTH,expand=YES)
canvas.create_rectangle(0.0,1.0,1936.0,140.0,fill="#1C1C28",outline="")
cursor.execute("select * from (select uname from admin_log order by log_in desc) where rownum=1")
s=cursor.fetchone()
s1=str(s[0])
print(s1)
n=StringVar()
n.set(s)
uname_l=Label(window, textvariable=n,fg="#1C1C28",bg='white', font=("Inter", 14,'bold')).place(x=74,y=910)
canvas.create_text(95.0,950.0,anchor="nw",text="Online",fill="#1C1C28",font=("Inter Light", 18 * -1))
canvas.create_text(31.0,158.0,anchor="nw",text="Main",fill="#1C1C28",font=("Inter Medium", 20 * -1))
canvas.create_text(403.0,48.0,anchor="nw",text="Dashboard",fill="#FFFFFF",font=("Inter Bold", 30 * -1))
canvas.create_text(59.0,35.0,anchor="nw",text="Online Class\nAutomation.",fill="#FFFFFF",font=("Inter Bold", 30 * -1))

#search bar
search_image = PhotoImage(file=relative_to_assets("entry_5.png"))
search_bg = canvas.create_image(1550.0,75,image=search_image)
search = Entry(bd=0,bg="#FFFFFF",highlightthickness=0)
search.place(x=1410.0,y=60,width=284.0,height=33.0)

#===========================================================Buttons============================================================================================#
#==============================================================================================================================================================#

#buttons
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: print("button_1 clicked"),relief="flat")
button_1.place(x=1750.0,y=50.0,width=50.0,height=50.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=logout,relief="flat")
button_2.place(x=1830.0,y=50.0,width=50.0,height=50.0)

retpassword_image = PhotoImage(file=relative_to_assets("button_3.png"))
retpass = Button(image=retpassword_image,borderwidth=0,highlightthickness=0,command=lambda: print("retrieve password"),relief="flat")
retpass.place(x=19.0,y=389.0,width=280.0,height=40.0)

dashboard_image = PhotoImage(file=relative_to_assets("dashboard.png"))
dashboard = Button(image=dashboard_image,borderwidth=0,highlightthickness=0,command=lambda: print("dashboard"),relief="flat")
dashboard.place(x=19.0,y=194.0,width=280.0,height=40.0)

complaints_image1 = PhotoImage(file=relative_to_assets("button_5.png"))
complaints1 = Button(image=complaints_image1,borderwidth=0,highlightthickness=0,command=compf,relief="flat")
complaints1.place(x=19.0,y=243.0,width=280.0,height=40.0)

tt_image = PhotoImage(file=relative_to_assets("button_10.png"))
tt = Button(image=tt_image,borderwidth=0,highlightthickness=0,command=ttf,relief="flat")            
tt.place(x=19.0,y=292.0,width=280.0,height=40.0)

entry_image = PhotoImage(file=relative_to_assets("button_6.png"))
entry = Button(image=entry_image,borderwidth=0,highlightthickness=0,command=entryf,relief="flat")
entry.place(x=20.0,y=341.0,width=280.0,height=40.0)

#===========================================================users==============================================================================================#
#==============================================================================================================================================================#

canvas.create_text(1050.0,180.0,anchor="nw",text="Users Online",fill="#1C1C28",font=("Inter",15))
c1 = Canvas(window,bg = "#FFFFFF",height = 700,width =600 ,bd = 0,highlightthickness = 0,relief = "ridge")
c1.place(x=600, y=270)


Label1 = Label(c1, text="Username", width=36,height=3,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label1.grid(row=0, column=0)
Label2 = Label(c1, text="Course", width=32,height=3,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label2.grid(row=0, column=1)
Label3 = Label(c1, text="Semester", width=32,height=3,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label3.grid(row=0, column=2) 
cursor.execute("select distinct u.uname, u.course, u.sem from user_tb u, log l where u.uname = l.uname and log_out IS NULL order by u.sem asc")
con.commit()
data=cursor.fetchall()

for i, ind in enumerate(data):
        Label(c1, text=ind[0],width=40,height=2,font=('Arial',10),background='white', relief="sunken").grid(row=i+1, column=0)
        Label(c1, text=ind[1], width=35,height=2,font=('Arial',10),background='white',relief="sunken").grid(row=i+1, column=1)
        Label(c1, text=ind[2], width=35,height=2,font=('Arial',10),background='white',relief="sunken").grid(row=i+1, column=2)




#==============================================================================================================================================================#
#==============================================================================================================================================================#

window.mainloop()