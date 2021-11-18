arrange = [111,123,333,555,1423]

#정반복문
print()
for i in range(len(arrange)):
    print(str(i)+"번쨰:",arrange[i])

print()
for i in range(len(arrange)):
    print("{}번쨰: {}".format(i,arrange[i]))
print()


#역반복문(reversed)
for i in reversed(range(len(arrange))):
    print("{}번쨰: {}".format(i,arrange[i]))




#while 반복문
#for반복문- 특정 정해진 횟수만큼 반복한다
#while반복문 - 무한정 반복한다

#while 불표현식:   
#   문장
#불표현식이 참이라면 문장을 계속 반복한다.
#ctrl + C는 강제 종료

#while True:
#    print(".",end='2') #엔드는 글자끝에 무엇인가 붙일지?

print()
j = 0
while j<30:
    print("{}번쨰입니다".format(j))
    j+=2
print()
