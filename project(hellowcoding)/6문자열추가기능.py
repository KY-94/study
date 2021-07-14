#"문자열". 뒤에 마침표찍으면 문자열 추가기능 나온다 찾아쓴다


# .upper() -대문자로 바꾸기
# .lower() -소문자로 바꾸기
# 절대 원본은 바뀌지 않는다 따라서 변수에 넣어서 처리해야하는게 좋음
string2 = "HAaPbPcY"
string2.lower()
string2_a = string2.lower()
print(string2_a) # 변경된함수에 저장되어 나옴
print(string2) # 원본으로 나온다


#문자열 양옆 공백제거
# .strip()
SSSS = '''
        파
    이
써언
'''
print(SSSS)
print(SSSS.strip()) #-? 맨앞 한줄만 공백제거됨?


#문자열 찾기
#.find() -왼쪽부터
#.rfind() - 오른쪽부터


#문자열 안에 있나 확인?
#A in B  B에 A가 있는지 참거짓 판단
print("파이" in "파이썬") 


#문자열자르기
#.split(자를문자) - 문자를 자를문자로 자른다
dug = " 안 녕 하 세 요 ".split()
print(dug) # 실행결과로 리스트로 생성됨 ex['안', '녕', '하', '세', '요']
