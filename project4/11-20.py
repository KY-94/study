#011 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
samsung = 50000
total_samsung_price = samsung * 10
print(total_samsung_price)
#012 
#다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
# 항목  	값
# 시가총액	298조
# 현재가	50,000원
# PER	    15.79
samsung_stack_total_price = 298000000000000
samsung_stack_price_now = 50000
samsung_PER = 15.79
print("시가총액", samsung_stack_total_price)
print("현재가", samsung_stack_price_now)
print("PER", samsung_PER)
#016 
# 문자열 '720'를 정수형으로 변환해보세요.
# >> num_str = "720"
num_str = "720"
num_int = int(num_str)
print(num_int, type(num_int))
#018
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
num_str2 = "15.79"
num_float = float(num_str2)
print(num_float, type(num_float))
#019
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
# year = "2020"
year = "2020"
year = int(year)
print("작년:", year-1)
print("올해:", year)
print("내년:", year+1)
#020
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
air_compressure_price_month = 48584
air_compressure_price_paymonth = 36
air_compressure_price_total = air_compressure_price_paymonth * air_compressure_price_month
print(air_compressure_price_total) 