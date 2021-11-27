class vietnampackage:
    def detail(self):
        print("[베트남 패키지 3박 5일] 다낭 효도 여행 60만원 ")



if __name__ == "__main__":
    print("베트남 모듈을 직접실행-이문장은 모듈을 집접실행할때만 실행")
    trip_too = vietnampackage()
    trip_too.detail()
else:
    print("베트남 외부에서 모듈 호출")