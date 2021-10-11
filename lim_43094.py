# source : https://level.goorm.io/exam/43094/%EC%8B%9C%ED%97%98%EC%84%B1%EC%A0%81-%ED%8F%89%EA%B7%A0%EA%B3%BC-%EB%93%B1%EA%B8%89-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

user_input = list(map(int, input().split(" ")))

avg = sum(user_input) / 3
grade = "A" if avg >= 90 else "B" if avg >= 80 else "C" if avg >= 70 else "D" if avg >= 60 else "F"

print('%.2f'%(avg), grade) # 소수점 두번째까지 무조건 출력