from pathlib import Path
from tkinter import Frame, Tk, Canvas, Entry, messagebox, Button, PhotoImage
from tkinter.constants import BOTH, YES
import random,sys, os, math
import smtplib
import cx_Oracle as oc
con = oc.connect('zoom/admin@localhost:1521/xe')
cursor = con.cursor()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./adminforgot_assets")

#====================================================Functions=================================================================================================#
#==============================================================================================================================================================#

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def sendf():
    mailid=mail.get()
    if mailid=="":
        messagebox.showerror("ERROR",'All fields are required')
    else:
        cursor.execute("select uname from admin_tb where email='{}'".format(mailid))
        data=[]
        res=cursor.fetchone()
        if res==None:
            messagebox.showerror("ERROR",'Email not found')
        else:
            for i in res:
                data.append(i)
            print(data[0])
            global u
            u=data[0]
            digits="0123456789"
            global otp
            otp=""
            for i in range(3):
                otp+=digits[math.floor(random.random()*10)]
            msg='Your new password is '+otp+''
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("onlineautomation9@gmail.com","udhsjabjsntvjjwh")
            print(msg)
            s.sendmail('&&&&&&&&&&&',mailid,msg)
            messagebox.showinfo("SUCCESS",'Password has been sent to your mail!')
            otp_e.config(state='normal')

def verify():
    o=otp_e.get()
    if o==otp:
        messagebox.showinfo("SUCCESS", 'OTP verified')
        sql="INSERT into admin_reset(uname, reset_date) VALUES ('{}', sysdate)".format(u)
        try:
            cursor.execute(sql)
            con.commit()
        except oc.DatabaseError as d:
            print("Error inserting data",d)
        finally:
            #cursor.close()
            con.close()
            window.destroy()
            import adminreset_password
    else:
        messagebox.showerror("ERROR", 'the otp entered is wrong')
        

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
canvas.create_text(400.0,200.0,anchor="nw",text="Forgot password?",fill="#1C1C28",font=("Inter", 20, 'bold'))   
canvas.create_text(340.0,300.0,anchor="nw",text="Enter your mail ID ",fill="#1C1C28",font=("Inter", 18 * -1))
canvas.create_text(340.0,390.0,anchor="nw",text="*OTP will be sent to your mail ID",fill="#1C1C28",font=("Inter", 11))
canvas.create_text(385.0,530.0,anchor="nw",text="*Enter your OTP",fill="#1C1C28",font=("Inter", 8))

#===========================================================Buttons============================================================================================#
#==============================================================================================================================================================#

mail_image = PhotoImage(file=relative_to_assets("uname.png"))
mail_bg = canvas.create_image(515.0,353.5,image=mail_image)
mail = Entry(bd=0,bg="#FFFFFF",highlightthickness=0, font=("Inter",12))
mail.place(x=349.0,y=332.0,width=334.0,height=43.0)

send_image = PhotoImage(file=relative_to_assets("send.png"))
send = Button(image=send_image,borderwidth=0,highlightthickness=0,command=sendf,relief="flat")
send.place(x=370.0,y=450.0)

otp_image = PhotoImage(file=relative_to_assets("otp.png"))
otp_bg = canvas.create_image(485.0,573.5,image=otp_image)
otp_e = Entry(bd=0,bg="#FFFFFF",highlightthickness=0, font=("Inter",12),state='readonly')
otp_e.place(x=390.0,y=552.0,width=190.0,height=43.0)

tick_image_1 = PhotoImage(file=relative_to_assets("tick.png"))
tick1 = Button(image=tick_image_1,borderwidth=0,highlightthickness=0,command=verify,relief="flat")
tick1.place(x=610.0,y=553.0)

#==============================================================================================================================================================#
#==============================================================================================================================================================#


window.resizable(False, False)
window.mainloop()