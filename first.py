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

#게임 참여자 정보를 저장할 클래스
class Member:
    def __init__(self, memId=None, score=0, time=0):
        self.__memId = memId
        self.__score = score
        self.__time = time
    def getInfo(self):
        return self.__score, self.__time
    def setInfo(self, score, time):
        self.__score = score
        self.__time = time

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
        a,b, c, d=l.split()
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

#Member 객체 생성
mem = Member()

#id와 password가 완벽히 조건 수행했을 때, Member 객체를 생성하기 위해 따로 저장하는 변수를 둔다.
playingid = 0


#아이디, 비밀번호 파일에 추가하기
def a_member(idcheck, pdcheck, m_id, m_pd):
    global playingid
    playingid= 0
    
    if(idcheck==1) and(pdcheck==1):
        playingid = m_id
        f=open('first.txt','a+')
        f.write('{} {}\n'.format(m_id, m_pd))
        f.close()
        openFrame(frame3)
    elif(idcheck==1) and (pdcheck!=1):
        prod.config(command=lambda:[messagebox.showinfo('회원가입 오류','비밀번호 일치 여부를 확인해주세요.')])
    else:
        prod.config(command=lambda:[messagebox.showinfo('회원가입 오류','아이디 중복체크를 눌러주세요.')])
        

#로그인 화면에서 아이디, 비밀번호 확인
def isExist(id_one, pd_one):
    global playingid
    
    f=open('first.txt','r')
    l = f.readline()
    k=0
    
    while l:
        mem_id, mem_pd, score, time=l.split()
          
        if (mem_id==id_one):
            if(mem_pd==pd_one):
                k=1
                playingid = mem_id
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
frame1 = Frame(root, bg = 'white') #맨 처음 화면
frame1.grid(row=0, column=0, sticky=W+E+N+S)

frame2 = Frame(root, bg = 'white') #회원가입 화면
frame2.grid(row=0, column=0, sticky=W+E+N+S)

frame3 = Frame(root, bg = 'white') #주제 선택 화면
frame3.grid(row=0, column=0, sticky=W+E+N+S)

frame4 = Frame(root, bg = 'white') #퀴즈 진행 화면
frame4.grid(row=0, column=0, sticky=W+E+N+S)






#frame1 >> 첫 화면 만들기
#레이블 만들기
tl = Label(frame1)
tl.config(text="⛰으쌰 열고개⛰", font=('맑은 고딕', 20,'bold'))
tl['fg']='white'
tl['bg']='forestgreen'
tl.pack(pady=40)

#id와 비밀번호 넣을 보조 프레임
frame1_1 = Frame(frame1, bg = 'white')
frame1_1.pack(anchor="center", pady=30)

#id 칸
idl = Label(frame1_1)
idl.config(text="아이디 : ", bg = 'white')
idl.grid(row=0,column=0, padx=10, pady=10)

idt = Entry(frame1_1)
idt.grid(row=0,column=1, padx=10, pady=10)


#비밀번호 칸
pd = Label(frame1_1)
pd.config(text="비밀번호 : ", bg = 'white')
pd.grid(row=1,column=0, padx=10, pady=10)

pdt = Entry(frame1_1)
pdt.grid(row=1,column=1, padx=10, pady=10)


#시작칸 만들기 > 이후에 이벤트 처리해서 클릭, 엔터 두개 처리해야 함
stl = Button(frame1)
stl.config(text = "시작해볼까요?", command=lambda:[isExist(idt.get(), pdt.get())])
stl.config(width = 20)
stl.pack(anchor="center", pady=10)


#회원가입 만들기
gol = Button(frame1)
gol.config(text = "회원가입")
gol.config(command = lambda:[openFrame(frame2)])
gol.pack(anchor="center", pady=10)




#frame2>> 2번째 회원가입 화면만들기
tl2 = Label(frame2, background = 'white')
tl2.config(text = "[사용자 등록]", font=('맑은 고딕', 18, 'bold'))
tl2['bg']='darkgrey'
tl2.pack(pady=40)

#id, 비밀번호, 비밀번호 확인 넣을 보조 프레임
frame2_1 = Frame(frame2, bg = 'white')
frame2_1.pack(anchor="center",pady=5)

idl2 = Label(frame2_1)
idl2.config(text="아이디",font=('맑은 고딕', 13))
idl2.grid(row=0,column=0, padx=10, pady=10)

idlt = Entry(frame2_1, width=15)
idlt.grid(row=0,column=1, padx=10, pady=10)


#아이디 중복확인 버튼
twiceid = Button(frame2_1)
twiceid.config(text = "ID 중복확인", font=('맑은 고딕', 10), command=lambda:[twiceCheck(idlt.get())])
twiceid.grid(row=0,column=2, padx=20, pady=10)


pd2 = Label(frame2_1)
pd2.config(text="비밀번호",font=('맑은 고딕', 13))
pd2.grid(row=1,column=0, padx=10, pady=10)

pdt2 = Entry(frame2_1, width=15)
pdt2.grid(row=1,column=1, padx=10, pady=10)


pdtw = Label(frame2_1)
pdtw.config(text="비번확인",font=('맑은 고딕', 13))
pdtw.grid(row=2,column=0, padx=10, pady=10)

pdte = Entry(frame2_1, width=15)
pdte.grid(row=2,column=1, padx=10, pady=10)


