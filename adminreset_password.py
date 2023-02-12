from pathlib import Path
from tkinter import Frame, Tk, Canvas, Entry, messagebox, Button, PhotoImage
from tkinter.constants import BOTH, YES
import cx_Oracle as oc
con = oc.connect('zoom/admin@localhost:1521/xe')
cursor = con.cursor()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./adminreset_assets")

#====================================================Functions=================================================================================================#
#==============================================================================================================================================================#

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def showf():
    old.config(show="")

def confirmf():
    o=old.get()
    n=new.get()
    if o=="" or n=="":
        messagebox.showerror("ERROR","ALl fields are required")
    elif len(o)==len(n)<=8:
        messagebox.showerror("ERROR","Password should be atleast 8 characters")
    elif (o != n):
        messagebox.showerror("ERROR", "Password and confirm password should be the same")
    else:
        try:
            cursor.execute("select * from (select uname from admin_reset order by reset_date desc) where rownum=1")
            s=cursor.fetchone()
            s1=str(s[0])
            sql="UPDATE admin_tb SET pwd='{}' where uname='{}'".format(o,s1)
            cursor.execute(sql)
            con.commit()
        except oc.DatabaseError as d:
            print("Error inserting data",d)
        finally:
            messagebox.showinfo("SUCCESS", 'Password successfully updated')
            window.destroy()
            import admin_login


#==============================================================================================================================================================#
#==========================================================Window==============================================================================================#

window = Tk()
window.title("ONLINE CLASS AUTOMATION")
window.geometry("1020x720+450+200")
window.configure(bg = "#FFFFFF")

#==============================================================================================================================================================#
#==========================================================Canvas==============================================================================================#

canvas = Canvas(window,bg = "#FFFFFF",height = 720,width = 1080,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.pack(fill= BOTH,expand=YES)
canvas.create_text(38.0,32.0,anchor="nw",text="Online class \nAutomation.",fill="#1C1C28",font=("Inter", 15,'bold'))
canvas.create_text(430.0,130.0,anchor="nw",text="Reset password",fill="#1C1C28",font=("Inter", 16, 'bold'))   
canvas.create_text(340.0,225.0,anchor="nw",text="Enter new password",fill="#1C1C28",font=("Inter", 12))
canvas.create_text(340.0,335.0,anchor="nw",text="Confirm new password ",fill="#1C1C28",font=("Inter", 12))

#===========================================================Buttons============================================================================================#
#==============================================================================================================================================================#

old_image = PhotoImage(file=relative_to_assets("old_pass.png"))
old_bg = canvas.create_image(515.0,280.5,image=old_image)
old = Entry(bd=0,bg="#FFFFFF",highlightthickness=0, font=("Inter",12))
old.place(x=349.0,y=260.0,width=334.0,height=43.0)
old.config(show='∙')

new_image = PhotoImage(file=relative_to_assets("new_pass.png"))
new_bg = canvas.create_image(515.0,390.5,image=new_image)
new = Entry(bd=0,bg="#FFFFFF",highlightthickness=0, font=("Inter",12))
new.place(x=349.0,y=370.0,width=334.0,height=43.0)

confirm_image = PhotoImage(file=relative_to_assets("send.png"))
confirm = Button(image=confirm_image,borderwidth=0,highlightthickness=0,command=confirmf,relief="flat")
confirm.place(x=370.0,y=450.0)

show_image1 = PhotoImage(file=relative_to_assets("button_4.png"))
show1 = Button( image=show_image1,borderwidth=0,highlightthickness=0,command=showf,relief="flat")
show1.place(x=645.0,y=263.0,width=39.0,height=37.0)


#==============================================================================================================================================================#
#==============================================================================================================================================================#


window.resizable(False, False)
window.mainloop()