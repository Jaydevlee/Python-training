# Q1
scores = [80, 90, 100]
def print_score (scores):
    return  sum(scores) / len(scores)
result = print_score(scores)
print (result)

# Q2
nums = [1, 3, 2, 10, 12, 11, 15]
def print_even(a):
    num_even=[]
    for i in range(0, len(a)): 
        if a[i] % 2 == 0:
            num_even.append(a[i])
    return num_even #return이 for안에 존재하면 안 됨, 내어쓰기로 for밖으로 빼내기
print(print_even(nums))

#for i in a:
#   if i % 2 == 0:
#       num_even.append(i)

#Q3
def make_url(str):
    url = "www." + str + ".com"
    return url
result = make_url("naver")
print(result)

#Q4
#문자열 + 숫자는 Python에서 허용되지 않음
def func (a,b):
    print(a * 3)
func("안녕", 3)

#Q5
num1 = int(input("숫자 입력"))
num2 = int(input("숫자 입력"))
opt = input("산술연산자 중 하나 입력")

def print_arithmetic_operation(a, b, c):
    if b == '+':
        return a + c
    elif b == '-':
        return a - c
    elif b == '*':
        return a * c
    elif b == '/':
        return a / c
print(print_arithmetic_operation(num1, opt, num2))

#Q6
def gugudan(n):
    list_gugudan = []
    for i in range(1, 10, 1):
        list_gugudan.append(n * i)
    return list_gugudan
print(gugudan(3))
