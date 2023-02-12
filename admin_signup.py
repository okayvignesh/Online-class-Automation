from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
import tkinter as tk
import cx_Oracle as oc
con = oc.connect('zoom/admin@localhost:1521/xe')
cursor = con.cursor()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./adminsignup_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def valid():
            fn=fname.get()
            ln=lname.get()
            cc=clgcd.get()
            e=email.get()
            u=uname.get()
            p=pwd.get()
            cp=conpwd.get()
            val= True
            if fn=="" or ln=="" or cc=="" or e=="" or u=="" or p=="" or cp=="":
                messagebox.showerror("ERROR","All fields are required")
            elif (cc.isnumeric()==False):
                messagebox.showerror("ERROR","College code should be a number")
            elif len(p)<8:
                messagebox.showerror("ERROR","Password should be atleast 8 characters")
            elif (p != cp):
                messagebox.showerror("ERROR", "Password and confirm password should be the same")
            elif len(p)<8:
                val = False
                return val
            elif val==False:
                messagebox.showerror("ERROR", "Password should be atleast 8 characters")
            else:
                sql= "INSERT INTO admin_tb VALUES ('{}','{}',{},'{}','{}','{}')".format(fn,ln,cc,e,u,p)
                sql1="INSERT INTO admin_login VALUES ('{}','{}')".format(u,p)
                try:
                        cursor.execute(sql)
                        cursor.execute(sql1)
                        con.commit()
                        messagebox.showinfo("SUCCESS", "Registered successfully")
                        window.destroy()
                        import admin_login
                except oc.DatabaseError as d:
                        print("Error inserting data",d)



def loginf():
    window.destroy()
    import admin_login


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
canvas.create_rectangle(63.0,80.0,1852.0,1002.0,fill="#FFFFFF",outline="")

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=valid,relief="flat")
button_1.place(x=860.0,y=780.0,width=190.0,height=75.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=loginf,relief="flat")
button_2.place(x=1609.0,y=169.0,width=160.0,height=45.0 )

conpwd_image = PhotoImage(file=relative_to_assets("entry_1.png"))
conpwd_bg = canvas.create_image(1276.0,670.0,image=conpwd_image)
conpwd = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
conpwd.place(x=1059.0,y=645.0,width=434.0,height=48.0)

canvas.create_text(1060.0,616.0,anchor="nw",text="Verify Password",fill="#606069",font=("Inter", 20 * -1))

pwd_image = PhotoImage(file=relative_to_assets("entry_2.png"))
pwd_bg = canvas.create_image(1276.0,555.0,image=pwd_image)
pwd = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
pwd.place(x=1059.0,y=530.0,width=434.0,height=48.0)
pwd.config(show='∙')

canvas.create_text(1061.0,500.0,anchor="nw",text="Password",fill="#606069",font=("Inter", 20 * -1))

email_image = PhotoImage(file=relative_to_assets("entry_3.png"))
email_bg = canvas.create_image(660.0,670.0,image=email_image)
email = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
email.place(x=443.0,y=645.0,width=434.0,height=48.0)


canvas.create_text(1062.0,381.0,anchor="nw",text="Username",fill="#606069",font=("Inter", 20 * -1))

canvas.create_text(447.0,615.0,anchor="nw",text="Email",fill="#606069",font=("Inter", 20 * -1))

uname_image = PhotoImage(file=relative_to_assets("entry_4.png"))
uname_bg = canvas.create_image(1276.0,436.0,image=uname_image)
uname = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
uname.place(x=1059.0,y=411.0,width=434.0,height=48.0)


clgcd_image = PhotoImage(file=relative_to_assets("entry_5.png"))
clgcd_bg = canvas.create_image(660.0,555.0,image=clgcd_image)
clgcd = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
clgcd.place(x=443.0,y=530.0,width=434.0,height=48.0)


canvas.create_text(442.0,499.0,anchor="nw",text="College code",fill="#606069",font=("Inter", 20 * -1))

lname_image = PhotoImage(file=relative_to_assets("entry_6.png"))
lname_bg = canvas.create_image(793.0,436.0,image=lname_image)
lname = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
lname.place(x=701.0,y=411.0,width=184.0,height=48.0)


canvas.create_text(703.0,382.0,anchor="nw",text="Last name",fill="#606069",font=("Inter", 20 * -1))

fname_image = PhotoImage(file=relative_to_assets("entry_7.png"))
fname_bg = canvas.create_image(535.0,436.0,image=fname_image)
fname = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,font=('Inter',10))
fname.place(x=443.0,y=411.0,width=184.0,height=48.0)

canvas.create_text(442.0,382.0,anchor="nw",text="First name",fill="#606069",font=("Inter", 20 * -1))
canvas.create_text(748.0,220.0,anchor="nw",text="Please enter your details to continue.",fill="#1C1C28",font=("Inter Bold", 24 * -1))
canvas.create_text(1575.0,139.0,anchor="nw",text="Already have an account?",fill="#1C1C28",font=("Inter Bold", 18 * -1))
canvas.create_text(889.0,163.0,anchor="nw",text="Signup",fill="#1C1C28",font=("Inter Bold", 36 * -1))
canvas.create_text(104.0,137.0,anchor="nw",text="Online class \nAutomation.",fill="#1C1C28",font=("Inter Bold", 25 * -1))

window.mainloop()