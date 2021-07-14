#break() - 반복문을 벗어날때
i=0
while True:
    print("{}번쨰 반복입니다.".format(i))
    i+=1
    input_txt = input("종료할까요?")
    if input_txt in ["y","Y"]:
        print("종료합니다")
        break
    else :
        print("계속시도합니다")


#contiune() - 현재 반복을 생략하고 다음반복으로 넘어간다
number = [5,15,6,20,7,25]
for j in number:
    if j<10:
        continue
    print(j)
        
#문자열.join(문자로구성된 리스트) - 리스트의 요소들을문자열로 연결한다
print("::".join(["1","2","3","4","5"]))

#textwarp 모듈 dedent함수 = 전체 들여쓰기 제거
import textwrap
if True:
    test='''\
    긴 문자열을
    만듭니다
    여러줄로'''
print("원본:",test)
print("모듈:",textwrap.dedent(test))