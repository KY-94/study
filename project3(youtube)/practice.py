
# 동영상 : https://www.youtube.com/watch?v=kWiCuklohdY&list=WL&index=6&t=4853s

# (0:00) 0.Intro
# (0:38) 1-1.소개
# (02:22) 1-2.환경설정
# (07:26) 2-1.숫자 자료형
# (11:42) 2-2.문자열 자료형
# (13:08) 2-3.boolean 자료형
# (15:05) 2-4.변수
# (22:08) 2-5.주석
# (23:57) 2-6.퀴즈 #1
# (25:48) 3-1.연산자
# (33:23) 3-2.간단한수식
# (36:26) 3-3.숫자처리함수
# (38:59) 3-4.랜덤함수
# (44:11) 3-5.퀴즈 #2
# (46:57) 4-1.문자열
# (48:24) 4-2.슬라이싱
# (55:09) 4-3.문자열처리함수
# (1:00:56) 4-4.문자열포맷
# (1:09:17) 4-5.탈출문자
# (1:15:47) 4-6.퀴즈 #3
# (1:22:31) 5-1.리스트
# (1:31:35) 5-2.사전
# (1:40:46) 5-3.튜플
# (1:43:19) 5-4.세트
# (1:48:44) 5-5.자료구조의 변경
# (1:50:47) 5-6.퀴즈 #4
# (1:57:33) 6-1.if
# (2:05:08) 6-2.for
# (2:09:33) 6-3.while
# (2:14:59) 6-4.continue 와 break
# (2:19:11) 6-5.한 줄 for
# (2:22:51) 6-6.퀴즈 #5
# (2:28:36) 7-1.함수
# (2:30:09) 7-2.전달값과 반환값
# (2:37:50) 7-3.기본값
# (2:41:32) 7-4.키워드값
# (2:43:07) 7-5.가변인자
# (2:47:55) 7-6.지역변수와 전역변수
# (2:53:58) 7-7.퀴즈 #6
# (2:58:59) 8-1.표준입출력
# (3:10:12) 8-2.다양한 출력포맷
# (3:17:45) 8-3.파일입출력
# (3:26:27) 8-4.pickle
# (3:30:22) 8-5.with
# (3:33:33) 8-6.퀴즈 #7
# (3:38:08) 9-1.클래스
# (3:47:04) 9-2._init_
# (3:48:34) 9-3.멤버변수
# (3:53:07) 9-4.메소드
# (3:59:29) 9-5.상속
# (4:02:54) 9-6.다중상속
# (4:10:08) 9-7.메소드 오버라이딩
# (4:17:03) 9-8.pass
# (4:19:31) 9-9.super
# (4:23:50) 9-10.스타크래프트 프로젝트 전반전
# (4:33:47) 9-11.스타크래프트 프로젝트 후반전
# (4:44:42) 9-12.퀴즈 #8
# (4:50:13) 10-1.예외처리
# (4:58:15) 10-2.에러 발생시키기
# (5:01:06) 10-3.사용자 정의 예외처리
# (5:04:28) 10-4.finally
# (5:06:19) 10-5.퀴즈 #9
# (5:14:23) 11-1.모듈
# (5:24:10) 11-2.패키지
# (5:30:30) 11-3._all_
# (5:34:16) 11-4.모듈 직접 실행
# (5:37:00) 11-5.패키지, 모듈 위치
# (5:40:33) 11-6.pip install
# (5:46:04) 11-7.내장함수
# (5:50:38) 11-8.외장함수
# (5:58:49) 11-9.퀴즈 #10
# (6:01:08) 12.Outro

#-------------------------------------------------------------------------------------------
# 문자열 자료형
# print('풍선')
# print("나비")
# print("ㅋ"*10)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# 불형 자료형 (참/거짓)
# print(5>10)
# print(True)
# print(False)
# print(not True)
# print(not (5>10))
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
#변수 -> 값을 저장하는 공간
# animal = "강아지"
# age = 4
# name = "연탄이"
# hobby = "산책"
# is_adult = age >= 3

