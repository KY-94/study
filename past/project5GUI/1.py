from tkinter import *

win = Tk() #창 생성


win.geometry("500x500") #창 크기 설정
win.title("sample") # 창 타이틀 설정
win.option_add("*Font","맑은고딕 25") #창의 폰트, 크기 변경
win.configure(bg="red") # 창색깔 변경

btn = Button(win, text="버튼") #win이라는 창에 text라는 내용으로 버튼만든다
btn.pack()#버튼위젯 생성후 항상 팩해줘야한다


win.mainloop() #창 실행