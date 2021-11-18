from tkinter import *
from datetime import datetime
#---------------------------------------------------------------------
win = Tk() #창 생성

win.geometry("300x100") #창 크기 설정
win.title("what time?") # 창 타이틀 설정
win.option_add("*Font","맑은고딕 10") #창의 폰트, 크기 변경

#-------------------------------------------------------------
btn = Button(win) #win이라는 창에 버튼만든다

btn.config(text ="현재 시간")#버튼 내용 
btn.config(width=25, height=2) #버튼 크기설정

#버튼 기능
def what_time():
    dnow = datetime.now()
    btn.config(text = dnow)
btn.config(command = what_time) #버튼의 기능 설정

btn.pack() #버튼위젯 생성후 항상 팩해줘야한다(배치하기)
#-------------------------------------------------------------



win.mainloop() #창 실행
#---------------------------------------------------------------------