# print("우리집" + animal + "의 이름은" + name +"이에요")
# hobby = "공놀이"
# print(name + "는" + str(age) +"살이며," + hobby + "을 아주 좋아해요")
# print(name, "는", age, "살이며,", hobby, "을 아주 좋아해요") #,다음에는 무조건 한칸 띄어진다 , ,일경우에는 문자열로 만들어주지 않아도 문제없다
# print(name + "는 어른일까요?" + str(is_adult))
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (36:26) 3-3.숫자처리함수
# print(5%3) #나머지 구하기 2
# print(5//3) #몫 구하기 1
# print(3 == 3) #앞뒤가 같다 True
# print(1 != 3) #앞뒤가 같지않다 True
# print(not(1 != 3)) # False
# print( (3>0) and (3<5)) # 앞뒤가 모두 참일때만 True 갖는다
# print( (3 >0) & (3<5)) # 앞뒤가 모두 참일떄만 true 갖는다 
# print( (3>0) or (3>5)) # 앞뒤 중하나의 값이 true면 true 갖는다
# print( (3>0) | (3>5)) # 앞뒤 중하나의 값이 true면 true 갖는다
# print( 5 > 4 > 3 ) # True
# print( 5 > 4 > 7 ) # False

# print(abs(-5)) # 절대값
# print(pow(4,2)) # 4^2
# print(max(5,12))# 최대
# print(min(5,12))# 최소
# print(round(3.14))#반올림

# from math import * # math 라이브러리에 있는 모든 것 * 들을 임폴트 하겠다
# print(floor(4.99)) #내림
# print(ceil(3.14))#올림
# print(sqrt(16))#제곱근
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
#(38:59) 3-4.랜덤함수
# from random import *
# print(random()) # 0.0~ 1.0 미만의 임의의값 
# print(randrange(1, 46)) # 1~ 46 미만의 임의의값
# print(randint(1, 45)) # 양끝을 모두 포함한상태의 임의의값
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (55:09) 4-3.문자열처리함수
# python = "PaYA"
# print(python.lower()) #소문자로 변경
# print(python.upper())# 대문자로 변경
# print(python[0].isupper())# 첫문자가 대문자인가?
# print(len(python)) # python 이라는 함수의 길이 숫자 구함
# print(python.replace("P", "Y",)) #python의 함수에서 P를 Y로 변형
# print(python.index("P")) #'P'가 몇번쨰부터 있는지?
# print(python.index("P",0)) # 'p'가 '0'번째부터 어디에 있는지?
# print(python.find("YA")) #"YA"를 찾아줌 없을경우 -1값
# print(python.count("Y")) # "Y"의 개수를 찾아줌

# (1:00:56) 4-4.문자열포맷
# print("a" + "b") #띄어쓰기 없이 붙여진다
# print("a" , "b") # 띄어쓰기후 붙여진다
# print( "나는 %d살 입니다" % 27) # d는 정수만
# print( "나는 %s을 좋아 합니다"  % "파이썬") # S는 문자열만
# print( "나는 %c로 시작합니다." % "A") # C는 문자1개
# print( "나는 %s색과 %s색 좋아해요" % ("파랑" , "빨강"))

# print("나는 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("블루" , "레드"))
# print("나는 {1}색과 {0}색을 좋아해요".format("블루" , "레드"))
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (1:09:17) 4-5.탈출문자
# print("백문이 불여일견\n백견이 불여일타")# \n : 줄바꿈
# print(" 저는 \"코딩\" 입니다.") # \: 는 뒤에 문자를 문자열로 인식 시킨다
# print("C:\\Users\\HOME\\Desktop\\ex>")# \\: = \
# print("red apple \rpine")# \r: 커서를 맨앞으로 이동
# print("Redd\bApple")# \b: 백스페이스(한글자삭제)
# print("Red\tApple")# \t : 탭을 하나 추가
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (1:22:31) 5-1.리스트
# subway = [10, 20, 30]
# print(subway.index(20)) # 20의 위치는 어디니?
# subway.append("하하") # "하하"를 맨뒤에 추가한다
# print(subway)
# subway.insert(1,"정형돈") # 1번자리에 "정형돈"을 넣는다
# print(subway)