#비밀번호 일치확인 버튼 
twicepd = Button(frame2_1)
twicepd.config(text = "비밀번호 일치 확인", font=('맑은 고딕', 10),command=lambda:[pdSame(pdt2.get(), pdte.get())])
twicepd.grid(row=2,column=2, padx=20, pady=10)


#이전 홈화면으로 돌아가기
gohome = Button(frame2)
gohome.config(text="🏠 이전 화면으로 돌아가기 🏠",font=('맑은 고딕', 13), command=lambda:[openFrame(frame1)])
gohome.pack(pady=25)


#아이디 중복체크, 비밀번호 일치까지 했을 때 생성하기 > 메시지 박스 함수 만들기
prod = Button(frame2)
prod.config(text = "생성하기", font=('맑은 고딕', 13))
prod.pack(pady=10)
prod.config(command=lambda:[a_member(idcheck, pdcheck, idlt.get(), pdt2.get())])



#frame3>> 3번째 주제 선택 화면 만들기

#주제 선택 시 랜덤으로 파일 불러오는 명령어
#for문 돌리면서 if button click이면 해당 함수 실행

from random import randint

global answer
answer=''
global hint
hint=[0,]

def open_randfile(number):
    n=randint(number*4+1, (number+1)*4)
    name=str(n)+'.txt' #해당 번호 클릭하면 해당 주제에 맞는 4개의 파일 중 랜덤으로 하나 실행
    fi=open(name, 'r', encoding='UTF8')
    answer=fi.readline()
    for i in range(1,11):
        hint.append(fi.readline())
    openFrame(frame4)
    

f3l = Label(frame3,text = "주제를 선택하세요",font =('맑은 고딕', 18,'bold'),bg = "forestgreen",fg='white')
f3l.pack(pady=40)
frame3_1 = Frame(frame3, background = 'white') #주제 선택 화면
frame3_1.pack(anchor="center",pady=30)

subj = ['영화','음식','동물','캐릭터']

btn_subj=[0,]

for i in range(1,5):
    btn_sub = Button(frame3_1, text=subj[i-1], font=('맑은 고딕', 15),width=10,bd=10)
    btn_subj.append(btn_sub)

num=1
for i in range(2):
    for j in range(2):
        btn_subj[num].grid(row=i,column=j,padx=15,pady=15)
        num+=1


#각 버튼을 클릭했을 때 open_randfile 함수 실행되도록 하기
for i in range(1,5):
    btn_subj[i].config(command=lambda z=i:[open_randfile(z-1)])


#frame4>> 4번째 퀴즈 진행 화면 만들기
f4l = Label(frame4,text = "힌트",font =('맑은 고딕', 18,'bold'), fg ="white",bg = "forestgreen")
f4l.pack(pady=40) # 첫 라벨 구현

f4l_1 = Label(frame4,text = "마음에 드는 번호를 선택하면 힌트가 보입니다.\n힌트는 한 번씩만 볼 수 있습니다.",font =('맑은 고딕', 13), bg = 'white')
f4l_1.pack() # 두번째 라벨 구현

frame4_1 = Frame(frame4, background = 'white') # 버튼 grid로 배치하기 위해 보조 frame 형성
frame4_1.pack(anchor="center", pady=30)

btn_hint=[0,] # btn_hint[n] = n번 버튼이 되게 0을 넣어둠.

for i in range(1,11):
    btn_hin = Button(frame4_1, text=i, font=('맑은 고딕',12), width = 8, bd=10)
    btn_hint.append(btn_hin)

num=1
for i in range(2):
    for j in range(5):
        btn_hint[num].grid(row=i, column=j, padx=10, pady=10)
        num+=1
        

frame4_2 = Frame(frame4, background = 'white') #버튼 grid로 배치하기 위해 보조 frame 형성
frame4_2.pack(anchor="center", pady=10)


#정답 입력 칸
ans_l = Label(frame4_2, text="정답 : ", font=('맑은 고딕',12), bg = 'white')
ans_l.grid(row=0,column=0, padx=10)

ans_in = Entry(frame4_2)
ans_in.grid(row=0, column=1,padx=10)

btn_ans = Button(frame4_2, text="확인", font=('맑은 고딕', 12))
btn_ans.grid(row=0, column=2)



#힌트 확인하기
#새로 생성 안하면 힌트 길이따라서 윗쪽 줄 친구들이 계속 움직임
#디자인을 위해.. 힌트칸 넣을 프레임을 새로 생성
frame4_3 = Frame(frame4, bg = 'white') 
frame4_3.pack(anchor="center", pady=10)

hint_1=Label(frame4_3, text="힌트 내용", font=('맑은 고딕',12), bg = 'white')
hint_1.grid(row=0, column=0)


#X표시 확실하게 보였으면 싶어서 bd를 없앴음
#너비랑 높이 변화 최대한 없게 하는 값 넣음
def button_hint(number):
    s=hint[number]
    btn_hint[number].configure(text='X',font=('맑은 고딕',12), state='disable', width=8, bd=10, bg = '#A4A4A4',disabledforeground='white')
    hint_1.configure(text=s)

for i in range(1,11):
    btn_hint[i].config(command=lambda x=i:[button_hint(x)])
    


'''
sco=3000
rankd = {'123':0,'김':2999,'정':2998,'최':2997,'편':2996}
if ans_in==hint[0]:
    if idt in rankd:
        if rankd[idt]<sco:
            rankd[idt]=sco
    else:
        rankd[idt]=sco
'''

openFrame(frame1)
root.mainloop()

