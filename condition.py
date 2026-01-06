# 조건문(if)
# score = 85
# if score >= 90: # 중괄호 대신 콜론(:) 사용
#     print("A학점")
# elif score >= 80:
#     print("B학점")
# else:
#     print("C학점")

# java
# if (score >= 90) { 
#     System.out.println("A학점");
# } else if (score >= 80) {
#     System.out.println("B학점");
# } else {
#     System.out.println("C학점");
# }

#반복문 for

# for 변수 in range(시작값, 종료값, 증감값)
# for i in range(0, 10, 1):  # 0~9까지 1씩 증가
#     print(i) 

# range(시작값, 종료값) 증감값 기본 1
# for i in range(0, 10):  # 0~9까지 1씩 증가
#     print(i)

# range(종료값) 시작값 기본 0, 증감값 기본 1
# for i in range(10):  # 0~9까지 1씩 증가
#     print(i)

# for 변수 in 객체 (리스트, 문자열, 튜플, 딕셔너리)
# for i in 'abc':
#     print(i)
# print("=============")
# for i in [10, 20, 30]:
#     print(i)
# print("=============")
# for i in [1, 2, 3]:
#      if i % 2 == 0:
#          print(i)

# numList = []
# for i in range(0, 6, 1): # 6번 반복
#    num=int(input("홀/짝 구분할 숫자입력:"))
#    if num % 2 == 0:
#     numList.append(num) #짝수만 리스트에 추가
#     print("입력한 숫자 중 짝수:", numList)

for i in range(0, 5, 1):
    num = int(input("숫자입력:"))
    if num % 2 == 1:
        print("홀")
    else:
        print("짝")