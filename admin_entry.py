from pathlib import Path
from tkinter import Tk, Canvas, Entry,  Button, PhotoImage, messagebox
from tkinter.constants import BOTH, LEFT, YES
from tkinter import *
from tkinter import ttk
from datetime import datetime
import cx_Oracle as oc
con = oc.connect('zoom/admin@localhost:1521/xe')
cursor= con.cursor()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./adminentry_assets")

#====================================================Functions=================================================================================================#
#==============================================================================================================================================================#

def relative_to_assets(path: str) -> Path:  
    return ASSETS_PATH / Path(path)

def ttf():
    window.destroy()
    import admin_tt

def comp():
    window.destroy()
    import admin_complaint    

def add():
    cou=course_e.get()
    sem=sem_e.get()
    sub=sub_e.get()
    fac=fac_e.get()
    sec=sec_e.get()
    if (cou== "" or sem=="" or sub=="" or fac=="" or sec==""):
        messagebox.showerror("Error","Fields can't be empty")
    else:
        sql= "INSERT INTO sub_fac VALUES ('{}',{},'{}','{}','{}')".format(cou, sem, sub, fac, sec)
        try:
            cursor.execute(sql)
            con.commit()
            messagebox.showinfo("SUCCESS","Sucessfully updated")
        except oc.DatabaseError as d:
            print("Error inserting data",d)
        finally:
            #cursor.close() 
            #con.close()
            None

def clear():
    course_e.delete(0, END)
    sem_e.delete(0, END)
    sub_e.delete(0, END)
    fac_e.delete(0, END)
    sec_e.delete(0, END)

def logout():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
        cursor.execute("UPDATE admin_log SET log_out=sysdate where uname= '{}'".format(s1))
        con.commit()
        window.destroy()
        import admin_login
    else:
        messagebox.showinfo('Return','You will now return to the application screen')
    
def dash():
    window.destroy()
    import admin_dashboard


def deletef():
    c=course_e.get()
    sub=sub_e.get()
    sem=sem_e.get()
    fac=fac_e.get()
    sec=sec_e.get()
    cursor.execute("delete from sub_fac where course='{}' and sem={} and section='{}' and  subject='{}'".format(c,sem,sec,sub))
    con.commit()
    messagebox.showinfo("SUCCESS","Sucessfully updated")

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
canvas.create_text(950.0,180.0,anchor="nw",text=" Subject & faculty information",fill="#1C1C28",font=("Inter", 15))
canvas.create_text(403.0,48.0,anchor="nw",text="Entry",fill="#FFFFFF",font=("Inter Bold", 30 * -1))     
canvas.create_text(59.0,35.0,anchor="nw",text="Online Class\nAutomation.",fill="#FFFFFF",font=("Inter Bold", 30 * -1))

#search bar
search_image = PhotoImage(file=relative_to_assets("entry_5.png"))
search_bg = canvas.create_image(1550.0,75,image=search_image)
search = Entry(bd=0,bg="#FFFFFF",highlightthickness=0)
search.place(x=1410.0,y=60,width=284.0,height=33.0)

#==============================================================================================================================================================#
#==============================================================Buttons=========================================================================================#

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
dashboard = Button(image=dashboard_image,borderwidth=0,highlightthickness=0,command=dash,relief="flat")
dashboard.place(x=19.0,y=194.0,width=280.0,height=40.0)

complaints_image1 = PhotoImage(file=relative_to_assets("button_5.png"))
complaints1 = Button(image=complaints_image1,borderwidth=0,highlightthickness=0,command=comp,relief="flat")
complaints1.place(x=19.0,y=243.0,width=280.0,height=40.0)

tt_image = PhotoImage(file=relative_to_assets("button_10.png"))
tt = Button(image=tt_image,borderwidth=0,highlightthickness=0,command=ttf,relief="flat")            
tt.place(x=19.0,y=292.0,width=280.0,height=40.0)

entry_image = PhotoImage(file=relative_to_assets("button_6.png"))
entry = Button(image=entry_image,borderwidth=0,highlightthickness=0,command=None,relief="flat")
entry.place(x=19.0,y=341.0,width=280.0,height=40.0)

#==============================================================================================================================================================#
#==========================================================Table view==========================================================================================#
data_frame = LabelFrame(window, background='white',font=("Inter", 10))
data_frame.place(x=500,y=250)

course_l = Label(data_frame, text="Course :", bg='white',font=("Inter", 10))
course_l.grid(row=0, column=0, padx=10, pady=10)
course_e = Entry(data_frame,font=('Inter', 10), width=30)
course_e.grid(row=0, column=1, padx=10, pady=10)

sec_l = Label(data_frame, text="Section :", bg='white',font=("Inter", 10))
sec_l.grid(row=0, column=2, padx=10, pady=10)
sec_e = Entry(data_frame,font=('Inter', 10), width=30)
sec_e.grid(row=0, column=3, padx=10, pady=10)

