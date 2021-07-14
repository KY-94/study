#사용자의 태어난 년도 띠출력
berthday = input("태어난 년도0000> ")
berthday = int(berthday)
berthday_end = berthday % 12
if berthday_end == 0:
    print("원숭이")
elif berthday_end == 1:
    print("닭")
elif berthday_end == 2:
    print("개")    
elif berthday_end == 3:
    print("돼지")
elif berthday_end == 4:
    print("쥐")
elif berthday_end == 5:
    print("소")
elif berthday_end == 6:
    print("범")
elif berthday_end == 7:
    print("토끼")
elif berthday_end == 8:
    print("용")
elif berthday_end == 9:
    print("뱀")
elif berthday_end == 10:
    print("말")
else:
    print("양")