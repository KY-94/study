#021
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# >> letters = 'python'
letters = 'python'
print(letters[0],letters[2])
#022
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# >> license_plate = "24가 2210"
# 실행 예: 2210
license_plate = "24가 2210"
print(license_plate[4:])#앞부터는0부터시작
print(license_plate[-4:])#뒤부터는1부터시작
#023
# 아래의 문자열에서 '홀' 만 출력하세요.
# >> string = "홀짝홀짝홀짝"
# 실행 예: 홀홀홀
string = "홀짝홀짝홀짝"
print(string[0] * string.count("홀"))
print(string[::1])
