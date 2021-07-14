#005 \n는 엔터기능  \t는 탭기능
print("안녕하세요.\n만나서\t\t반갑습니다.")
#006 ,로 구분을 하면 한칸띄워준후 다음값 출력
print ("오늘은", "일요일")
#007 sep=";"는 출력되는 값들 사이에 공백대신 ";"이 출력됨
print("naver;kakao;sk;samsung")
print("naver", "kakao", "sk", "samsung", sep="") #공백이없다
print("naver", "kakao", "sk", "samsung", sep=";")#공백대신 ;있다
#008 7과 비슷한문제
print("naver/kakao/sk/samsung")
print("naver", "kakao", "sk", "samsung", sep="/")
#009 ;는 한줄에 여러개의 명령을 작성하는데사용됨 
#print의 특성상 출력되고 나서는 엔터가 입력되는데 end=""를 넣음으로 출력마지막에 빈공백생성
print("first", end=""); print("second")
#010
print(5/3)
