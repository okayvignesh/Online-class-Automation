from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, ttk
import tkinter as tk
import cx_Oracle as oc
con = oc.connect('zoom/admin@localhost:1521/xe')
cursor = con.cursor()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./usersignup_assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def valid():
            fn=fname.get()
            ln=lname.get()
            cc=clgcd.get()
            cs=course.get()
            rno=regno.get()
            e=email.get()
            u=uname.get()
            p=pwd.get()
            cp=conpwd.get()
            sec=n.get() 
            gd= v.get()
            print(p)
            if gd == 1:
                gd='M'
            else:
                gd='F'
            s=sp1.get()
            val= True
            if fn=="" or ln=="" or cc=="" or cs=="" or rno=="" or e=="" or u=="" or p=="" or cp=="":
                messagebox.showerror("ERROR","All fields are required")
            elif (cc.isnumeric()==False):
                messagebox.showerror("ERROR","College code should be a number")
            elif len(p)<8:
                messagebox.showerror("ERROR","Password should be atleast 8 characters")
            elif (p != cp):
                messagebox.showerror("ERROR", "Password and confirm password should be the same")
            else:
                sql= "INSERT INTO user_tb VALUES ('{}','{}','{}',{},'{}','{}','{}','{}','{}','{}',{})".format(rno,fn,ln,cc,cs,u,p,e,sec,gd,s)
                sql1="INSERT INTO user_login VALUES ('{}','{}')".format(u,p)
                try:
                        cursor.execute(sql)
                        cursor.execute(sql1)
                        con.commit()
                        messagebox.showinfo("SUCCESS", "Registered successfully")
                except oc.IntegrityError as e:
                        messagebox.showerror("ERROR","User already exists")
                finally:
                        window.destroy()
                        import user_login

def loginf():
    window.destroy()
    import user_login 

window = tk.Tk()
window.title("ONLINE CLASS AUTOMATION")
window.geometry("1536x864+0+0")
fullScreenState = False
window.attributes("-fullscreen", fullScreenState)
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d" % (w, h))
window.configure(bg = "#FFFFFF")

canvas = Canvas(window,bg = "#F4F4F4",height = 1080,width = 1920,bd = 0,highlightthickness = 0,relief = "ridge")

canvas.place(x = 0, y = 0)
canvas.create_rectangle(75.0,60.0,1850.0,1000.0,fill="#FFFFFF",outline="")
canvas.create_text(748.0,201.99999999999994,anchor="nw",text="Please enter your details to continue.",fill="#1C1C28",font=("Inter Bold", 24 * -1))
canvas.create_text(1575.0,138.99999999999994,anchor="nw",text="Already have an account?",fill="#606069",font=("Inter Bold", 18 * -1))
canvas.create_text(889.0,148.0,anchor="nw",text="Signup",fill="#1C1C28",font=("Inter Bold", 36 * -1))
canvas.create_text(124.0,106.0,anchor="nw",text="Online class \nAutomation.",fill="#1C1C28",font=("Inter Bold", 18))

canvas.create_text(410.0,638.0,anchor="nw",text="Gender",fill="#606069",font=("Inter", 12))
v=IntVar()
rbmale=Radiobutton(window,value=1,text="  Male",variable=v,font=("Inter", 12 ),background="white", foreground='#606069' )
rbmale.place(x=410,y=675)
rbfe=Radiobutton(window,value=2,text='  Female', variable=v,font=("Inter", 12 ),background="white",foreground='#606069')
rbfe.place(x=540,y=675)

canvas.create_text(410.0,732.0,anchor="nw",text="Course",fill="#606069",font=("Inter", 12))

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=4,highlightthickness=0,command=valid,relief="flat")
button_1.place(x=865.0,y=878.0,width=180.0,height=65.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=4,highlightthickness=0,command=loginf,relief="flat")
button_2.place( x=1609.0, y=168.99999999999994, width=160.0,height=45.0)

