#인치단위를 cm 단위로
inch = float(input("몇인치인가요? 숫자로 입력해주세요 "))
print(inch," 인치 입력받았습니다")
cm = inch*2.54
print(inch,"인치는")
print(cm,"cm입니다")

#킬로그램을 파운드로
kg = float(input("몇kg인가요? 숫자로 입력해주세요 "))
print(kg," 인치 입력받았습니다")
lb = kg*2.20462262
print(kg,"kg은")
print(lb,"lb입니다")

#원의 반지름 입력받아 원의 둘레와 넓이
circle =float(input("원의 반지름을 입력해주세요"))
print(circle,"입력받았습니다")
pi = 3.141592
doole = 2*pi*circle
wide = pi*circle**2
print("원의 둘레는 {} 입니다.".format(doole))
print("원의 넓이는 {} 입니다.".format(wide))

