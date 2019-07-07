# Created on : 06 / 07 / 2016
# Author : Pritam Kulkarni
# interface.py

from Tkinter import *
import MySQLdb
import datetime

import Tkinter as Tk

import tkMessageBox
import tkFont
from PIL import Image
root = Tk.Tk()
#root.minsize(width=666,height=666)
#root.maxsize(width=666,height=666)
width=600
height=400

background_image=Tk.PhotoImage(file="/home/pi/Desktop/project/html/7.gif")
background_label = Tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.wm_geometry("600x400+20+40")
label_head=Label(root,text="Walchand College of Engineering,Sangli.",font=("Lucida Fax",23),fg="cyan",bg="black");
f = tkFont.Font(label_head, label_head.cget("font"))
f.configure(underline = True)
label_head.configure(font=f)
label_head.pack()
label_b1=Label(root,text="",bg="black")
label_b1.pack()
label_1= Label(root,text="Welcome to Smart Energy Conservaton System",font=("Helvetica",20),fg="red",bg="black")
label_1.pack()
label11= Label(root,text="General Information About The Energy Conservation System",font=("Helvetica",15),fg="blue",bg="black")
label11.pack()

label_2= Label(root,text="A Smart Energy Conservation System that will help various organizations to play an",fg="white",bg="black")
label3= Label(root,text="effective role in saving electrical energy.  The major area which consumes maximum amount",fg="white",bg="black")
label4= Label(root,text="of electricity is observed to be the educational institutions. They are used nearly 70% of the",fg="white",bg="black")
label5= Label(root,text="time by students and faculties. A simple action of switching OFF the electric consumables ",fg="white",bg="black")
label6= Label(root,text="when not in use will save lot of energy. In order to conserve energy, automated lighting",fg="white",bg="black")
label7= Label(root,text="system using Raspberry Pi that monitors the electrical lighting is proposed. The experimental",fg="white",bg="black")
label8= Label(root,text="results show that we can reduce our bill to the extent of 50% if the electrical x are",fg="white",bg="black")
label9= Label(root,text="switched OFF promptly when not in use.",fg="white",bg="black")
label10= Label(root,text="Press the below CONTINUE button to proceed",fg="white",bg="black")
label13= Label(root,text="",bg="black")
label14= Label(root,text="",bg="black")
label15= Label(root,text="",bg="black")
label16= Label(root,text="",bg="black")
label17= Label(root,text="Developed By:",fg="white", bg="black")
label18= Label(root,text="  Vaibhav B. Revanwar",fg="white",bg="black")
label19= Label(root,text="  Pritam V. Kulkarni",fg="white",bg="black")
label20= Label(root,text="  Prasad Manedeshmukh",fg="white",bg="black")


label_2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()
label7.pack()
label8.pack()
label9.pack()
label10.pack()

screen_w =root.winfo_screenwidth()
screen_h =root.winfo_screenheight()

x = (screen_w/2)-(width/2)
y = (screen_h/2)-(height/2)
root.geometry('%dx%d+%d+%d' %(600,450,x,y))

#load=Tk.PhotoImage(file="/home/pi/Desktop/new_project/Logo_384_1.png")
#img10=Label(root,image=load)
#img10.image=load
#img10.place(x=0,y=0)

def loginpage():
    login = Tk.Tk()
    login.geometry('%dx%d+%d+%d' %(450,200,450,260))
    loginf= Frame(login)
    login.title("Login")
    label_3= Label(loginf,text="Provide Valid Username and Password to get current consumption")
    label_3.pack()
    w1=Label(loginf,text="Username:")
    w2= Label(loginf,text="Password")
    t1=Entry(loginf)
    t1.focus_set()
    t2=Entry(loginf,show="*")
    w1.pack()
    t1.pack()
    w2.pack()
    t2.pack()
    m=Label(loginf,text="")
    m.pack()
    def dbpage1():
        txt= t1.get()
        txt1 = t2.get()
        def exe():
                execfile("../motion_detector.py")
        if txt=="admin" and txt1=="admin":
            q=Tk.Tk()
            q.title("Welcome admin")
            qf=Frame(q)
            blogin4= Button(qf, text="Start monitering",fg="black",bg="red",command=exe)
            blogin4.pack()
            qf.pack()
        else:
            m.config(text="Invalid username or password ")
            t1.delete(0,END)
            t2.delete(0,END)
            t1.focus_set()
    
    
            
    def dbpage():
        txt= t1.get()
        txt1 = t2.get()
        
        if txt=="walchand" and txt1=="XYZ":
            db = Tk.Tk()
            db.geometry('%dx%d+%d+%d' %(200,100,550,350))
            db.title("Congratulations !!")
            dbf= Frame(db)
            x=Label(dbf,text="You are successfully Logged to system")
      
            def qrypage():
                db=MySQLdb.connect(host="localhost",user="root",passwd="root",db="Energy_conservation_data")

                cur=db.cursor()
                d=datetime.datetime.now()
                d1=d.strftime("%Y-%d-%m")
                sql="select sum(CONSUMED) from INSTANCES where DATE = '%s'" % ( d1)
                result=''
                try:
                    cur.execute(sql)
                    result=cur.fetchone()
                    db.commit()
                except:
                    print("Error")
                    db.rollback()
      
                qry = Tk.Tk()
                qry.geometry('%dx%d+%d+%d' %(200,50,550,350))
                qry.title("INFO")
                qryf = Frame(qry)
                qry.maxsize(width=900,height=900)
                
                label12= Label(qryf,text="Total usage is "+str(round(result[0],4))+" Watts uptil now")
                label12.pack()
                label24= Label(qryf,text="Your savings: "+((d.hour-9)*3600+(d.minute)*60+(d.seconds))*0.00139+"Watts !!")
                qryf.pack()
            b2= Button(dbf,text="Get Information from the database",command=qrypage)
            x.pack()
            b2.pack()
            dbf.pack()
        else:
            m.config(text="Invalid username or password as user ")
            t1.delete(0,END)
            t2.delete(0,END)
            t1.focus_set()
    blogin= Button(loginf, text="LOGIN AS USER",fg="black",bg="red",command=dbpage)
    blogin.pack()
    blogin1=Button(loginf, text="Click here to LOGIN AS ADMIN",fg="black",bg="red",command=dbpage1)
    blogin1.pack()
    loginf.pack()
    
bcontinue = Tk.Button(root,text="Continue",fg="red",bg="grey",command=loginpage)

label15.pack()
label16.pack()
bcontinue.pack()
label13.pack()
label14.pack()
label17.pack()
label18.pack()
label19.pack()
label20.pack()

root.mainloop()
