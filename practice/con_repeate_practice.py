# Q1
list1 = [3, -20, -3, 44]
for i in list1:
    if i < 0:
        print(i)

# Q2
list2 = [3, 100, 23, 44]
for i in list2:
    if i % 3 == 0:
        print(i)

# Q3
list3 = [13, 21, 12, 14, 30, 18]
for i in list3:
    if i % 3 == 0 and i < 20:
        print(i)

# Q4
list4 = ['I', 'study', 'python', 'language', '!']
for i in list4:
    if len(i) >= 3:
        print(i)

# Q5
list5 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in list5:
    str = i.split(".")
    print(str[0])

# 06
for i in range(1, 6):
    phone = input("휴대전화 번호 입력:")
    phone1 = phone.split("-") #phone1 = phone.split("-")[0]
    if phone1[0] == "011":
        print("SKT")
    elif(phone1[0] == "016"):
        print("KT")
    elif(phone1[0] == "019"):
        print("LGU")
    elif(phone1[0] == "010"):
        print("알 수 없음")

#07
for i in range (1,6):
    post = input("우편번호(-)제외:")[0 : 3]
    if post in ["010", "011", "012"]:
        print("강북구")
    elif post in ["013", "014", "015"]:
        print("도봉구")
    else:
        print("노원구")