# print(subway.pop()) #맨뒤에 있는 리스트를 가져온다(본래 리스트는 제거됨)
# print(subway)
# print(subway.pop()) #맨뒤에 있는 리스트를 가져온다(본래 리스트는 제거됨)
# print(subway)
# print(subway.pop()) #맨뒤에 있는 리스트를 가져온다(본래 리스트는 제거됨)
# print(subway)

# human = ["유재석", "정형돈", "유재석", "박명수"]
# print(human.count("유재석")) # 유재석은 몇 명 있는가?
# num = [ 5, 3, 2 ,9, 15]
# num.sort() # 순차적으로 정렬해줘
# print(num)
# num.reverse()# 역순으로 정렬해줘
# print(num)
# num.clear()# 리스트를 지워줘
# print(num)   
 
# num1 = [ 1,2,3,4 ]
# Str1 = ['가','나']
# num1.extend(Str1) # num리스트에 Str리스트 추가한다
# print(num1)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (1:31:35) 5-2.사전
# 키와 사물함 , 문제와 답 , 단어와 뜻
#cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])                       #[]로 키값과 벨류값 가져온다        없을경우는 프로그램을 바로 종료한다
# print(cabinet.get(3))                  #.get 으로 키값과 벨류값 가져온다 없을경우는 none 을 출력한다
# print(cabinet.get(5,"사용가능"))    #.get 으로 키값과 벨류값 가져온다 없을경우는 none 을 출력한다 또는  ,"말"로써 표시할 값을 준다

# print(3 in cabinet) #=true 키값 in 변수 에서 변수안에 키값이 있는지 확인한다
# print(5 in cabinet) #=false

# cabinet["c-20"] = "조세호" #cabinet 안에 c-20 키값을 만들고 변수로 조세호를 추가
# cabinet[3] = "김종국" #cabinet 안에 3키값의 변수를 김종국으로 업데이트 
# del cabinet[100] # 100번키값을 삭제
# print(cabinet)
# print(cabinet.keys()) # 현재 key 값만들을 보여준다
# print(cabinet.values()) # 현재 values 만들을 보여준다
# print(cabinet.items()) # 현재 있는 모든 값,변수 보여준다
# cabinet.clear #모든값 삭제
# print(cabinet) 
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (1:40:46) 5-3.튜플
#내용변경 및 추가를 할수 없음
# manu = ('돈까스', '치즈까스')
# print(manu[0]) # 0번째 1번째 값 가져온다
# print(manu[1]) # 0번째 1번째 값 가져온다

# (name, age, hobby) = ("김종국", 20, "코딩") # 한번에 선언가능하다
# print(name, age, hobby)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (1:43:19) 5-4.세트
# 중복이 안되고 , 순서가 없음
# my_set = {1,2,3,3,3,3,} #중괄호 사용
# python = set(["유재석", "조세호"]) # 리스트 사용,set 사용
# print(my_set) 

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "조세호"]) 
# print(java & python) # 자바와 파이썬 중 중복값 출력
# print(java.intersection(python))# 교집합

# print(java | python) #자바하거나 파이썬 할수 있는
# print(java.union(python)) #합집합

# print(java - python) #자바는하지만 파이썬 못하는
# print(java.difference(python)) #차집합

# python.add("감자") #추가
# python.remove("조세호") #제거
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (1:48:44) 5-5.자료구조의 변경
# manu = {"커피", "우유", "주스"}
# print(manu, type(manu))

