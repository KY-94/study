#개미수열
# 1
# 11
# 12
# 1121
# 12211

result = ["1"]

#10번째까지 반복시키기
for i in range(10):
    print("".join(result))

    next = []          #다음단계 수열을 구해 넣을 리스트
    number = result[0] #현재숫자
    count = 0          # 현재숫자 출현 개수
    
    #숫자 확인 개수를 계산
    for item in result:
        if number == item:
            count += 1
        else:
            next.append(number)
        next.append(str(count))
        number = item
        count = 1
    next.append(number)
    next.append(str(count))
    result = next
print()
print("10번쨰:","".join(result))    
