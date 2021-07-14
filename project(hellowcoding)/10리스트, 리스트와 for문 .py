# 리스트는 [ , ]로 생성함
#list()로 생성가능함
# 리스트 내부는 자료형,숫자형,불 등 다양하게 넣을수 있음
arrang = [1,"숫자",True]

#리스트출력 - 변수[]  ㅡ>"인덱싱"
print(arrang[0])
print(arrang[-1])
print(arrang[0:2])
#리스트내용[]번째 변경 - 변수[]=새로운자료형
arrang[0] = "새로운"
print(arrang[0])
#최종리스트는 변경된값이 저장된형태로 형성된다.
print(arrang)

#리스트 연산자 +와 *사용가능
list_a = [0,1,2,3,4]
list_b = [3,4,5]
# + 의 사용
listtotal = list_a+list_b
print(listtotal)
# * 의 사용
listduble = list_a*3
print(listduble)

#리스트에 요소추가하기
# .append(추가) 리스트뒤에 추가한다
# .insert(위치,추가) 리스트 위치에 추가 한다
# .extend([추가,추가,추가]) 리스트에 여러 값을 추가한다
list_c = [0,1,2]
list_c.append("추가")
list_c.insert(1,"추가")
list_c.extend(["가","나"])
print(list_c)


#리스트에 요소제거하기
#인덱싱제거 ex) del 변수[인덱싱] , del 변수[~:~]  
#              변수.pop(제거위치)
list_A = [0,1,2]
del list_A[1]
print(list_A)
list_B = [0,3,4]
list_B.pop(1) #.pop()은 리스트의 마지막 값을 제거
print(list_B)
# 리스트내 특정 처음 발견값 제거 ex) 변수.remove(값) 
list_C = [1,1,1]
list_C.remove(1)
print(list_C)
# 리스트 모두 제거하기 ex) 변수.clear()
list_C.clear()
print(list_C)


#리스트내 특정값 찾기
# 값 in 리스트 - 특정값이 있는지 True,False로 나타남
# 값 not in 리스트 -특정값이 없는지 True,False로 나타남



#for 반복자 in 반복할수있는것:
#   코드(들여쓰기해야함)

#리스트와 for
# for 요소를 담을변수 in 리스트
arrge = [1,2,3,4,5]
for elimental in arrge: #arrge의 리스트값을 elimental에 넣는다
    print(elimental) #elimental을 정의하지 않음에도 형성됨

#for문은 문자열과도 사용가능
for list_a in "안녕파이썬?":
    print(list_a)
