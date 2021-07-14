#range는 list를 이용해 범위를 확인할수있다
print(list(range(5))) # 5미만까지
print(list(range(1,5))) # 1이상 5미만
print(list(range(0,10,2))) #0이상 10미만 2차이만큼

#range와 for문을 결합시키면 원하는 동안 반복시킬수있다
# for 범위내부의숫자를담을변수 in 범위:
#   코드

for i in range(1,5): #반복의경우 ijkm으로 표현한다
    print(i,"번쨰반복입니다")

for i in range(10):
    print(str(i)+"번쨰반복입니다")