# manu = list(manu) #세트였던 메뉴를 리스트[]로 바꾼다
# print(manu, type(manu))
# manu = tuple(manu) #세트였던 메뉴를 튜플()로 바꾼다
# print(manu, type(manu))
# manu = set(manu) #세트였던 메뉴를 세트{}로 바꾼다
# print(manu, type(manu))
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (1:57:33) 6-1.if
# weather = input("날씨ex)비,미세먼지>>> ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙겨")
# elif weather == "미세먼지":
#     print("마스크")
# else:
#     print("다필요없음")
        
# temp = int(input("기온은 몇도?>> "))
# if 30 <= temp:
#     print("날씨가 너무 덥다. 나가지 마라")
# elif 10 <= temp and temp<30:
#     print("나가도 좋아")
# elif 0 <= temp < 10:
#     print("외투입어")
# else:
#     print("너무추워")
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (2:05:08) 6-2.for

# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {} ".format(waiting_no))

# for waiting_no in range(1, 6):
#     print("대기번호 : {} ".format(waiting_no))
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (2:09:33) 6-3.while
# customer = "아이언맨"
# index = 5

#01
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회 ".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기 퇴었다.")
# while True:  #ctrl+c 강제 종료
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회 ".format(customer, index))
#     index += 1

#02
# customer = "토르"
# person = ""
# while customer != person:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("성함이 어떻게 되세요? ")
#     if customer == person: 
#         print("커피 여기 있습니다.")
#     else:
#         print("{0}, 님 아직 준비 되지 않았습니다.".format(person))   
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (2:14:59) 6-4.continue 와 break
# absent = [2, 5] # 2명 결석
# no_book = [7] # 책을 깜빡함
# for student in range(1, 10): # 1~10번까지 학생 존재
#     if student in absent:
#         continue #밑의 문장을 하지 않고 다음반복으로 넘어간다
#     elif student in no_book:
#         print("오늘 수업 여기까지. {}는 교무실로 따라와".format(no_book))
#         break #반복문을 바로 탈출함 다음 반복이 있든 없든
#     print("{}, 읽어봐".format(student))
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (2:19:11) 6-5.한 줄 for
#01
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student]
# print(student)

# #02
# student = ["iron man", "Thor", "i am groot"]
# student = [len(i) for i in student]
# print(student)

# #03
# student = ["iron man", "Thor", "i am groot"]
# student = [i.upper() for i in student]
# print(student)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (2:28:36) 7-1.함수
# def open_account(): #함수의정의
#     print("새로운 계좌가 생성되었습니다.")
# print(open_account())
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (2:30:09) 7-2.전달값과 반환값
# def deposit(balance, money): #입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money #리턴된 값을 balance에 저장한다.

# def withdraw(balance, money):#출금
#     if balance >= money:
#         print("출금되었다 잔액은 {}이다".format(balance - money))
#         return balance - money
#     else:
#         print("출금 실패됨, 잔액부족, 잔액은 {} 이다".format(balance))
#         return balance

# def withdraw_night(balance, money):#저녁 출금
#     commission = 100
#     print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance - money - commission)) 
#     return commission, balance - money - commission #2개의 값을 튜플로 반환

# balance = 0
# balance = deposit(balance, 5000)
# balance = withdraw(balance, 5000)
# commission, balance = withdraw_night(balance, 5000)
# deposit(balance, 5000)
# withdraw(balance, 5000)
# withdraw_night(balance, 5000)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (2:37:50) 7-3.기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이 : {1} \t 주사용언어: {2}".format(name, age, main_lang))
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#만약 같은 학교 같은 반 같은 수업 일경우 일일이 수정하지 않고 기본값을 통해 이용
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t 나이 : {1} \t 주사용언어: {2}".format(name, age, main_lang))
# profile("유재석")
# profile("김태호")
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (2:43:07) 7-5.가변인자
# def profile(name, age, *language): #가변인자를 사용해서 무제한으로 추가하거나 불러올수 있다
#     print("이름 : {0}\t 나이 : {1}".format(name, age), end=" ") #end=" "는 줄바꿈을 하지않고이어서다음줄을 출력한다는 의미
#     for lang in language:
#         print(lang, end=" ")
#     print()  

