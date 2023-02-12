from os import P_DETACH
from pathlib import Path
from platform import python_branch
from tkinter import *
from tkinter import ttk
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from turtle import back
import cx_Oracle as oc
con = oc.connect('zoom/admin@localhost:1521/xe')
cursor = con.cursor()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./admintt_assets")

#====================================================Functions=================================================================================================#
#==============================================================================================================================================================#

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def dash():
    window.destroy()
    import admin_dashboard

def comp():
    window.destroy()
    import admin_complaint

def entryf():
    window.destroy()
    import admin_entry

def add():
    c=n1.get()
    sems=n2.get()
    secs=n3.get()
    dow=n4.get()
    pd =n5.get()
    sbt=n6.get()
    fac=n7.get()
    lk=n8.get()
    sql= "INSERT INTO tt_tb VALUES ('{}',{},'{}','{}','{}','{}','{}','{}')".format(c,sems,secs,dow,pd,sbt,fac,lk)
    messagebox.showinfo("SUCCESS","Sucessfully updated")

    try:
        cursor.execute(sql)
        con.commit()
    except oc.DatabaseError as d:
        print("Error inserting data",d)
    finally:
        None

def clear():
        spn1.set('')
        spn2.set('')
        spn3.set('')
        spn4.set('')
        spn5.set('')
        spn8.set('')

def logout():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
        cursor.execute("UPDATE admin_log SET log_out=sysdate where uname= '{}'".format(s1))
        con.commit()
        con.close()
        window.destroy()
        import admin_login
    else:
        messagebox.showinfo('Return','You will now return to the application screen')


#==============================================================================================================================================================#
#==========================================================Window==============================================================================================#

window = tk.Tk()
window.title("ONLINE CLASS AUTOMATION")
window.geometry("1536x864+0+0")
fullScreenState = False
window.attributes("-fullscreen", fullScreenState)       
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d" % (w, h))
window.configure(bg = "#FFFFFF")

#==============================================================================================================================================================#
#==========================================================Canvas==============================================================================================#

