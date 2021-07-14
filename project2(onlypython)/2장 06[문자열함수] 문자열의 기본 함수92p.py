#문자열의 함수 "{}".format()
#문자열.함수(매개변수, 매개변수)
string_a = "{} {} {}" .format(10, "문자", True)
print(string_a)
print(type(string_a))

#특정 출력하기
data_1 = "{:d}".format(55) # {:d} 정수로만 출력
print(data_1)
data_2 = "{:5d}".format(55) # {:5d} 5칸뒤부터 채우며 출력
print(data_2)
data_3 = "{:05d}".format(55) # {:05d} 5칸뒤부터 채우고 앞은 0으로 채움
print(data_3)

#특정 출력하기
data_a = "{:f}".format(55.233) #{:f} 실수로만 출력
print(data_a)
data_b = "{:30f}".format(55.233) #{:5f} 5칸뒤부터 채우며 출력
print(data_b)
data_c = "{:025f}".format(55.233) # {:05f} 5칸뒤부터 채우고 앞은 0으로 채움
print(data_c)
data_d = "{:15.1f}".format(55.233) # {:15.1f} 15칸 뒤부터 채우며 첫째자리 까지 출력(자동으로 반올림 된다)
print(data_d)
data_f = "{:g}".format(55.000000) # {:g} 0을 제거한 후 출력
print(data_f)
