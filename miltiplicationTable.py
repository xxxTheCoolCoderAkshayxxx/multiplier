from tkinter import *
from tkinter.ttk import *
#main window
screen = Tk()
screen.title("Multiplication Table")

#Creating labels
titel=Label(screen,text="mathimatical table")
caption=Label(screen,text="number and range")
titel.grid(row=0,column=0,columnspan=3,pady=20)
caption.grid(row=1,column=0,padx=10)

#combo box creation
number=IntVar()
multiNum=Combobox(screen,text=number,width=5)
multiNum["values"]=tuple(range(51))
multiNum.grid(column=1,row=1)

#creating raido buttons
number2=IntVar()
radio1=Radiobutton(screen,text="10",variable=number2,value=10)
radio2=Radiobutton(screen,text="20",variable=number2,value=20)
radio3=Radiobutton(screen,text="30",variable=number2,value=30)
number2.set(10)
radio1.grid(column=3,row=1,padx=30)
radio2.grid(column=3,row=2,padx=30)
radio3.grid(column=3,row=3,padx=30)

#creating the multiplication function
def multiplication():
    tabels=""
    for i in range(number2.get()+1):
        tabels+=str(number.get())+"X"+str(i)+"="+str(number.get()*i)+"\n"
    tabel.configure(text=tabels)

#Creating the generate button
creating=Button(screen,text="Generate",command=multiplication)
creating.grid(column=1,row=4,pady=10)


tabel=Label(screen,anchor="center")
tabel.grid(row=5,column=1,pady=10)




screen.mainloop()