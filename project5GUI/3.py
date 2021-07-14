from tkinter import *
import requests
#---------------------------------------------------------------------
# ent = Entry(win) #입력창만들기
# ent.get() #입력창 내용추출
# ent. pack() #입력창 배치
#---------------------------------------------------------------------
win = Tk()
win.title("로또번호 검색")
win.geometry("300x100")
win.option_add("*Font","궁서 20")

ent = Entry(win)
ent.pack()

btn = Button(win)
btn.config(text = "로또당첨 번호 확인")

def lotto_p():
    import requests
    from bs4 import BeautifulSoup
    n = ent.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)
    req = requests.get(url) #url로부터 html 가져오기
    #print(req.text)
    soup = BeautifulSoup(req.text, "html.parser") # html 태그 정리하기
    #print(soup)
    txt = soup.find("div", attrs = {"class", "win_result"}).get_text() #div ,class,win_result 찾고, 문자만 추출하기
    #print(txt)
    no = txt.split("\n") #얻은 결과를 엔터 단위로 리스트화 하기
    #print(no)
    num_list = no[7:13] # 리스트에서 당첨결과의 값만 인덱싱
    #print(num_list)
    bonus = no[-4] # 리스트에서 보너스 결과의 값만 인덱싱
    #print(bonus)
    win2 = Tk()
    win2.title("로또번호 결과")
    win2.geometry("300x100")
    win2.option_add("*Font","궁서 20")
    btn001 = Button(win2, text = num_list)
    btn001.pack()
    btn002 = Button(win2, text = bonus)
    btn002.pack()
    win2.mainloop()
    #num_list.append(bonus) #보너스결과를 num_list에 추가해서 리스트화 한다

    #btn.config(text = num_list) # 버튼을 누루고 나면 버튼글자가 결과로 바뀜

btn.config(command = lotto_p)
btn.pack()

win.mainloop()

