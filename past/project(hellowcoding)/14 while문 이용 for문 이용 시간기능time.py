# 리스트의 remove()는 중복리스트중 하나를 제거한다 
# 이를 while반복문으로 해결가능하다
Arrang = [1,2,1,2,1,2]
Del = 2
i = 0
while Del in Arrang: #리스트안에 변수 2가 있을때까지
    Arrang.remove(Del) #arrang에서 del을 제거
    print("{}번째중복제거입니다".format(i),Arrang)
    i+=1
else:
    print("모두 제거 되었습니다")

#시간을 기반으로 반복하기
import time #유닉스타임-1970년 1월1일0시0분0초로부터 몇초가 지났는지 정수로 나타낸다

i = 0
target_time = time.time()+5 #time.time() 유닉스타임을 구한다
while time.time() < target_time:
    i+=1
print("{}번 시도했음".format(i))


