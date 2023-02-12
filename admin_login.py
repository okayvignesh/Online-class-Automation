from msilib.schema import Icon
from pathlib import Path
from tkinter import Tk, Canvas, Entry, messagebox, Button, PhotoImage
from tkinter.constants import BOTH, YES
from datetime import datetime
import cx_Oracle as oc
con = oc.connect('zoom/admin@localhost:1521/xe')
cursor = con.cursor()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./adminlogin_assets")

#====================================================Functions=================================================================================================#
#==============================================================================================================================================================#

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def showf():
    pasw.config(show="")

def signupf():
    window.destroy()
    import admin_signup

def forgotf():
    window.destroy()
    import adminforgot_password

def Ok():
        u = uname.get()
        p = pasw.get()
        if(u == "" or p == "") :
            messagebox.showerror("ERROR","All fields are required", icon='warning')
        else:
            sql1="SELECT * FROM  admin_login "
            cursor.execute(sql1)
            res=cursor.fetchall()
            for x in res:
                if (u==x[0] and p==x[1]):
                    messagebox.showinfo("SUCCESS", 'Successfully logged in')
                    sql="INSERT INTO admin_log(uname,log_in) VALUES ('{}',sysdate)".format(u)
                    cursor.execute(sql)
                    con.commit()
                    print(u)
                    window.destroy()
                    import admin_dashboard
                    break
            else:
                messagebox.showerror("FAILED", 'Invalid  username/password')
            try:
                    con.commit()
            except oc.DatabaseError as d:
                        print(d)
            finally:
                    #cursor.close()
                    #con.close()
                    None

#==============================================================================================================================================================#
#==========================================================Window==============================================================================================#

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

canvas = Canvas(window,bg = "#FFFFFF",height = 720,width = 1080,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.pack(fill= BOTH,expand=YES)
canvas.create_text(38.0,32.0,anchor="nw",text="Online class \nAutomation.",fill="#1C1C28",font=("Inter", 25 * -1,'bold'))
canvas.create_text(840.0,230.0,anchor="nw",text="WELCOME!",fill="#1C1C28",font=("Inter", 30, 'bold'))
canvas.create_text(780.0,365.0,anchor="nw",text="Admin name ",fill="#1C1C28",font=("Inter", 18 * -1))
canvas.create_text(780.0,480.0,anchor="nw",text="Password",fill="#1C1C28",font=("Inter", 18 * -1))
canvas.create_text(750.0,715.0,anchor="nw",text="Don't have an account?",fill="#1C1C28",font=("Inter", 22 * -1))

#===========================================================Buttons============================================================================================#
#==============================================================================================================================================================#

uname_image = PhotoImage(file=relative_to_assets("uname.png"))
uname_bg = canvas.create_image(955.0,423.5,image=uname_image)
uname = Entry(bd=0,bg="#FFFFFF",highlightthickness=0, font=("Inter",12))
uname.place(x=789.0,y=402.0,width=334.0,height=43.0)

pasw_image = PhotoImage(file=relative_to_assets("pasw.png"))
pasw_bg = canvas.create_image(955.0,530.5,image=pasw_image)
pasw = Entry(bd=0,bg="#FFFFFF",highlightthickness=0, font=("Inter",12))
pasw.place(x=789.0,y=510.0,width=334.0,height=43.0)
pasw.config(show="∙",font=('Inter',10))

signup_image = PhotoImage(file=relative_to_assets("button_1.png"))
signup = Button(image=signup_image,borderwidth=0,highlightthickness=0,command=signupf,relief="flat")
signup.place(x=1010.0,y=710.0,width=150.0,height=36.0)

fpasw_image = PhotoImage(file=relative_to_assets("button_2.png"))
fpasw = Button(image=fpasw_image,borderwidth=0,highlightthickness=0,command=forgotf,relief="flat")
fpasw.place(x=970.0,y=570.0,width=168.0,height=26.0)

login_image = PhotoImage(file=relative_to_assets("button_3.png"))
login = Button(image=login_image,borderwidth=0,highlightthickness=0,command=Ok,relief="flat")
login.place(x=810.0,y=620.0,width=289.0,height=58.33331298828125)

show_image = PhotoImage(file=relative_to_assets("button_4.png"))
show = Button( image=show_image,borderwidth=0,highlightthickness=0,command=showf,relief="flat")
show.place(x=1080.0,y=513.0,width=39.0,height=37.0)

#==============================================================================================================================================================#
#==============================================================================================================================================================#

window.mainloop()