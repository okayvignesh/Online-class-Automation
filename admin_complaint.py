
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import tkinter as tk
from tkinter.constants import ANCHOR, BOTH, YES 
from datetime import datetime
from tkinter import *
import cx_Oracle as oc
con = oc.connect('zoom/admin@localhost:1521/xe')
cursor= con.cursor()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./admincomplaint_assets")

#====================================================Functions=================================================================================================#
#==============================================================================================================================================================#

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def dash():
    window.destroy()
    import admin_dashboard
    
def ttf():
    window.destroy()
    import admin_tt   

def logout():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
        cursor.execute("UPDATE admin_log SET log_out=sysdate where uname= '{}'".format(s1))
        con.commit()
        window.destroy()
        import admin_login
    else:
        messagebox.showinfo('Return','You will now return to the application screen')

def entryf():
    window.destroy()
    import admin_entry

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
canvas.create_rectangle(0.0,1.0,1936.0,140.0,fill="#1C1C28",outline="")
canvas.create_text(403.0,48.0,anchor="nw",text="Complaints",fill="#FFFFFF",font=("Inter Bold", 30 * -1))
cursor.execute("select * from (select uname from admin_log order by log_in desc) where rownum=1")
s=cursor.fetchone()
s1=str(s[0])
print(s1)
n=StringVar()
n.set(s)
uname_l=Label(window, textvariable=n,fg="#1C1C28",bg='white', font=("Inter", 14,'bold')).place(x=74,y=910)
canvas.create_text(95.0,950.0,anchor="nw",text="Online",fill="#1C1C28",font=("Inter Light", 18 * -1))
canvas.create_text(31.0,158.0,anchor="nw",text="Main",fill="#1C1C28",font=("Inter Medium", 20 * -1))
canvas.create_text(59.0,35.0,anchor="nw",text="Online Class\nAutomation.",fill="#FFFFFF",font=("Inter Bold", 30 * -1))
canvas.create_text(1000.0,162.0,anchor="nw",text="User Complaints",fill="#1C1C28",font=("Helvetica", 24 * -1,'bold'))

search_image = PhotoImage(file=relative_to_assets("entry_5.png"))
search_bg = canvas.create_image(1550.0,75,image=search_image)
search = Entry(bd=0,bg="#FFFFFF",highlightthickness=0)
search.place(x=1410.0,y=60,width=284.0,height=33.0)

#==============================================================================================================================================================#
#==============================================================Buttons=========================================================================================#


button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: print("button_1 clicked"),relief="flat")
button_1.place(x=1750.0,y=50.0,width=50.0,height=50.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=logout,relief="flat")
button_2.place(x=1830.0,y=50.0,width=50.0,height=50.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=lambda: print("button_3 clicked"),relief="flat")
button_3.place(x=19.0,y=389.0,width=280.0,height=40.0)

dashboard_image = PhotoImage(file=relative_to_assets("button_7.png"))
dashboard = Button(image=dashboard_image,borderwidth=0,highlightthickness=0,command=dash,relief="flat")
dashboard.place(x=19.0,y=194.0,width=280.0,height=40.0)

complaints_image1 = PhotoImage(file=relative_to_assets("button_5.png"))
complaints1 = Button(image=complaints_image1,borderwidth=0,highlightthickness=0,command=None,relief="flat")
complaints1.place(x=19.0,y=243.0,width=280.0,height=40.0)

tt_image = PhotoImage(file=relative_to_assets("button_11.png"))
tt = Button(image=tt_image,borderwidth=0,highlightthickness=0,command=ttf,relief="flat")            
tt.place(x=19.0,y=292.0,width=280.0,height=40.0)

entry_image = PhotoImage(file=relative_to_assets("button_6.png"))
entry = Button(image=entry_image,borderwidth=0,highlightthickness=0,command=entryf,relief="flat")
entry.place(x=20.0,y=341.0,width=280.0,height=40.0)


#==============================================================================================================================================================#
#==========================================================Complaints==========================================================================================#
c1 = Canvas(window,bg = "#FFFFFF",height = 700,width =600 ,bd = 0,highlightthickness = 0,relief = "ridge")
c1.place(x=400, y=250)


