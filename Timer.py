from tkinter import*                  #importing nessesarry librarys
from tkinter import messagebox
import time


window=Tk()         #definging window

window.geometry('500x500')               #configuring window size 

window.title('Timer')
window.config(bg='orange')
hour = StringVar()
minute = StringVar()
second = StringVar()
hour.set("0")
minute.set("0") 
second.set("0")  

                
def countdown():
    start_b.place_forget()
    total=int(hour_e.get())  *3600 + int(minute_e.get()) *60 + int(second_e.get())
    while total>-1:

        mins, secs = divmod(total,60)
        hours = 0
        if mins>60:
            hours, mins = divmod(mins,60)
        hour.set(hours)
        minute.set(mins)
        second.set(secs)
        hour_e.config(state=DISABLED)
        second_e.config(state=DISABLED)
        minute_e.config(state=DISABLED)
        window.update()
        time.sleep(1)
        if total==0:
            messagebox.showinfo('STOP','Time Is Up!')
        total=total-1
        


title_l=Label(window,text='Import the correct digits into the timer')    #title
hour_e=Entry(window,width=3,font=('Arial',18,''),textvariable=hour)                        #entrys
minute_e=Entry(window,width=3,font=('Arial',18,''),textvariable=minute)
second_e=Entry(window,width=3,font=('Arial',18,''),textvariable=second)
start_b=Button(window,height='3',text='Start',command=countdown)          
title_l.place(x=150,y=60)         #placing buttons,entrys,labels
hour_e.place(x=150,y=200)
minute_e.place(x=200,y=200)
second_e.place(x=250,y=200)
start_b.place(x=300,y=200)

def starttimer():
       start_b.place_forget()
       countdown







window.mainloop()
