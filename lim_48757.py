# source : https://level.goorm.io/exam/48757/369-%EA%B2%8C%EC%9E%84/quiz/1

user_input = int(input())

ret = 0
for num in range(1, user_input): # 입력 N - 1까지만 확인

    for check in ["3", "6", "9"]:
        ret += str(num).count(check)

print(ret)

