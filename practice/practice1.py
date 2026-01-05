#Q1
name = "김하늘"
birth_year = 2003
currnet_year = 2025

print("이름 : %s 나이 : %d" % (name, birth_year))

#Q2
id_number="9990101-1234567"

print(id_number[:5:])
print(id_number[-7: ])
print(id_number.replace("-", ""))

#Q3
filename = "report_final_v2.pdf"
#확장자만 출력
print("확장자만 출력" + filename[-3: ])
print("파일이름만 출력" + filename[ :15])

#Q4

text = "abcabcabc"
print(text[: : 3])

#Q5
phone = "01011115222"

ph1 = phone[ : 3]
ph2 = phone[3 : 7]
ph3 = phone[8 : 11]

print(ph1 + "-" + ph2 + "-" + ph3) 

#Q6
a ="5"
b = 3
print(a * b)

#Q7
count = 7
print("총 개수 :  %d 개" % count)

#Q8
car_number = "12가3456"

print(len(car_number))
print(car_number[3 : 8])

#Q9
star = "★"
print(star * 10)

#Q10
name = '이준호'
score = 87

#Q11
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

#Q12
t1 = 'python'
t2 = 'java'
print((t1+t2) * 4)

#Q13
branch =  "2020/03(E) (IFRS연결)"
print(branch[ : 7])
