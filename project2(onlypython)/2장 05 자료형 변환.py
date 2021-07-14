#---------------------------------------------
#사용자 입력을 input() 함수 - 어떤값을 넣어도 "문자열"로 타입이 정해진다
a = input(">>> ")
print(a)
print(type(a))

# 문자열을 숫자로, 숫자를 문자열로 변환
a = int(input("첫숫자 "))
b = int(input("둘숫자 "))
print(a+b)
print(type(a),type(b),type(a+b))

a = float(input("첫숫자 "))
b = float(input("둘숫자 "))
print(a+b)
print(type(a),type(b),type(a+b))

a = str(input("첫숫자 "))
b = str(input("둘숫자 "))
print(a+b)
print(type(a),type(b),type(a+b))
# 파이썬의 경우 문자,숫자연자가 불가능함으로 자료형을 한가지로 통일 해주어야 한다