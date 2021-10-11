# source : https://level.goorm.io/exam/43166/3%EA%B3%BC-5%EC%9D%98-%EB%B0%B0%EC%88%98/quiz/1

user_input = int(input())

ret = 0
for num in range(1, user_input + 1):

    if num % 3 == 0 or num % 5 == 0:
        ret += num

print(ret)
