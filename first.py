from tkinter import *

 

class Cont1:

    def __init__(self, root):
        self.tl = Label(root)
        self.tl.config(text="☆으쌰 열고개☆")
        self.tl.place(x=200, y=20)
        self.tl.pack()

        self.idl = Label(root)
        self.idl.config(text="아이디")
        self.idl.place(x=100, y=100)
        self.idl.pack()
        self.idt = Entry(root)
        self.idt.place(x=230, y=100)
        self.idt.pack()

 
        self.pd = Label(root)
        self.pd.config(text="비밀번호")
        self.pd.place(x=100, y = 150)
        self.pd.pack()
        self.pdt = Entry(root)
        self.pdt.place(x=230, y=150)
        self.pdt.pack()


        self.stl = Button(root)
        self.stl.config(text = "시작해볼까요?")
        self.stl.config(width = 20)

        #self.stl.config(command = startpress)
        self.stl.place(x=170, y=230)
        self.stl.pack()


        self.gol = Button(root)
        self.gol.config(text = "회원가입")
        #gol.config(command = gopress)
        self.gol.place(x=100, y=300)
        self.gol.pack()

 

        self.logl = Button(root)
        self.logl.config(text= "로그인")
        #logl.config(command = loginpress)
        self.logl.place(x=350, y=300)
        self.logl.pack()

 


#창 생성하기

'''root라는 창을 만들었음'''
root = Tk() 
root.geometry("550x400")
root.title("열고개 수수께끼")
root.option_add("*Font","맑은고딕25")
root.resizable(False, False)

 

#프레임 생성하기

'''첫 화면 컨테이너 생성'''

container1 = Cont1(root)

 

 

root.mainloop()