# profile("유재석", 20, "파이썬","자바","자바스크립트","C","C++")
# profile("유재석", 20, "파이썬","자바")
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (2:47:55) 7-6.지역변수와 전역변수
# 지역변수: 함수호출될때만 만들어졌다가 끝나면 사라지는것
# 전역변수: 어디서든지 부를수 있는 변수

# gun = 10
# def chekpoint(soldiers): #경계근무를 나갔다
#     global gun #전역변수인 gun을 사용한다(일반적으로 사용하지않음)
#     gun = gun - soldiers
#     print("함수내 남은총: {0}".format(gun))

# print("전체 총 : {0} ".format(gun))
# chekpoint(2) #2명이 근무
# print("남은 총 : {0} ".format(gun))

# gun = 10
# def chekpoint_ret(gun, soldiers): #일반적으로 변수를 2개 받는함수로 제작
#     gun = gun - soldiers
#     print("총기실내 남은총: {0}".format(gun))
#     return gun # 항상 리턴해주어 함수사용시 405줄의 변수 값을 변경 시켜준다

# print("부대 전체 총 : {0} ".format(gun))
# gun = chekpoint_ret(gun, 2)
# print("현재 부대 총 : {0} ".format(gun))
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# # (2:58:59) 8-1.표준입출력
# #01
# print("python", "java") #중간이 띄어쓰기된다
# print("python" + "java") #중간에 띄어쓰기 없음
# print("python", "java", sep=",") #콤마,중간에 무엇이 들어 갈지 지정할수 있다
# print("python", "java", sep=" vs ")

# print("python", "java", sep=" vs ", end=" ? ") # 마지막에 무엇이 들어갈지 지정가능 뒤에있는 문장은 연이어서 출력(한문장출력)
# print("end사용하면 바로 다음으로 입력된다")

# #02
# import sys
# print("python", "java", file=sys.stdout) #표준 출력으로 문장이 찍힌다(로그처리를 할때 표준출력에대한건 잘표시됨)
# print("python", "java", file=sys.stderr) #표준 에러로 출력이 된다(로그처리를 할떄 표준에러로 출력되면 확인을 하기 쉬움)

# #03
# scores = {"수학":0, "영어":50, "코딩":100} #딕셔너리로 정의

# for subject, score in scores.items():
#     print(subject, score) # 정렬되지 않았다

# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # 과목은 8개의 공간을 확보한뒤 왼쪽정렬, 스코어는 4칸의 공간을 확보한뒤 오른쪽정렬

# #04 - 은행대기 순번표 001 002 003
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3)) # 3자리만큼 공간을 확보하고 그공간에 0 값을 넣는다

# #05 
# answer = input("숫자,문자 모두 문자열형태로 인풋된다")
# print(type(answer))    
# print(answer)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (3:10:12) 8-2.다양한 출력포맷
# print("{0: >10}".format(500)) # 빈자리는 빈공간으로,오른쪽정렬,총 10자리 (이떄 숫자는 -값은 나오지만 +값은 +안붙음)
# print("{0: >10}".format(-500)) # 빈자리는 빈공간으로,오른쪽정렬,총 10자리 (이떄 숫자는 -값은 나오지만 +값은 +안붙음)

# print("{0: >+10}".format(500)) # 빈자리는 빈공간으로,오른쪽정렬,총 10자리 +,- 부호 붙이기
# print("{0: >+10}".format(-500)) # 빈자리는 빈공간으로,오른쪽정렬,총 10자리 +,- 부호 붙이기

