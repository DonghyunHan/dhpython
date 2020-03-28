#출력
#print(1)

# 값을 저장
#a = 1
#print(a)

#변수로 사용할 수 없는 것들
#1. 이미 다른 것으로 알고 있는 것
#and
#True
#False
#for
#while
#if
#....

#2. 처음에 숫자가 오면 안 됨 (처음에 숫자가 오면 숫자로 인식)
#a1, abc1 등은 가능
#1a, 1abc 는 불가능

#3. 띄어쓰기가 중간에 못 옴
#a b 와 같은 것들은 안 됨

#4. 특수문자가 오면 안 됨 (언더바, 언더스코어는 가능)
#a_b, b_c 와 같이 언더바를 활용가능 다른 특수문자는 안 됨

#TIP
#파이썬은 대소문자를 구별할 수 있음
#True 와 true를 구분
#즉, true는 변수로 활용 가능
#잘 안 쓰지만 한글로도 변수 활용 가능

#input() 컴퓨터에 값을 입력하는 것
#print()와 정반대

#a = input()
#print(a)

#type() 은 변수를 어떤 걸로 알고 있는지를 물어봄

#a = 1
#print(type(a))

#int() 는 컴퓨터가 숫자 형식의 값을 순자값으로 변환해줌

#a = '123'
#b = int(a)
#print(type(a))




#3.28 문제1

#people = input("참석자의 수를 임력하시오: ")
#p = int(people)
#c = p
#b = p * 2
#ca = p * 4
#print()
#print("치킨의 수: ", c)
#print("맥주의 수: ", b)
#print("케익의 수: ", ca)

#print 심화 과정
#print() 안에 , 를 적으면 변수값 사이에 띄어쓰기 됨
#sep = '(값)' 을 쓰면 듸어쓰기를 다른 값으로 변경
#end = '(값)' 을 쓰면 줄바꿈을 다른 값으로 변




#3.28 문제2

m = 0
e = input("에스프레소 판매량: ")
e = int(e) * 2500
a = input("아메리카노 판매량: ")
a = int(a) * 2500
cl = input("카페라떼 판매량: ")
cl = int(cl) * 3000
cc = input("카푸치노 판매량: ")
cc = int(cc) * 3000
b = input("비엔나커피 판매량: ")
b = int(b) * 4000
h = input("핸드드립커피 판매량: ")
h = int (h) * 6000
m = e + a + cl + cc + b + h
print("오늘 총 매출은", m, "원 입니다.")
