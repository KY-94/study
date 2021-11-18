#리스트로 변환하기
#list()
A = "문자열"
B = {"키1":"값","키2":"값2"}
C = range(10)

print("A",list(A)) #문자열 한글자 한글자가 리스트의 요소로
print("B",list(B)) #딕셔너리 키값이 리시트의요소로
print("c",list(C)) # 범위정수가 리스트의요소로

#리스트의 요소 뒤집기 - reversed()

#enumerate() - 숫자를 카운트해주며 출력해준다
example_A =["요소A","요소B","요소C"]

print()
print("단순출력")
print(example_A)
print()

print("enumerate()출력")
print(enumerate(example_A))
print()

print("리스트 강제 변환 출력")
print(list(enumerate(example_A))) # 이것을 튜플이라고 부른다.
print()

for i,k in enumerate(example_A): # 반복문에 변수를 여러개 넣을 수있음
    print("{}번쨰 요소는 {}입니다".format(i,k))


#딕셔너리 .items()함수 - 키와 값을 조합해 반복문을 작성가능
example_b = {
    "키A":"값A",
    "키B":"값B",
    "키C":"값C"}
print("그냥출력: ",example_b)
print("items()함수사용: ",example_b.items())
print()

for m,j in example_b.items():
    print("{} = {}".format(m,j))


#반복문에서 리스트의 재조합
#ex> 0~20 사이의 짝수를 구해 제곱한뒤 새로운 리스트만들기
arrang = []
for h in range(0,20,2):
    arrang.append(h*h)
print(arrang)  

arrang_b = [h*h for h in range(0,20,2)]
print(arrang_b)



