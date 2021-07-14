#비교연산자를 통해 불을 확할수 있다
#불은 true  와 False 값만 가진다
#수학에서 > < == >= <= != , 문자열에서 > < == != 사용
print("가방"<"집")
print("가방">"집")
print("여행"<"취직")#????


# and는 모두참일때만
# or은 둘중 하나만 참일때


# if 조건:
#   조건이 참일때 출력될 문장
number01 = input("A> ")
number02 = input("B> ")

if number01 == number02:
    print("같아")
if number01 < number02:
    print("B가 더 커")
if number01 > number02:
    print("A가 더 커")


#파이썬의 날짜/시간관련 기능 impor datetime 임
import datetime
now = datetime.datetime.now() #현재의 날짜/시간을 구한다

print()
print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print()

if now.hour < 12:
    print(now.hour,"지금은 오전{}시입니다.".format(now.hour)) #폴매이팅을 사용해 출력 -> 연습문제에도 사용가능할듯
if now.hour > 12:
    print(now.hour,"지금은 오후{}시입니다.".format(now.hour)) #폴매이팅을 사용해 출력 -> 연습문제에도 사용가능할듯



# 짝수 홀수 구분하기 ver.1 - if와 else

Num_a = input("숫자입력> ")#입력받기
Num_end = Num_a[-1] #끝자리 인덱싱

if float(Num_end) == 0\
    or float(Num_end) == 2\
    or float(Num_end) == 4\
    or float(Num_end) == 6\
    or float(Num_end) == 8:
    print("짝수입니다")
else:
    print("홀수입니다")

#pass 키워드는 큰그림그릴때 미구현으로 넘어가는 코드이다