# print("{0:_<+10}".format(500)) # 빈자리는 _로, 왼쪽정렬, 총10자리, 부호붙이기
# print("{0:_<+10}".format(-500)) # 빈자리는 _로, 왼쪽정렬, 총10자리, 부호붙이기

# print("{0:+,}".format(10000000000000)) # 3자리마다 콤마 붙이기, 부호 붙이기
# print("{0:+,}".format(-10000000000000)) # 3자리마다 콤마 붙이기, 부호 붙이기

# print("{0:^<+30,}".format(10000000000)) #3자리마다 콤마, 부호, 자리수10자리 , 빈칸은 ^로 채우기, 왼쪽정렬

# print("{0:f}".format(5/3)) #소수점을 표시
# print("{0:.2f}".format(5/3)) #소수점을 두번째 자리까지만 표시 = 소수점 3째자리에서 반올림 해줘
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (3:17:45) 8-3.파일입출력

# score_file = open("score.txt", "w", encoding="utf8") # 파일을 쓰기용도로 연다
# print("수학 : 0", file=score_file) #스코어 파일에 프린트문(다채운뒤 엔터) 삽입
# score_file.close()# 파일은 항상 열고 닫고 까지 해준다

# score_file = open("score.txt", "a", encoding="utf8") # 파일을 내용추가 용도로 연다
# score_file.write("영어 : 0") #스코어 파일에 삽입 (이때는 연이어서 붙여진다) 따라서 \n 사용
# score_file.write("\n코딩 : 0") #스코어 파일에 삽입 (이때는 연이어서 붙여진다)
# score_file.close()# 파일은 항상 열고 닫고 까지 해준다

# score_file = open("score.txt", "r", encoding="utf8") # 파일을 읽는 용도로 연다
# print(score_file.read()) # 스코어파일의 모든 내용을 터미널로 읽는다 (프린트문은 항상 엔터를 쳐준다)
# score_file.close()# 파일은 항상 열고 닫고 까지 해준다

# score_file = open("score.txt", "r", encoding="utf8") # 파일을 읽는 용도로 연다
# #01
# print(score_file.readline()) # 스코어파일의 내용을 한줄씩 터미널로 읽는다 ()
# print(score_file.readline()) # 스코어파일의 내용을 한줄씩 터미널로 읽는다 ()
# print(score_file.readline()) # 스코어파일의 내용을 한줄씩 터미널로 읽는다 ()
# #02
# print(score_file.readline(), end="") # 스코어파일의 내용을 한줄씩 터미널로 읽는다 (end=""을이용해 중간띄기 없앤다)
# print(score_file.readline(), end="") # 스코어파일의 내용을 한줄씩 터미널로 읽는다 (end=""을이용해 중간띄기 없앤다)
# print(score_file.readline(), end="") # 스코어파일의 내용을 한줄씩 터미널로 읽는다 (end=""을이용해 중간띄기 없앤다)
# score_file.close()# 파일은 항상 열고 닫고 까지 해준다

# score_file = open("score.txt", "r", encoding="utf8") # 파일을 읽는 용도로 연다
# while True:
#     line = score_file.readline() #반복문으로 쭉 한줄씩 계속 읽어 준다
#     if not line:
#         break
#     print(line, end="")
# score_file.close()# 파일은 항상 열고 닫고 까지 해준다

# score_file = open("score.txt", "r", encoding="utf8") # 파일을 읽는 용도로 연다
# lines = score_file.readlines() #각 라인을 list형태로 저장한다 [1,2,3,4]
# for line in lines: #lines라는 리스트를 반복적으로 line에 순서대로 넣는다
#     print(line, end="")
# score_file.close()# 파일은 항상 열고 닫고 까지 해준다
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (3:26:27) 8-4.pickle (유용한 라이브 러리)
# import pickle
# profile_file = open("profile.pickle","wb") #프로필.픽클이라는 파일을 만들고, 쓰기형식은 wb, 유니코드는 지정 안해도됨
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구","골프","코딩"]} # 프로파일이라는 변수에 딕셔너리,리스트 저장
# pickle.dump(profile, profile_file) # 프로파일의 내용을 프로필파일에 쓴다
# profile_file.close() #꼭 닫아준다

