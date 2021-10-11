# source : https://level.goorm.io/exam/49095/%EA%B3%A0%EC%9E%A5%EB%82%9C-%EC%BB%B4%ED%93%A8%ED%84%B0/quiz/1

N, c = map(int, input().split(" "))
input_times = list(map(int, input().split(" ")))

type_cnt = 0
time_prev = 0

for time in input_times:

    if time - time_prev > c:
        type_cnt = 1
    else:
        type_cnt += 1

    time_prev = time

print(type_cnt)

