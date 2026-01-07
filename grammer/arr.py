# list - 자바의 배열과 동일, 요소의 값 추가, 수정 가능
arr1 = ["닥터스트레인지", "스플릿", "기생충"]
print(arr1)
print(arr1[1])
arr1.append("배트맨")
arr1[3] = "배트맨3"
print(arr1)
#  기생충 삭제
del arr1[2]
print(arr1)

# tuple - 자바의 배열과 유사, 요소의 값 추가, 수정 불가능
arr2 = ("닥터스트레인지", "스플릿", "기생충")
print(arr2)
print(arr2[1])
# arr2[3] = "배트맨3"
# print(arr2)
# del arr2[2]
# print(arr2)

# 리스트 합계, 평균, 최대값, 최소값
score = [65, 73, 84, 98, 70]
print(sum(score))
print(max(score))
print(min(score))
print(sum(score) / len(score))