# profile_file = open("profile.pickle","rb") 
# profile = pickle.load(profile_file) # 프로파일이라는 파일을 읽어온다
# print(profile)
# profile_file.close() #꼭 닫아준다
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (3:30:22) 8-5.with

# with open("study.txt","w",encoding="utf8") as study_file: #파일을 만들어서, as의미 == study_file에 저장한다
#     study_file.write("2줄로 파일생성 및 저장 ,읽기")

# with open("study.txt","r",encoding="utf8") as study_file: 
#     print(study_file.read())
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (3:38:08) 9-1.클래스
# 클래스는 붕어빵틀이다. 재료를 넣으면 틀에의해 붕어빵(객체)가 자동으로 생성된다
# class Unit: #클래스 생성
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{}유닛이 생성되었습니다".format(name))
#         print("체력은{}, 공격력은{}".format(hp, damage))

# Unit("마린", 10, 5)
# Unit("탱크", 50, 100)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (3:48:34) 9-3.멤버변수

# class Unit: 
#     def __init__(self, name, hp, damage):
#         self.name = name #.name 쓰는걸 멤버변수라고 함
#         self.hp = hp
#         self.damage = damage
#         print("{}유닛이 생성되었습니다".format(name))
#         print("체력은{}, 공격력은{}".format(hp, damage))

# tank = Unit("탱크",80,5) # 탱크라는 객체를 먼저 출력해야함
# print("유닛이름: {}, 공격력 {}".format(tank.name, tank.damage)) #.변수로 바로 사용 가능

# tank2 = Unit("탱크2",80,5) # 탱크라는 객체를 먼저 출력해야함
# print("유닛이름: {}, 공격력 {}".format(tank2.name, tank2.damage)) #.변수로 바로 사용 가능

# tank.sizemod = "시즈모드" #외부에서 멤버 변수를 만들어 줄수 있음
# print("{}는 현재 {} 중입니다.".format(tank.name, tank.sizemod)) #탱크1에서만 현재 시즈모드 저장됨
# print("{}는 현재 {} 중입니다.".format(tank2.name, tank2.sizemod))#탱크2는 시즈모드라는 것이 없음(기존에있는다른객체에는 적용x)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (3:53:07) 9-4.메소드==각기능 
# class Attack_Unit: 
#     def __init__(self, name, hp, damage):
#         self.name = name 
#         self.hp = hp
#         self.damage = damage
#         print("{}유닛이 생성되었습니다".format(name))
#         print("체력은{}, 공격력은{}".format(hp, damage))

#     def attack(self, location):#공격 메소드
#         print("{0} : {1} 방향으로 적군을 공격합니다. 데미지 [{2}]".format(self.name,location,self.damage))

#     def dameged(self, damage):#피해 메소드
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0} : 파괴 되었습니다.".format(self.name))

# firebat1 = Attack_Unit("파이어뱃",100,50)
# firebat1.attack("1시")
# firebat1.dameged(50)
# firebat1.dameged(50)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (3:59:29) 9-5.상속 
# (4:02:54) 9-6.다중상속 

#일반유닛 ()
# class Attack_Unit: 
#     def __init__(self, name, hp, damage):
#         self.name = name 
#         self.hp = hp
#         self.damage = damage
        
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{} : {}방향으로 날아갑니다.[속도{}]".format(name,location,self.flying_speed))

