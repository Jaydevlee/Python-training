#문자열 "" '' 관계없이 사용 가능
word = 'Python'
print(word)

str1 = "Python"
print(str1)

#python 문자열에서 p와 t만 출력
print(word[0], word[2])

#뒤 4자만 출력
car_number = '24가 3456'
#문자열 슬라이싱([startIndex : endIndex(출력범위에서 + 1) : stepIndex])
#startIndex 기본값(생략): 0
#endIndex 기본값(생략): 문자열 끝까지
#stepIndex 기본값(생략): 1
print(car_number[4:8:1])
print(car_number[4::1])
print(car_number[-4: ])
print(car_number[4:8:2])

string = "홀짝홀짝홀짝"
print(string[: : 2])

#replace: 문자열 대체
phone_number = "010-1234-5678"
phone = phone_number.replace("-", " ")
print(phone)

#문자열 합치기: 문자열 + 문자열
a = "3"
b = "4"
print(a+b)

#문자열 * 숫자: 문자열을 숫자만큼 반복
print("hi" * 3)

#출력 형식
#파이썬에서는 기본적으로 문자 + 숫자 허용하지 않음
name1 =  "홍길동"
age1 = 10

name2 = "이몽룡"
age2 = 12

#문자열과 숫자를 동시에 출력하는 방법
#1. str(int)
print("이름: " + name1 + " 나이: " + str(age1))
print("이름: " + name2 + " 나이: " + str(age2))

#2. formatting
print("이름 : %s 나이: %d" % (name1, age1))
print("이름 : %s 나이: %d" % (name2, age2))

# 문자열 나누기  split
s = 'hello world'
print(s)
r = s.split() #띄어 쓰기 기준으로 문자열 나누기
print(r)

data = '2026-01-05'
d = data.split("-") #하이픈을 기준으로 문자열 나누기
print(d)
