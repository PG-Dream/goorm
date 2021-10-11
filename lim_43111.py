# source : https://level.goorm.io/exam/43111/%ED%99%80%EC%A7%9D-%ED%8C%90%EB%B3%84/quiz/1

user_input = int(input())

ret = "odd" if user_input % 2 != 0 else "even"  # 홀수 , 짝수 구별 로직
print(ret)