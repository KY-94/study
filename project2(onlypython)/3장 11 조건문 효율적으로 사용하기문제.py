score = input("학점입력: ")
score = float(score)

if score == 4.5:
    print("신")
elif 4.2 <= score < 4.5:
    print("교수님의 사랑") 
elif 3.5 <= score < 4.2:
    print("현체제의 수호자") 
elif 2.8 <= score < 3.5:
    print("일반인") 
else:
    print("일탈을 꿈꾸는 시민")         