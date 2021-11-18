#리스트가 숫자를 기반으로 값을 저장하는것
#딕셔너리는 문자를 기반으로 값을 저장하는것-문자열을키,값을 값이라고

#{
#    키:값,
#    키:값,
#}

jangbogi = {
    "장볼것":"망고",
    "가격":"5000원",
    "원산지":"필리핀"
}
print(jangbogi)
print(jangbogi["장볼것"]) #인덱싱으로 출력 가능
jangbogi["장볼것"] = "당신? 휴먼입니까?"#인덱싱으로 내용 변경
print(jangbogi)

#딕셔너리에 새로운 요소 추가하기
# 변수[키]=새로운값
hong = {} #비어있는 딕셔너리
hong["이름"]="파이썬"
hong["가능성"]="높음"
print(hong)

#딕셔너리에 요소 제거하기
# del 변수[키]
del hong["이름"]
print(hong)

#딕셔너리에 키있는지 확인
# 키 in 변수
print("가능성" in hong)


# for 키변수 in 변수:
#   코드
delpi = {
    "이름":"몰라",
    "이건":"왜쓰지?"
}
print(delpi)

#delpi에 키변수인new를 넣는다
#delpi의 키인 "이름"이 출력된다
#delpi[키변수]의 값인 "몰라"가 출력된다
for new in delpi:
    print(new,delpi[new])