canvas = Canvas(window,bg = "#FFFFFF",height = 864,width = 1536,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.pack(fill= BOTH,expand=YES)
canvas.create_rectangle(0.0,0.0,1936.0,139.0,fill="#1C1C28",outline="")
canvas.create_text(403.0,48.0,anchor="nw",text="Time Table",fill="#FFFFFF",font=("Inter Bold", 30 * -1))
canvas.create_text(60.0,35.0,anchor="nw",text="Online Class\nAutomation.",fill="#FFFFFF",font=("Inter Bold", 30 * -1))  
canvas.create_text(900.0,470.0,anchor="nw",text="View Time table",fill="#1C1C28",font=("Inter", 16,'bold'))
cursor.execute("select * from (select uname from admin_log order by log_in desc) where rownum=1")
s=cursor.fetchone()
s1=str(s[0])
print(s1)
n=StringVar()
n.set(s)
uname_l=Label(window, textvariable=n,fg="#1C1C28",bg='white', font=("Inter", 14,'bold')).place(x=74,y=910)
canvas.create_text(95.0,950.0,anchor="nw",text="Online",fill="#1C1C28",font=("Inter Light", 18 * -1))
canvas.create_text(32.0,158.0,anchor="nw",text="Main",fill="#1C1C28",font=("Inter Medium", 20 * -1))


#==============================================================================================================================================================#
#==========================================================refresh==============================================================================================#

def ref():
    semester=m2.get()
    section=m3.get()
    course=m1.get()
    sql= "select * from tt_tb where sem={} and course ='{}' and section='{}' order by subject asc".format(semester,course, section)
    cursor.execute(sql)
    con.commit()
    data = cursor.fetchall()
    if data == []:
        messagebox.showerror('ERROR','No records found')
    else:
        global f2
        f2=Frame(window, height=600)
        f2.place(x=450, y=600)
        Label1 = Label(f2, text="Course", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
        Label1.grid(row=0, column=0)
        Label2 = Label(f2, text="Semester", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
        Label2.grid(row=0, column=1)
        Label3 = Label(f2, text="Section", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
        Label3.grid(row=0, column=2)    
        Label4 = Label(f2, text="Weekday", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
        Label4.grid(row=0, column=3)
        Label5 = Label(f2, text="Hour", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
        Label5.grid(row=0, column=4)
        Label6 = Label(f2, text="Subject", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
        Label6.grid(row=0, column=5)
        Label7= Label(f2, text="Faculty", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
        Label7.grid(row=0, column=6)
        sql= "select * from tt_tb where sem={} and course ='{}' and section='{}' order by start_time asc".format(semester,course, section)
        cursor.execute(sql)
        con.commit()
        data = cursor.fetchall()
        if data == []:
            messagebox.showerror('ERROR','No records found')
        else:
    #for index,dat in data:
            for i, ind in enumerate(data):  
                Label(f2, text=ind[0],width=20,height=2,font=('Inter',8),background='white', relief="sunken").grid(row=i+1, column=0)
                Label(f2, text=ind[1], width=20,height=2,font=('Inter',8),background='white',relief="sunken").grid(row=i+1, column=1)
                Label(f2, text=ind[2], width=20,height=2,font=('Inter',8),background='white',relief="sunken").grid(row=i+1, column=2)
                Label(f2, text=ind[3],width=20,height=2,font=('Inter',8),background='white', relief="sunken").grid(row=i+1, column=3)
                Label(f2, text=ind[4], width=20,height=2,font=('Inter',8),background='white',relief="sunken").grid(row=i+1, column=4)
                Label(f2, text=ind[5], width=20,height=2,font=('Inter',8),background='white',relief="sunken").grid(row=i+1, column=5)
                Label(f2, text=ind[6],width=20,height=2,font=('Inter',8),background='white', relief="sunken").grid(row=i+1, column=6)


global f1
f1=Frame(window, height=600)
f1.place(x=450, y=600)
Label1 = Label(f1, text="Course", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
Label1.grid(row=0, column=0)
Label2 = Label(f1, text="Semester", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
Label2.grid(row=0, column=1)
Label3 = Label(f1, text="Section", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
Label3.grid(row=0, column=2)    
Label4 = Label(f1, text="Weekday", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
Label4.grid(row=0, column=3)
Label5 = Label(f1, text="Hour", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
Label5.grid(row=0, column=4)
Label6 = Label(f1, text="Subject", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
Label6.grid(row=0, column=5)
Label7= Label(f1, text="Faculty", width=20,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
Label7.grid(row=0, column=6)
sql= "select * from tt_tb order by start_time asc"
cursor.execute(sql)
con.commit()
data = cursor.fetchall()
if data == []:
    messagebox.showerror('ERROR','No records found')
else:
#for index,dat in data:
    for i, ind in enumerate(data):  
        Label(f1, text=ind[0],width=20,height=2,font=('Inter',8),background='white', relief="sunken").grid(row=i+1, column=0)
        Label(f1, text=ind[1], width=20,height=2,font=('Inter',8),background='white',relief="sunken").grid(row=i+1, column=1)
        Label(f1, text=ind[2], width=20,height=2,font=('Inter',8),background='white',relief="sunken").grid(row=i+1, column=2)
        Label(f1, text=ind[3],width=20,height=2,font=('Inter',8),background='white', relief="sunken").grid(row=i+1, column=3)
        Label(f1, text=ind[4], width=20,height=2,font=('Inter',8),background='white',relief="sunken").grid(row=i+1, column=4)
        Label(f1, text=ind[5], width=20,height=2,font=('Inter',8),background='white',relief="sunken").grid(row=i+1, column=5)
        Label(f1, text=ind[6],width=20,height=2,font=('Inter',8),background='white', relief="sunken").grid(row=i+1, column=6)


ref_image = PhotoImage(file=relative_to_assets("refresh.png"))
refresh = Button(image=ref_image,borderwidth=0,highlightthickness=0,command=ref,relief="flat")
refresh.place(x=1650.0,y=600.0)

sem=Label(window,text="Semester",foreground="#1C1C28",bg='white',  font=("Inter", 10 )).place(x=450,y=510)
global m2
m2=IntVar()
spn2=ttk.Combobox(window,width=20,state='readonly',textvariable=m2,font=("Inter", 15 * -1))
spn2['values']=(1,2,3,4,5,6,7,8)
spn2.place(x=450.0,y=540,width=180.0,height=40)


cour=Label(window,text="Course",foreground="#1C1C28",bg='white',font=("Inter", 10 )).place(x=760, y=510)
global m1
m1=StringVar()
sem_g=m2.get()
cursor.execute("Select distinct(course) from sub_fac")
con.commit()
courdata=[]
res=cursor.fetchall()
for i in res:
    courdata.append(i[0])
spn1=ttk.Combobox(window,width=20,state='readonly',textvariable=m1,font=("Inter", 15 * -1))
spn1['values']=courdata
spn1.place(x=760.0,y=540,width=180.0,height=40)


sec= Label(window,text="Section",foreground="#1C1C28",bg='white',font=("Inter", 10 )).place(x=1080, y=510)
global m3
m3=StringVar()
spn3=ttk.Combobox(window,width=20,state='readonly',textvariable=m3,font=("Inter", 15 * -1))
spn3['values']=('A',
              'B',
              'C',
              'D')
spn3.place(x=1080.0,y=540,width=180.0,height=40)

#==============================================================================================================================================================#
#==========================================================edit button=========================================================================================#

def updatef():
    c=n1.get()
    sems=n2.get()
    secs=n3.get()
    dow=n4.get()
    pd =n5.get()
    sbt=n6.get()
    print(pd)
    cursor.execute("delete from tt_tb where course='{}' and sem={} and section='{}' and dow='{}' and start_time='{}' and subject='{}'".format(c,sems,secs,dow,pd,sbt))
    con.commit()
    messagebox.showinfo("SUCCESS","Sucessfully updated")



def editf():
    d.destroy()
    add_tt.destroy()
    d1=Label(f, text="Edit Timetable", font=("Inter", 15), anchor=CENTER, bg='white')
    d1.place(x=500, y=0)


update_image = PhotoImage(file=relative_to_assets("delete_button.png"))
update_tt = Button(image=update_image,borderwidth=0,highlightthickness=0,command=updatef,relief="flat")
update_tt.place(x=1650.0,y=280.0)


close_image = PhotoImage(file=relative_to_assets("close.png"))
close = Button(image=close_image,borderwidth=0,highlightthickness=0,command= lambda:(f2.destroy(),f1.destroy()),relief="flat")
close.place(x=1650.0,y=700.0)

edit_image = PhotoImage(file=relative_to_assets("edit.png"))
edit = Button(image=edit_image,borderwidth=0,highlightthickness=0,command=editf,relief="flat")
edit.place(x=1650.0,y=650.0)

#view_image = PhotoImage(file=relative_to_assets("view.png"))
#view = Button(image=view_image,borderwidth=0,highlightthickness=0,command=viewf,relief="flat")
#view.place(x=1400.0,y=540)

#==============================================================================================================================================================#
#==========================================================dropdown==============================================================================================#


f=Frame(canvas,width=1500, height=230, background='white')
f.place(x=400, y=190)
d=Label(f, text="Define Timetable", font=("Inter", 15), anchor=CENTER, bg='white')
d.place(x=500, y=0)

sem=Label(f,text="Semester",foreground="#1C1C28",bg='white',  font=("Inter", 10 )).place(x=50,y=55)
n2=IntVar()
spn2=ttk.Combobox(f,width=20,state='readonly',textvariable=n2,font=("Inter", 15 * -1))
spn2['values']=(1,2,3,4,5,6,7,8)
spn2.place(x=50.0,y=80.9,width=180.0,height=40)
spn2.current(0)

cour=Label(f,text="Course",foreground="#1C1C28",bg='white',font=("Inter", 10 )).place(x=350, y=55)
n1=StringVar()
cursor.execute("Select distinct(course) from sub_fac")
con.commit()
courdata=[]
res=cursor.fetchall()
for i in res:
    courdata.append(i[0])
spn1=ttk.Combobox(f,width=20,state='readonly',textvariable=n1,font=("Inter", 15 * -1))
spn1['values']=courdata
spn1.place(x=350.0,y=80.9,width=180.0,height=40)

sec= Label(f,text="Section",foreground="#1C1C28",bg='white',font=("Inter", 10 )).place(x=670, y=55)
n3=StringVar()
spn3=ttk.Combobox(f,width=20,state='readonly',textvariable=n3,font=("Inter", 15 * -1))
spn3['values']=('A',
              'B',
              'C',
              'D')
spn3.place(x=670.0,y=80.9,width=180.0,height=40)

day= Label(f,text="Weekday",foreground="#1C1C28",bg='white',font=("Inter", 10 )).place(x=1000, y=55)
n4=StringVar()
spn4=ttk.Combobox(f,width=20,state='readonly',textvariable=n4,font=("Inter", 15 * -1))
spn4['values']=('Monday',
              'Tuesday',
              'Wednesday',
              'Thursday',
              'Friday', 
              'Saturday')
spn4.place(x=1000.0,y=80.9,width=180.0,height=40)

perd= Label(f,text="Start Time (HH:MM)",foreground="#1C1C28",bg='white',font=("Inter", 10 )).place(x=50, y=145)
n5=StringVar()
spn5=ttk.Combobox(f,width=20,textvariable=n5,font=("Inter", 15 * -1))
spn5['values']=None
spn5.place(x=50.0,y=170.9,width=180.0,height=40)


subj= Label(f,text="Subject",foreground="#1C1C28",bg='white',font=("Inter", 10 )).place(x=350, y=145)
n6=StringVar()
def selectf():
    semester=n2.get()
    course=n1.get()
    sql="Select subject from sub_fac where sem={} and course ='{}'".format(semester,course)
    cursor.execute(sql)
    con.commit()
    subdata=[]
    res=cursor.fetchall()
    for i in res:
        subdata.append(i[0])
    if subdata==[]:
        messagebox.showwarning('Error','No records found!\nPlease enter the subject and faculty details in the DATA ENTRY section.')
    else:
        sp=ttk.Combobox(f,width=20,state='readonly',textvariable=n6,font=("Inter", 15 * -1))
        sp['values']=subdata
        sp.place(x=350.0,y=170.9,width=180.0,height=40)


fact= Label(f,text="Faculty",foreground="#1C1C28",bg='white',font=("Inter", 10 )).place(x=670, y=145)
n7=StringVar()
def selectf1():
    semester=n2.get()
    course=n1.get()
    sql="Select faculty from sub_fac where sem={} and course ='{}'".format(semester,course)
    cursor.execute(sql)
    con.commit()
    facdata=[]
    res=cursor.fetchall()
    for i in res:
        facdata.append(i[0])
    if facdata==[]:
        messagebox.showwarning('Error','No records found!\nPlease enter the subject and faculty details in the DATA ENTRY section.')
    else:
        sp1=ttk.Combobox(f,width=20,state='readonly',textvariable=n7,font=("Inter", 15 * -1))
        sp1['values']=facdata
        sp1.place(x=670.0,y=170.9,width=180.0,height=40)


link_l= Label(f,text="Link",foreground="#1C1C28",bg='white',font=("Inter", 10 )).place(x=1000, y=145)
n8=StringVar()
spn8=ttk.Combobox(f,width=20,textvariable=n8,font=("Inter", 15 * -1))
spn8['values']=None
spn8.place(x=1000.0,y=170.9,width=180.0,height=40)

tick_image_1 = PhotoImage(file=relative_to_assets("tick.png"))
tick1 = Button(image=tick_image_1,borderwidth=0,highlightthickness=0,command=lambda: [selectf(), selectf1()],relief="flat")
tick1.place(x=940.0,y=260.0)

add_image = PhotoImage(file=relative_to_assets("add_button.png"))
add_tt = Button(image=add_image,borderwidth=0,highlightthickness=0,command=add,relief="flat")
add_tt.place(x=1650.0,y=280.0)

clear_image = PhotoImage(file=relative_to_assets("clear_button.png"))
clear_tt = Button(image=clear_image,borderwidth=0,highlightthickness=0,command=clear,relief="flat")
clear_tt.place(x=1650.0,y=330.0)

#==============================================================================================================================================================#
#==========================================================Buttons==============================================================================================#

search_image = PhotoImage(file=relative_to_assets("entry_5.png"))
search_bg = canvas.create_image(1550.0,75,image=search_image)
search = Entry(bd=0,bg="#FFFFFF",highlightthickness=0)
search.place(x=1410.0,y=60,width=284.0,height=33) 

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: print("button_1 clicked"),relief="flat")
button_1.place(x=1750.0,y=50.0,width=50.0,height=50.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=logout,relief="flat")
button_2.place(x=1830.0,y=50.0,width=50.0,height=50.0)

rpass_image = PhotoImage(file=relative_to_assets("button_3.png"))
rpass_btn = Button(image=rpass_image,borderwidth=0,highlightthickness=0,command=lambda: print("button_3 clicked"),relief="flat")
rpass_btn.place(x=20.0,y=389.0,width=280.0,height=40.0)

comp_image = PhotoImage(file=relative_to_assets("button_5.png"))
comp_btn = Button(image=comp_image,borderwidth=0,highlightthickness=0,command=comp,relief="flat")
comp_btn.place(x=20.0,y=243.0,width=280.0,height=40.0)

entry_image = PhotoImage(file=relative_to_assets("button_6.png"))
entry = Button(image=entry_image,borderwidth=0,highlightthickness=0,command=entryf,relief="flat")
entry.place(x=20.0,y=341.0,width=280.0,height=40.0)

tt_image = PhotoImage(file=relative_to_assets("button_10.png"))
tt = Button(image=tt_image,borderwidth=0,  highlightthickness=0,command=None,relief="flat")
tt.place(x=20.0,y=292.0,width=280.0,height=40.0)

dash_image = PhotoImage(file=relative_to_assets("button_7.png"))
dash_btn = Button(image=dash_image,borderwidth=0,highlightthickness=0,command=dash,relief="flat")
dash_btn.place(x=20.0,y=194.0,width=280.0,height=40.0)


window.mainloop()