# source : https://level.goorm.io/exam/43255/%EC%95%BD%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

user_input = int(input())

ret = []

for num in range(1, user_input + 1):

    if user_input % num == 0:
        ret.append(str(num))

print(" ".join(ret) + " ")

