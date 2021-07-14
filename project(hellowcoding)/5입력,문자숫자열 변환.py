# 사용자에게 키보드,마우스등 받을떄
# 변수 = input("문자열") 
python_1 = input("그래 안그래? " )
print(python_1)

# 입력받은것은 무조건 문자열로 됨 
# 이것을 다시 정수나 실수로 변환 하고자 할떄
# 변수 = int(input("숫자"))
# 변수 = float(input("숫자")) -> 플롯이 대부분 유리한듯?
output_a = int(input("정수만 가능- 다른것은 오류남 "))
output_b = float(input("정수,실수 가능- 다른것은 오류남"))
print(type(output_a), output_a)
print(type(output_b), output_b)

#숫자를 문자열로도 바꿀수 있다 - 오려우니까 포기한다 쉬불
# 변수 = "{}".format()
outcome = "{} {} {}".format(1.0, "문자", 2)
print(outcome)