from tkinter import *
from tkinter import messagebox

#창 생성하기
root = Tk() 
root.geometry("600x400")
root.title("열고개 수수께끼")
root.option_add("*Font","맑은고딕25")
root.resizable(False, False)

#프레임 전환하기
def openFrame(frame):
    frame.tkraise()
#아이디 중복확인 > 파일 관리와 더불어서 조금 더 뒤에 수정해야함
#사용할 수 없는 아이디입니다. 해당 객체 넣어서 if문으로 추가하기
def twiceCheck():
    messagebox.showinfo('아이디 중복 확인','사용가능한 id입니다.')

#비밀번호 중복 함수만들기
def pdSame(a,b):
    if a==b:
        openFrame(frame3)
    else:
        messagebox.showinfo('비밀번호 일치 확인','비밀번호가 일치하지 않습니다.')

#로그인 화면에서 아이디, 비밀번호 찾는 함수만들기
def isExist(id_one, pd_one):
    f=open('Reposit.txt','r')
    l = f.readline()
    k=0

    while l:
        idcheck, pdcheck=l.split(' ')
        if (idcheck==id_one):
            if(pdcheck==pd_one):
                k=1
                openFrame(frame3)
                break
            else:
                k=1
                messagebox.showinfo('로그인 오류', '아이디 또는 비밀번호가 일치하지 않습니다.')
                break
        l=f.readline()
        
    if k==0:
        messagebox.showinfo('로그인 오류', '아이디 또는 비밀번호가 일치하지 않습니다.')
        
    


    
#화면 프레임 만들기
frame1 = Frame(root)
#frame1.pack(expand = True, anchor="center") #아 프레임 이쁘게 하고 싶은데 방법 찾기
frame1.grid(row=0, column=0, sticky="nsew") 

frame2 = Frame(root)
frame2.grid(row=0, column=0, sticky="nsew")

frame3 = Frame(root)
frame3.grid(row=0, column=0, sticky="nsew")
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
stl.config(text = "시작해볼까요?", command=lambda:[isExist(idt.get(), pdt.get())])
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
#아이디 중복확인 버튼 
twiceid = Button(frame2)
twiceid.config(text = "ID 중복확인", command=lambda:[twiceCheck()])
twiceid.place(x=300, y=150)
twiceid.pack()

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

#비번 일치확인 버튼 
twicepd = Button(frame2)
twicepd.config(text = "비밀번호 일치 확인", command=lambda:[pdSame(pdt2.get(), pdte.get())])
twicepd.place(x=300, y=150)
twicepd.pack()

#아이디 중복체크, 비밀번호 일치까지 했을 때 생성하기 > 메시지 박스 함수 만들기
prod = Button(frame2)
prod.config(text = "생성하기")
prod.pack()



openFrame(frame1)
root.mainloop()
