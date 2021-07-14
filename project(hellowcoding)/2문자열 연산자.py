# 문자열 연산자로는 +, * 가능

# 문자열 선택: 문자열[숫자] - 이는 인덱스라고 부름 
# []안의 숫자를 음수로 하면 뒤부터 선택 가능
print("파이썬"[0])
print("파이썬"[1])
print("파이썬"[2])

# 문자열 선택 ~부터 ~까지: 문자열[숫자1:숫자2] -숫자1이상 숫자2미만 
print("파이썬"[0:2])
print("파이썬파이"[0:])
print("파이썬파이"[:3])

#문자열의 길이: len(문자열 or 리스트)
print(len("파이썬"))

#문자열에 복합연산자 사용 가능
pyton = "안녕하세요"
pyton +="!" # +=는 문자열 문자열 가능
pyton *=2   # *=s는 문자열 숫자열 가능
print(pyton)
