from pathlib import Path
import random
from tkinter import ttk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import tkinter as tk
from tkinter import *
from datetime import datetime
from tkinter.constants import BOTH, END, YES
import cx_Oracle as oc
from matplotlib.pyplot import text
con = oc.connect('zoom/admin@localhost:1521/xe')
cursor= con.cursor()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./usercomplaint_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path) 

def dashboardf():
    window.destroy()
    import user_dashboard



def logout():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
        cursor.execute("UPDATE log SET log_out=sysdate where uname= '{}'".format(s1))
        con.commit()
        window.destroy()
        import user_login
    else:
        messagebox.showinfo('Return','You will now return to the application screen')



def sendf():
    comp=c_text.get("1.0",'end-1c')
    if (comp==""):
        messagebox.showerror("Error","Complaint can't be empty")
    else:
        rand=random.randrange(1,1000)
        stat="PENDING"
        sql="INSERT INTO cmp_tb(cmp_no,cmp,cmp_raised,uname,cmpst) VALUES ({},'{}', sysdate,'{}','{}')".format(rand,comp, s1,stat)
        try:
            cursor.execute(sql)
            con.commit()
            messagebox.showinfo("SUCCESS","Complaint raised")
        except oc.DatabaseError as d:
            messagebox.showerror("Error inserting data",d)
            print(d)
        finally:
            c_text.delete('0.0',END)
            

    
window = tk.Tk()
window.title("ONLINE CLASS AUTOMATION")
window.geometry("1536x864+0+0")
fullScreenState = False
window.attributes("-fullscreen", fullScreenState)
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d" % (w, h))
window.configure(bg = "#FFFFFF")

def clear():
    c_text.delete('0.0',END)

canvas = Canvas(window,bg = "#FFFFFF",height = 864,width = 1536,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.pack(fill= BOTH,expand=YES)
canvas.create_rectangle(0.0,1.0,1936.0,140.0,fill="#1C1C28",outline="")
canvas.create_text(403.0,48.0,anchor="nw",text="Complaints",fill="#FFFFFF",font=("helvetica Bold", 20 * -1,'bold'))
cursor.execute("select * from (select uname from log order by log_in desc) where rownum=1")
s=cursor.fetchone()
s1=str(s[0])    
print(s1)
n=StringVar()
n.set(s)
uname_l=Label(window, textvariable=n,fg="#1C1C28",bg='white', font=("Inter", 14,'bold')).place(x=74,y=930)
canvas.create_text(90.0,960.0,anchor="nw",text="Online",fill="#1C1C28",font=("Inter Light", 18 * -1))
canvas.create_text(31.0,158.0,anchor="nw",text="Main",fill="#1C1C28",font=("Inter Medium", 20 * -1))
canvas.create_text(59.0,35.0,anchor="nw",text="Online Class\nAutomation.",fill="#FFFFFF",font=("helvetica Bold", 20 * -1,'bold'))
canvas.create_text(620.0,231.0,anchor="nw",text="Write your Complaint ",fill="#1C1C28",font=("helvetica Bold", 15 * -1,'bold') )
canvas.create_text(1000.0,162.0,anchor="nw",text="Raise a Complaint",fill="#1C1C28",font=("helvetica Bold", 15,'bold'))

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

c_image = PhotoImage(file=relative_to_assets("Rectangle_21.png"))
c_bg = canvas.create_image(1100,337,image=c_image)
c_text = Text(window, wrap=tk.WORD,width=60, height=6,font=("Inter", 12))
c_text.place(x=650,y=267)

s_image = PhotoImage(file=relative_to_assets("send.png"))
s_btn = Button(image=s_image,borderwidth=0,highlightthickness=0,command=sendf,relief="groove")
s_btn.place( x=1450.0,y=290.0)

cl_image = PhotoImage(file=relative_to_assets("clear.png"))
cl_btn = Button(image=cl_image,borderwidth=0,highlightthickness=0,command=clear,relief="groove")
cl_btn.place( x=1450.0,y=340.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=lambda: print("button_3 clicked"),relief="flat")
button_3.place(x=20.0,y=297.0,width=280.0,height=40.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=lambda: print("button_4 clicked"),relief="flat")
button_4.place(x=20.0,y=346.0,width=280.0,height=40.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_6.png"))
button_5 = Button(image=button_image_5,borderwidth=0,highlightthickness=0,command= dashboardf,relief="flat")
button_5.place(x=20.0,y=199.0,width=280.0,height=40.0)

button_image_6 = PhotoImage(file=relative_to_assets("button_5.png"))
button_6 = Button(image=button_image_6,borderwidth=0,highlightthickness=0,command=lambda: print("button_6 clicked"),relief="flat")
button_6.place(x=20.0,y=248.0,height=40.0)

canvas.create_text(1000.00,550.0,anchor="nw",text="Your Complaints",fill="#1C1C28",font=("Inter",15))
c1 = Canvas(window,bg = "#FFFFFF",height = 700,width =600 ,bd = 0,highlightthickness = 0,relief = "ridge")
c1.place(x=400, y=600)



Label1 = Label(c1, text="Complaint ", width=54,height=2,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label1.grid(row=0, column=0)
Label2 = Label(c1, text="Complaint raised", width=25,height=2,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label2.grid(row=0, column=1)
Label3 = Label(c1, text="Complaint status ", width=25,height=2,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label3.grid(row=0, column=2) 
Label4 = Label(c1, text="Remarks", width=32,height=2,font=('Inter',10),background='#1C1C28',foreground='white',relief="sunken")
Label4.grid(row=0, column=3)

def ref():
    cursor.execute("select cmp, cmp_raised, cmpst, remarks from cmp_tb where uname='{}' order by cmp_raised asc".format(s1))
    con.commit()
    data=cursor.fetchall()
    print(data)
    if data==[]:
        messagebox.showerror("ERROR",'No records found')
    else:
        for i, ind in enumerate(data):
                Label(c1, text=ind[0],width=60,font=('Arial',10),background='white', relief="sunken").grid(row=i+1, column=0)
                Label(c1, text=ind[1], width=28,font=('Arial',10),background='white',relief="sunken").grid(row=i+1, column=1)
                Label(c1, text=ind[2], width=28,font=('Arial',10),background='white',relief="sunken").grid(row=i+1, column=2)
                Label(c1, text=ind[3], width=35,font=('Arial',10),background='white',relief="sunken").grid(row=i+1, column=3)

    y=0
    vscrollbar = Scrollbar(c1, orient=VERTICAL, command=canvas.yview)
    vscrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
    c1.config(yscrollcommand=vscrollbar.set, scrollregion=(0, 0, 0, y))

    


ref_image = PhotoImage(file=relative_to_assets("refresh.png"))
refresh = Button(image=ref_image,borderwidth=0,highlightthickness=0,command=ref,relief="flat")
refresh.place(x=1650.0,y=550.0)

window.mainloop()
