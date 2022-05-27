
from tkinter import *


idt = '예시'
sco=3000
rankd = dict(예시=0)
tri=1

ca=[]
caso=[0]
'''
ra=1
open("ranking.txt",r) as f:
    
while ra:
    ra=f.readline()
    ca.append(ra.split())
    
'''
    


win = Tk()
win.geometry("1000x500")
win.title("end")
win.option_add("*Font","맑은고딕 25")

frame5=Frame(win)
frame5.grid(row=0, column=0, sticky=W+E+N+S) 

frame5.pack(anchor="center", pady=30)
if tri==1:
    e_label1=Label(frame5,text="~성공~",padx=20,pady=10)

    e_label1.pack()
else:
    e_label1=Label(frame5,text="ㅠ~실패~ㅠ",padx=20,pady=10)

    e_label1.pack()


e_label2=Label(frame5,text=idt+':'+str(sco)+'점')

e_label2.pack()

f=open(".txt","w")
f.write("\n"+idt+" : "+str(sco))


def f1(x):
    return x[1]
sorted1=sorted(rankd.items(),key=f1)


def change():
    e_label1.config(text="ㅠ~실패~ㅠ")
open('ranked','r',encoding)

listbox =Listbox(frame5,selectmode="extended",height=5)
listbox.insert(END,ca[caso[1]][0]+" : "+ca[caso[1]][1])
listbox.insert(END,ca[caso[2]][0]+" : "+ca[caso[2]][1])
listbox.insert(END,ca[caso[3]][0]+" : "+ca[caso[3]][1])
listbox.insert(END,ca[caso[4]][0]+" : "+ca[caso[4]][1])
listbox.insert(END,ca[caso[5]][0]+" : "+ca[caso[5]][1])
listbox.pack()
win.mainloop()