sub_l = Label(data_frame, text="Subject :", bg='white',font=("Inter", 10))
sub_l.grid(row=1, column=0, padx=10, pady=10)
sub_e = Entry(data_frame,font=('Inter', 10), width=30)
sub_e.grid(row=1, column=1, padx=10, pady=10)

sem_l = Label(data_frame, text="Semester :", bg='white',font=("Inter", 10))
sem_l.grid(row=1, column=2, padx=10, pady=10)
sem_e = Entry(data_frame,font=('Inter', 10), width=30)
sem_e.grid(row=1, column=3, padx=10, pady=10)

fac_l = Label(data_frame, text="Faculty :", bg='white',font=("Inter", 10))
fac_l.grid(row=2, column=1, padx=10, pady=10)
fac_e = Entry(data_frame,font=('Inter', 10), width=30)
fac_e.grid(row=2, column=2, padx=10, pady=10)

delete_im = PhotoImage(file=relative_to_assets("delete.png"))
delete_btn = Button(image=delete_im,borderwidth=0,highlightthickness=0,command=deletef,relief="flat")
delete_btn.place(x=1700.0,y=280)

add_image = PhotoImage(file=relative_to_assets("add_button.png"))
add_tt = Button(image=add_image,borderwidth=0,highlightthickness=0,command=add,relief="flat")
add_tt.place(x=1700.0,y=280)

clear_image = PhotoImage(file=relative_to_assets("clear_button.png"))
clear_tt = Button(image=clear_image,borderwidth=0,highlightthickness=0,command=clear,relief="flat") 
clear_tt.place(x=1700.0,y=330)

#==============================================================================================================================================================#
#=============================================================================================================================================================#

d=Label(window, text="View info", font=("Inter", 15), bg='white').place(x=950, y=500)
f=Frame(canvas,width=1500, height=900, background='white')
f.place(x=500, y=500)

sem=Label(f,text="Semester",foreground="#1C1C28",bg='white',  font=("Inter", 10 )).place(x=1000,y=55)
n2=IntVar()
spn2=ttk.Combobox(f,width=20,state='readonly',textvariable=n2,font=("Inter", 15 * -1))
spn2['values']=(1,2,3,4,5,6,7,8)
spn2.place(x=1000.0,y=80.9,width=180.0,height=40)


cour=Label(f,text="Course",foreground="#1C1C28",bg='white',font=("Inter", 10 )).place(x=1000, y=125)
n1=StringVar()
sem_g=n2.get()
cursor.execute("Select distinct(course) from sub_fac")
con.commit()
courdata=[]
res=cursor.fetchall()
for i in res:
    courdata.append(i[0])
spn1=ttk.Combobox(f,width=20,state='readonly',textvariable=n1,font=("Inter", 15 * -1))
spn1['values']=courdata
spn1.place(x=1000.0,y=150.9,width=180.0,height=40)


sec= Label(f,text="Section",foreground="#1C1C28",bg='white',font=("Inter", 10 )).place(x=1000, y=195)
n3=StringVar()
spn3=ttk.Combobox(f,width=20,state='readonly',textvariable=n3,font=("Inter", 15 * -1))
spn3['values']=('A',
              'B',
              'C',
              'D')
spn3.place(x=1000.0,y=220.9,width=180.0,height=40)

def viewf():
    semester=n2.get()
    section=n3.get()
    course=n1.get()
    f1=Frame(window, height=600)
    f1.place(x=600, y=550)
    Label1 = Label(f1, text="Subject", width=50,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
    Label1.grid(row=0, column=0)
    Label2 = Label(f1, text="Faculty", width=50,height=3,font=('Inter',8),background='#7373A8',foreground='white',relief="sunken")
    Label2.grid(row=0, column=1)
    sql= "select subject, faculty from sub_fac where sem={} and course ='{}' and section='{}' order by subject asc".format(semester,course, section)
    cursor.execute(sql)
    con.commit()
    data = cursor.fetchall()
    if data == []:
        messagebox.showerror('ERROR','No records found')
    else:
#for index,dat in data:
        for i, ind in enumerate(data):  
            Label(f1, text=ind[0],width=50,height=2,font=('Inter',8),background='white', relief="sunken").grid(row=i+1, column=0)
            Label(f1, text=ind[1], width=50,height=2,font=('Inter',8),background='white',relief="sunken").grid(row=i+1, column=1)


view_image = PhotoImage(file=relative_to_assets("view.png"))
view = Button(f,image=view_image,borderwidth=0,highlightthickness=0,command=viewf,relief="flat")
view.place(x=1030.0,y=280)

update_im = PhotoImage(file=relative_to_assets("update.png"))
update = Button(f,image=update_im,borderwidth=0,highlightthickness=0,command=add_tt.destroy,relief="flat")
update.place(x=1030.0,y=330)


window.mainloop()