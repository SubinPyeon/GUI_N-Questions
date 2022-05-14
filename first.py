from tkinter import *
from tkinter import messagebox


#창 생성하기
root = Tk() 
root.geometry("600x500")
root.title("열고개 수수께끼")
root.option_add("*Font","맑은고딕25")
root.grid_rowconfigure(0, minsize=500)
root.grid_columnconfigure(0,minsize=600)
root.resizable(False, False)

#프레임 전환하기
def openFrame(frame):
    frame.tkraise()


#아이디, 비밀번호 파일에 추가하기
def a_member(idcheck, pdcheck, m_id, m_pd):
    if(idcheck==1) and(pdcheck==1):
        f=open('first.txt','a+')
        f.write('{} {}\n'.format(m_id, m_pd))
        f.close()
        openFrame(frame3)
    elif(idcheck==1) and (pdcheck!=1):
        prod.config(command=lambda:[messagebox.showinfo('회원가입 오류','비밀번호 일치 여부를 확인해주세요.')])
    else:
        prod.config(command=lambda:[messagebox.showinfo('회원가입 오류','{}//{}아이디 중복체크를 눌러주세요.'.format(idcheck, pdcheck))])
        


#id와 password가 완벽히 조건 수행했을 때 flag를 각각 idcheck, pdcheck로 전역변수를 둔다
idcheck=0
pdcheck=0


#아이디 중복 확인
def twiceCheck(isidexist):
    global idcheck
    
    f=open('first.txt','r')
    l=f.readline()
    flag=0
    
    while l:
        a,b=l.split()
        l=f.readline()
        if(a==isidexist):
            messagebox.showinfo('아이디 중복 확인','{}는 사용할 수 없는 아이디입니다.'.format(isidexist))
            flag=1
            break
          
    if(flag==0):
        idcheck=1
        messagebox.showinfo('아이디 중복 확인','{}는 사용할 수 있는 아이디입니다.'.format(isidexist))
    f.close()


#비밀번호 중복 확인
def pdSame(a,b):
    global pdcheck
    
    if a==b:
        pdcheck=1
        messagebox.showinfo('비밀번호 일치 확인','비밀번호가 일치합니다.')
    else:
        messagebox.showinfo('비밀번호 일치 확인','비밀번호가 일치하지 않습니다.')
        

#로그인 화면에서 아이디, 비밀번호 확인
def isExist(id_one, pd_one):
    f=open('first.txt','r')
    l = f.readline()
    k=0
    
    while l:
        mem_id, mem_pd=l.split()
          
        if (mem_id==id_one):
            if(mem_pd==pd_one):
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
        
    f.close()


    
#화면 프레임 만들기
frame1 = Frame(root) #맨 처음 화면
frame1.grid(row=0, column=0, sticky=W+E+N+S) 

frame2 = Frame(root) #회원가입 화면
frame2.grid(row=0, column=0, sticky=W+E+N+S)

frame3 = Frame(root) #퀴즈 화면
frame3.grid(row=0, column=0, sticky=W+E+N+S)


#frame1 >> 첫 화면 만들기
#레이블 만들기
tl = Label(frame1)
tl.config(text="⛰으쌰 열고개⛰", font=('맑은 고딕', 20,'bold'))
tl['fg']='white'
tl['bg']='forestgreen'
tl.place(x=200, y=50)

#id 칸
idl = Label(frame1)
idl.config(text="아이디")
idl.place(x=100, y=150)

idt = Entry(frame1)
idt.place(x=230, y=150)


#비밀번호 칸
pd = Label(frame1)
pd.config(text="비밀번호")
pd.place(x=100, y = 200)

pdt = Entry(frame1)
pdt.place(x=230, y=200)


#시작칸 만들기 > 이후에 이벤트 처리해서 클릭, 엔터 두개 처리해야 함
stl = Button(frame1)
stl.config(text = "시작해볼까요?", command=lambda:[isExist(idt.get(), pdt.get())])
stl.config(width = 20)
stl.place(x=170, y=300)


#회원가입 만들기
gol = Button(frame1)
gol.config(text = "회원가입")
gol.config(command = lambda:[openFrame(frame2)])
gol.place(x=230, y=350)


#frame2>> 2번째 회원가입 화면만들기
tl2 = Label(frame2)
tl2.config(text = "[사용자 등록]", font=('맑은 고딕', 18, 'bold'))
tl2['bg']='darkgrey'
tl2.place(x=70, y=20)

idl2 = Label(frame2)
idl2.config(text="아이디",font=('맑은 고딕', 13))
idl2.place(x=70, y=100)

idlt = Entry(frame2, width=15)
idlt.place(x=180, y=100)


#아이디 중복확인 버튼
twiceid = Button(frame2)
twiceid.config(text = "ID 중복확인", font=('맑은 고딕', 10), command=lambda:[twiceCheck(idlt.get())])
twiceid.place(x=400, y=100)


pd2 = Label(frame2)
pd2.config(text="비밀번호",font=('맑은 고딕', 13))
pd2.place(x=70, y=150)

pdt2 = Entry(frame2, width=15)
pdt2.place(x=180, y=150)


pdtw = Label(frame2)
pdtw.config(text="비번확인",font=('맑은 고딕', 13))
pdtw.place(x=70, y=200)

pdte = Entry(frame2, width=15)
pdte.place(x=180, y=200)


#비밀번호 일치확인 버튼 
twicepd = Button(frame2)
twicepd.config(text = "비밀번호 일치 확인", font=('맑은 고딕', 10),command=lambda:[pdSame(pdt2.get(), pdte.get())])
twicepd.place(x=400, y=200)


#이전 홈화면으로 돌아가기
gohome = Button(frame2)
gohome.config(text="🏠 이전 화면으로 돌아가기 🏠",font=('맑은 고딕', 13), command=lambda:[openFrame(frame1)])
gohome.place(x=150, y=350)


#아이디 중복체크, 비밀번호 일치까지 했을 때 생성하기 > 메시지 박스 함수 만들기
prod = Button(frame2)
prod.config(text = "생성하기", font=('맑은 고딕', 13))
prod.place(x=240,y=280)
prod.config(command=lambda:[a_member(idcheck, pdcheck, idlt.get(), pdt2.get())])


openFrame(frame1)
root.mainloop()
