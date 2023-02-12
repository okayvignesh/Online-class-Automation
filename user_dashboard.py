from pathlib import Path
from threading import Thread
from tkinter import Tk, messagebox, Canvas,  Button, PhotoImage
from tkinter import *
from tkinter import ttk
import tkinter as tk
from datetime import datetime
import cx_Oracle as oc
import webbrowser
import time

con = oc.connect('zoom/admin@localhost:1521/xe')
cursor= con.cursor()
cursor2= con.cursor()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./dashboard_assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

 

def complaintf():
    window.destroy()
    import user_complaints

def logout():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
        cursor.execute("UPDATE log SET log_out=sysdate where uname= '{}'".format(s1))
        con.commit()
        window.destroy()
        import user_login
    else:
        messagebox.showinfo('Return','You will now return to the application screen')





window = Tk()
window.title("ONLINE CLASS AUTOMATION")
window.geometry("1536x864+0+0")
fullScreenState = False
window.attributes("-fullscreen", fullScreenState)
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d" % (w, h))
window.configure(bg = "#FFFFFF")


canvas = Canvas(window,bg = "#FFFFFF",height = 864,width = 1536,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.pack(fill= BOTH,expand=YES)
canvas.create_rectangle(0.0,1.0,1936.0,140.0,fill="#1C1C28",outline="")
canvas.create_text(403.0,48.0,anchor="nw",text="Dashboard",fill="#FFFFFF",font=("Inter", 30 * -1,'bold'))
cursor.execute("select * from (select uname from log order by log_in desc) where rownum=1")
s=cursor.fetchone()
s1=str(s[0])

cursor.execute("select course,section, sem from user_tb where uname='{}'".format(s1))
css=cursor.fetchone()

course=str(css[0])
section=str(css[1])
semester=str(css[2])

n=StringVar()
n.set(s)
uname_l=Label(window, textvariable=n,fg="#1C1C28",bg='white', font=("Inter", 14,'bold')).place(x=74,y=930)
canvas.create_text(90.0,960.0,anchor="nw",text="Online",fill="#1C1C28",font=("Inter Light", 18 * -1))
canvas.create_text(900.0,200.0,anchor="nw",text="Today's Time Table",fill="#1C1C28",font=("Inter", 30 * -1,'bold'))
canvas.create_text(31.0,158.0,anchor="nw",text="Main",fill="#1C1C28",font=("InterMedium", 20 * -1))

day=datetime.today().strftime('%A')
sql2=" select link,start_time from tt_tb where course='{}' and sem={} and section='{}' and dow='{}'".format(course,semester,section,day)
cursor2.execute(sql2)
dat = cursor2.fetchall()
currentTime = time.strftime("%H:%M")




items = [store[1] for store in dat]
link = [store[0] for store in dat]
def start():
    try:
        for i in range(len(items)):
                if (items[i]==currentTime):
                    webbrowser.open(link[i])
                    break
        else:
            messagebox.showerror("ERROR","Class not started")
    except ValueError as cal :
        print(cal)



sql= "select start_time,subject,fac from tt_tb where dow='{}' and course='{}' and section='{}' and sem='{}' order by start_time asc".format(day,course,section,semester)
cursor.execute(sql)
data = cursor.fetchall()
f=Frame(window)
f.place(x=700, y=350)
Label1 = Label(f, text="HOUR", background='#7373A8',width=30,height=3,font=('Inter',8),relief="sunken")
Label1.grid(row=0, column=0)
Label2 = Label(f, text="SUBJECT", background='#7373A8',width=30,height=3,font=('Inter',8),relief="sunken")
Label2.grid(row=0, column=1)
Label3 = Label(f, text="FACULTY", background='#7373A8',width=30,height=3,font=('Inter',8),relief="sunken")
Label3.grid(row=0, column=2)
#for index,dat in data:
for i, ind in enumerate(data):
    Label(f, text=ind[0],width=30,height=2,font=('Inter',8), relief="sunken").grid(row=i+1, column=0)
    Label(f, text=ind[1], width=30,height=2,font=('Inter',8),relief="sunken").grid(row=i+1, column=1)
    Label(f, text=ind[2], width=30,height=2,font=('Inter',8),relief="sunken").grid(row=i+1, column=2)



def ref():

    sql= "select start_time,subject,fac from tt_tb where dow='{}' and course='{}' and section='{}' and sem='{}' order by start_time asc".format(day,course,section,semester)
    cursor.execute(sql)
    data = cursor.fetchall()

    f=Frame(window)
    f.place(x=700, y=350)
    Label1 = Label(f, text="HOUR", background='#7373A8',width=30,height=3,font=('Inter',8),relief="sunken")
    Label1.grid(row=0, column=0)
    Label2 = Label(f, text="SUBJECT", background='#7373A8',width=30,height=3,font=('Inter',8),relief="sunken")
    Label2.grid(row=0, column=1)
    Label3 = Label(f, text="FACULTY", background='#7373A8',width=30,height=3,font=('Inter',8),relief="sunken")
    Label3.grid(row=0, column=2)
    #for index,dat in data:
    for i, ind in enumerate(data):
        Label(f, text=ind[0],width=30,height=2,font=('Inter',8), relief="sunken").grid(row=i+1, column=0)
        Label(f, text=ind[1], width=30,height=2,font=('Inter',8),relief="sunken").grid(row=i+1, column=1)
        Label(f, text=ind[2], width=30,height=2,font=('Inter',8),relief="sunken").grid(row=i+1, column=2)


search_image = PhotoImage(file=relative_to_assets("entry_5.png"))
search_bg = canvas.create_image(1550.0,75,image=search_image)
search = Entry(bd=0,bg="#FFFFFF",highlightthickness=0)
search.place(x=1410.0,y=60,width=284.0,height=33.0)
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: print("button_1 clicked"),relief="flat")
button_1.place(x=1750.0,y=50.0,width=50.0,height=50.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=logout,relief="flat")
button_2.place(x=1830.0,y=50.0,width=50.0,height=50.0)



