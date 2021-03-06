#importing modules on which we work
from tkinter import *
import calendar

#making our main window
root=Tk()
root.title("Calender")
root.geometry("240x200")
root.resizable(0,0)

#defining function for displaying the calender
def show():
    a=int(spin1.get())
    b=int(spin2.get())
    cal=calendar.month(b,a)  #here b is year and a is month

    txt.delete('0.0',END) #for removing old content of textbox
    txt.insert(INSERT,cal)  #for adding new calender data

#creating label
lb1=Label(root,text="Month",font=("arial",9,"bold")).place(x=15,y=0)
lb2=Label(root,text="Year",font=("arial",9,"bold")).place(x=115,y=0)

#creating spinbox
spin1=Spinbox(root,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4)
spin1.place(x=60,y=0)
spin2=Spinbox(root,from_=1990,to=2100,width=4)
spin2.place(x=150,y=0)

#creating button
bt=Button(root,text="Show",font=("arial",9,'bold'),command=show).place(x=100,y=30)

#creating textbox to display calender
txt=Text(root,width=24,height=8)
txt.place(x=20,y=57)

root.mainloop()