# #공중공격 유닛
# # 클래스 두개를 받아서 다중 상속 클래스 만든다
# class FlyableAttackUnit(Attack_Unit, Flyable): #상속받을 두클래스 쓴다
#     def __init__(self,name,hp,damage,flying_speed): #초기화할 값을 적어준다
#         Attack_Unit.__init__(self,name,hp,damage) #어택유닛에서 초기화값 받는다
#         Flyable.__init__(self,flying_speed) #플라잉 유닛에서 초기화값 받는다

# valkyrie = FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name,"3시")
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (4:10:08) 9-7.메소드 오버라이딩
# (4:17:03) 9-8.pass
# (4:19:31) 9-9.super
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (4:23:50) 9-10.스타크래프트 프로젝트 전반전
# (4:33:47) 9-11.스타크래프트 프로젝트 후반전

# #지상유닛
# class Unit:
#     def __init__(self,name,hp,speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{} 유닛이 생성되었습니다.".format(self.name))

#     def move(self, location):
#         print("지상유닛이동")
#         print(" {0} : {1} 방향으로 이동합니다. [ 속도 {2} ]".format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다".format(self.name))    
# #공격 유닛
# class AttackUnit(Unit):
#     def __init__(self,name,hp,speed,damage):
#         Unit.__init__(self,name,hp,speed)
#         self.damage = damage
    
#     def attack(self, location):
#         print("{} : {} 방향으로 적군을 공격합니다.[공격력 {}]".format(self.name,location,self.damage))

# #공중유닛
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{} : {}방향으로 날아갑니다.[속도{}]".format(name,location,self.flying_speed))

# class FlyableAttackUnit(AttackUnit,Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self,name,hp,0, damage)
#         Flyable.__init__(self, flying_speed)

# #마린 유닛
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)
    
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{} : 스팀팩을 사용합니다.(hp 10 감소)".format(self.name))
#         else:
#             print("{} : 체력이 부족하여스팀팩을 사용하지 않습니다".format(self.name))

# #탱크 유닛
# class Tank(AttackUnit):
#     seize_developed = False #시즈모드 개발여부

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return

#         if self.seize_mode == False:
#             print("{} : 시즈모드로 전환 합니다.".format(self.name))
#             self.damage*=2
#             self.seize_mode = True
#         else:
#             print("{} : 시즈모드로 해제 합니다.".format(self.name))
#             self.damage/=2
#             self.seize_mode = False   

# #레이스
# class wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스",80,20,5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True:
#             print("{} : 클로킹 모드 해제합니다. ".format(self.name))
#             self.clocked = False
#         else:
#             print("{} : 클로킹 모드 성정합니다. ".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다")

# def game_over():
#     print("Player : gg")
#     print("[player] 님이 게임에서 퇴장하셨습니다.")
#-------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------
# (4:50:13) 10-1.예외처리
#트라이부분을 실행하다 문제가 생길시 엑셉트 를 찾아 밸류에러에 해당하는 프린트물을 넣어 예외로 처리
# try:
#     print("나누기 전용 계산기")
#     nums= []
#     nums.append(int(input(">>>")))
#     nums.append(int(input(">>>")))
#     #nums.append(int(nums[0]/nums[1]))
#     print("{} / {} = {}".format(nums[0],nums[1],nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력했습니다")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("나머지 모든오류는 알수없는 에러가 발생")
#     print(err)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# (5:01:06) 10-3.사용자 정의 예외처리 finally
# class bignumberError(Exception):
#     pass

# try:
#     print("나누기 전용 계산기")
#     nums= []
#     nums.append(int(input(">>>")))
#     nums.append(int(input(">>>")))
#     nums.append(int(nums[0]/nums[1]))
#     if nums[0] >=10 or nums[2] >= 10:
#         raise bignumberError
#     print("{} / {} = {}".format(nums[0],nums[1],nums[2]))

# except bignumberError as err:
#     print("한자리 숫자만 입력해라")
#     print(err)
# finally:
#     print("오류가 나던 문제가 생기던 이문장은 꼭 출력된다")
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