Label1 = Label(c1, text="C.no", width=10,height=2,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label1.grid(row=0, column=0)
Label2 = Label(c1, text="Username", width=20,height=2,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label2.grid(row=0, column=1)
Label3 = Label(c1, text="Complaint", width=55,height=2,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label3.grid(row=0, column=2) 
Label4 = Label(c1, text="Complaint Raised at", width=30,height=2,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label4.grid(row=0, column=3)
Label5 = Label(c1, text="Status ", width=25,height=2,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label5.grid(row=0, column=4)

def resolvedf():
    cursor.execute("select cmp_no,uname, cmp, cmp_raised, cmpst from cmp_tb where cmpst='PENDING' order by cmp_raised asc")
    con.commit()
    data1=[]
    res=cursor.fetchone()
    if res==None:
        messagebox.showerror("ERROR",'No records found')
    else:
        for i in res:
            data1.append(i)
        u=data1[0]
        cno=str(u)
        print(cno)
        stat='RESOLVED'
        rem=c_text1.get('1.0', 'end-1c')
        if rem=="":
            messagebox.showerror("Error","Remarks can't be empty")
        else:
            sql1="UPDATE cmp_tb SET remarks='{}',cmp_resolved=sysdate, cmpst='{}' where cmp_no='{}' ".format(rem, stat, cno)
            try:
                cursor.execute(sql1)
                con.commit()
            except oc.DatabaseError as d:
                messagebox.showerror("Error inserting data",d)
                print(d)
            finally:
                c_text1.delete('0.0',END)
                messagebox.showinfo("SUCCESS","Complaint resolved")
def ref():      
    cursor.execute("select cmp_no, uname, cmp, cmp_raised, cmpst from cmp_tb where cmpst='PENDING' order by cmp_raised asc")
    con.commit()
    data1=[]
    res=cursor.fetchone()
    if res==None:
        messagebox.showerror("ERROR",'No records found')
    else:
        for i in res:
            data1.append(i)
        Label(c1, text=data1[0],width=11,font=('Arial',10),background='white', relief="sunken",anchor=W).grid(row=1, column=0)
        Label(c1, text=data1[1], width=22,font=('Arial',10),background='white',relief="sunken",anchor=W).grid(row=1, column=1)
        Label(c1, text=data1[2], width=61,font=('Arial',10),background='white',relief="sunken",anchor=W).grid(row=1, column=2)
        Label(c1, text=data1[3], width=33,font=('Arial',10),background='white',relief="sunken",anchor=W).grid(row=1, column=3)
        Label(c1, text=data1[4], width=28,font=('Arial',10),background='white',relief="sunken",anchor=W).grid(row=1, column=4)


c_image = PhotoImage(file=relative_to_assets("Rectangle_21.png"))
c_bg = canvas.create_image(1050,420,image=c_image)
c_text1 = Text(window, wrap=tk.WORD,width=55, height=2,font=("Inter", 10))
c_text1.place(x=680,y=400)

button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
button_8 = Button(image=button_image_8,borderwidth=0,highlightthickness=0,command=resolvedf,relief="flat")
button_8.place(x=1300.0,y=405.0)


ref_image = PhotoImage(file=relative_to_assets("refresh.png"))
refresh = Button(image=ref_image,borderwidth=0,highlightthickness=0,command=ref,relief="flat")
refresh.place(x=1650.0,y=200.0)

canvas.create_text(1000.00,550.0,anchor="nw",text="Complaints Resolved",fill="#1C1C28",font=("Inter",15))
c2 = Canvas(window,bg = "#FFFFFF",height = 700,width =600 ,bd = 0,highlightthickness = 0,relief = "ridge")
c2.place(x=600, y=600)

Label6 = Label(c2, text="C.no ", width=10,height=2,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label6.grid(row=0, column=0)
Label7 = Label(c2, text="Complaint raised", width=25,height=2,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label7.grid(row=0, column=1)
Label8 = Label(c2, text="Complaint status ", width=25,height=2,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label8.grid(row=0, column=2) 
Label9 = Label(c2, text="Remarks", width=32,height=2,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label9.grid(row=0, column=3)

def ref():
    cursor.execute("select cmp_no, cmp_raised, cmpst, remarks from cmp_tb where cmpst='RESOLVED' order by cmp_raised asc")
    con.commit()
    data=cursor.fetchall()
    if data==None:
        messagebox.showerror("ERROR",'No records found')
    else:
        for i, ind in enumerate(data):
                Label(c2, text=ind[0],width=11,font=('Arial',10),background='white', relief="sunken").grid(row=i+1, column=0)
                Label(c2, text=ind[1], width=28,font=('Arial',10),background='white',relief="sunken").grid(row=i+1, column=1)
                Label(c2, text=ind[2], width=28,font=('Arial',10),background='white',relief="sunken").grid(row=i+1, column=2)
                Label(c2, text=ind[3], width=35,font=('Arial',10),background='white',relief="sunken").grid(row=i+1, column=3)


ref_image1 = PhotoImage(file=relative_to_assets("refresh.png"))
refresh1 = Button(image=ref_image1,borderwidth=0,highlightthickness=0,command=ref,relief="flat")
refresh1.place(x=1600.0,y=605.0)
#==============================================================================================================================================================#
#=============================================================================================================================================================#

window.mainloop()