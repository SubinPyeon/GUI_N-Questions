from tkinter import *

#창 생성하기
root = Tk() 
root.geometry("600x400")
root.title("열고개 수수께끼")
root.option_add("*Font","맑은고딕25")
root.resizable(False, False)

#프레임 전환하기
def openFrame(frame):
    frame.tkraise()

#화면 프레임 만들기
frame1 = Frame(root)
#frame1.pack(expand = True, anchor="center") #아 프레임 이쁘게 하고 싶은데 방법 찾기
frame1.grid(row=0, column=0, sticky="nsew") 

frame2 = Frame(root)
frame2.grid(row=0, column=0, sticky="nsew")

#레이블 만들기
tl = Label(frame1)
tl.config(text="으쌰 열고개")
tl.place(x=230, y=20)
tl.pack()

#id만드는 칸
idl = Label(frame1)
idl.config(text="아이디")
idl.place(x=100, y=100)
idl.pack()

idt = Entry(frame1)
idt.place(x=230, y=100)
idt.pack()


#비밀번호 만드는 칸
pd = Label(frame1)
pd.config(text="비밀번호")
pd.place(x=100, y = 150)
pd.pack()

pdt = Entry(frame1)
pdt.place(x=230, y=150)
pdt.pack()


#시작칸 만들기 > 이후에 이벤트 처리해서 클릭, 엔터 두개 처리해야 함
'''btnpress가 btnpress() 함수 호출하는 것'''
stl = Button(frame1)
stl.config(text = "시작해볼까요?")
stl.config(width = 20)
#stl.config(command = btnpress)
stl.place(x=170, y=200)
stl.pack()

#회원가입 만들기
gol = Button(frame1)
gol.config(text = "회원가입")
gol.config(command = lambda:[openFrame(frame2)])
gol.place(x=100, y=300)
gol.pack()


#로그인 만들기
logl = Button(frame1)
logl.config(text= "로그인")
#logl.config(command = loginpress)
logl.place(x=350, y=300)
logl.pack()




#여기서부터 2번째 회원가입 화면만들기
tl2 = Label(frame2)
tl2.config(text = "사용자 등록")
tl2.place(x=200, y=20)
tl2.pack()

namel = Label(frame2)
namel.config(text="이름")
namel.place(x=100, y=100)
namel.pack()
namet = Entry(frame2)
namet.place(x=230, y=100)
namet.pack()

idl2 = Label(frame2)
idl2.config(text="아이디")
idl2.place(x=100, y=150)
idl2.pack()
idlt = Entry(frame2)
idlt.place(x=230, y=150)
idlt.pack()

twicet = Button(frame2)
twicet.config(text = "V")
twicet.place(x=300, y=150)

pd2 = Label(frame2)
pd2.config(text="비밀번호")
pd2.place(x=100, y=200)
pd2.pack()
pdt2 = Entry(frame2)
pdt2.place(x=230, y=200)
pdt2.pack()

pdtw = Label(frame2)
pdtw.config(text="비번확인")
pdtw.place(x=100, y=250)
pdtw.pack()
pdte = Entry(frame2)
pdte.place(x=230, y=250)
pdte.pack()

prod = Button(frame2)
prod.config(text = "생성하기")


openFrame(frame1)
root.mainloop()