comp_image = PhotoImage(file=relative_to_assets("button_3.png"))
comp = Button(image=comp_image,borderwidth=0,highlightthickness=0,command=complaintf,relief="flat")
comp.place(x=19.0,y=243.0,width=280.0,height=40.0)

reports_image = PhotoImage(file=relative_to_assets("button_4.png"))
reports = Button(image=reports_image,borderwidth=0,highlightthickness=0,command=lambda: print("button_4 clicked"),relief="flat")
reports.place(x=19.0,y=292.0,width=280.0,height=40.0)

contad_image = PhotoImage(file=relative_to_assets("button_5.png"))
contad = Button(image=contad_image,borderwidth=0,highlightthickness=0,command=lambda: print("button_5 clicked"),relief="flat")
contad.place(x=19.0,y=341.0,width=280.0,height=40.0)

dash_image = PhotoImage(file=relative_to_assets("button_6.png"))
dash = Button(image=dash_image,borderwidth=0,highlightthickness=0, command=lambda: print("button_6 clicked"),relief="flat")
dash.place(x=19.0,y=194.0,width=280.0,height=40.0)

#start buttons
play_image = PhotoImage(file=relative_to_assets("play.png"))
play = Button(image=play_image,borderwidth=0,highlightthickness=0, command=start,relief="flat")
play.place(x=1500,y=380.0)

ref_image = PhotoImage(file=relative_to_assets("refresh.png"))
refresh = Button(image=ref_image,borderwidth=0,highlightthickness=0,command=ref,relief="flat")
refresh.place(x=1500.0,y=430.0)

#start buttons end

canvas.create_text(63.0,35.0,anchor="nw",text="Online Class\nAutomation.",fill="#FFFFFF",font=("Inter", 30 * -1,'bold'))
canvas.create_rectangle(68.0,351.0,88.0,371.0,fill="#000000",outline="")

#window.resizable(False, False)
window.mainloop()