conpwd_image = PhotoImage(file=relative_to_assets("entry_1.png"))
conpwd_bg = canvas.create_image(1251.0,788.0,image=conpwd_image)
conpwd = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
conpwd.place(x=1059.0,y=763.0,width=384.0,height=48.0)

canvas.create_text(1060.0,734.0,anchor="nw",text="Verify Password",fill="#606069",font=("Inter", 12))
pwd_image = PhotoImage(file=relative_to_assets("entry_2.png"))
pwd_bg = canvas.create_image(1251.0,687.0,image=pwd_image)
pwd = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
pwd.place(x=1059.0,y=662.0,width=384.0,height=48.0)
pwd.config(show='∙')

canvas.create_text(1061.0,632.0,anchor="nw",text="Password",fill="#606069",font=("Inter", 12))
email_image = PhotoImage(file=relative_to_assets("entry_3.png"))
email_bg = canvas.create_image(1251.0,483.99999999999994,image=email_image)
email = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
email.place(x=1059.0,y=458.99999999999994,width=384.0,height=48.0)

canvas.create_text(1062.0,531.0,anchor="nw",text="Username",fill="#606069",font=("Inter", 12))
regno_image = PhotoImage(file=relative_to_assets("entry_4.png"))
regno_bg = canvas.create_image(1251.0,379.99999999999994,image=regno_image)
regno = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
regno.place(x=1059.0,y=354.99999999999994,width=384.0,height=48.0)

canvas.create_text(1063.0,428.99999999999994,anchor="nw",text="Email",fill="#606069",font=("Inter", 12))
uname_image = PhotoImage(file=relative_to_assets("entry_5.png"))
uname_bg = canvas.create_image(1251.0,586.0,image=uname_image)
uname = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
uname.place(x=1059.0,y=561.0,width=384.0,height=48.0)

canvas.create_text(1061.0,325.99999999999994,anchor="nw",text="Register Number",fill="#606069",font=("Inter", 12))

canvas.create_text(410.0,528.0,anchor="nw",text="Semester",fill="#606069",font=("Inter", 12))
sp1=Spinbox(window,from_=1,to=8,bd=1,state='readonly',font=("Inter", 10))
sp1.place(x=410.0,y=565.9,width=190.0,height=33.0)

clgcd_image = PhotoImage(file=relative_to_assets("entry_6.png"))
clgcd_bg= canvas.create_image(603.0,483.99999999999994,image=clgcd_image)
clgcd = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
clgcd.place(x=411.0,y=458.99999999999994,width=384.0,height=48.0)

course_image = PhotoImage(file=relative_to_assets("entry_7.png"))
course_bg = canvas.create_image(603.0,788.0,image=course_image)
course = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
course.place( x=411.0,y=763.0,width=384.0,height=48.0)

canvas.create_text(410.0,427.99999999999994,anchor="nw",text="College code",fill="#606069",font=("Inter", 12))
lname_image = PhotoImage(file=relative_to_assets("entry_8.png"))
lname_bg = canvas.create_image(761.0,379.99999999999994,image=lname_image)
lname = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
lname.place(x=669.0,y=354.99999999999994,width=184.0,height=48.0)

canvas.create_text(671.0,325.99999999999994,anchor="nw",text="Last name",fill="#606069",font=("Inter", 12))

canvas.create_text(674.0,528.0,anchor="nw",text="Section",fill="#606069",font=("Inter", 12))
    
n=StringVar()
spn=ttk.Combobox(window,width=20,state='readonly',textvariable=n,font=("Inter", 10))
spn['values']=('A',
              'B',
              'C',
              'D')
spn.place(x=671.0,y=565.9,width=190.0,height=38.0)
spn.current(0)

fname_image = PhotoImage(file=relative_to_assets("entry_9.png"))
fname_bg = canvas.create_image(503.0,379.99999999999994,image=fname_image)
fname = Entry( bd=0, bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
fname.place(x=411.0,y=354.99999999999994,width=184.0,height=48.0)

canvas.create_text(410.0,325.99999999999994,anchor="nw",text="First name",fill="#606069",font=("Inter", 12))

window.mainloop()