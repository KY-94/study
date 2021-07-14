#if <조건>:
#    조건이 참일 떄 실행할 문장
#    조건이 참일 떄 실행할 문장
#    조건이 참일 떄 실행할 문장
#    조건이 참일 떄 실행할 문장

#       if True:
#           print("Ture입니다") 
#       if False:
#           print("Flase입니다") 
#       
import datetime # 날짜 모듈(날짜/시간 관련된 기능을 가져온다)
now = datetime.datetime.now() # 현재 시간 구해 now에 선언
print("{}년입니다.".format(now.year))

#else 조건문
# if 조건:
#     참일 때 나타낼 명령
# else:
#     거짓일 때 나타낼 명령       
# 
# #elif 조건문
# if 조건A:
#     A가 참일떄 나타낼 명령
# elif 조건B:
#     B가 참일떄 나타낼 명령
# else:
#     모두 거짓 일때 나타낼 명령   
