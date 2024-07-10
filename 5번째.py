# x = 6
# if 5 < x < 10:
#     print(x)
# else :
#     print("no")

# 1. 사용자로부터 값을 입력
# 2. 사용자로부터 입력받은 값을 숫자형으로 데이터 타입을 변환
# 3. 변환된 값을 각 조건에 따라 학점으로 출력

ans = input("점수를 입력하시오 : ")
x = int(ans)
if 81 < x < 100 :
    print("A")
elif 61 < x <80 :
    print("B")
elif 41 < x < 60:
    print("C")
elif 21 < x < 40:
    print("D")
elif 0 < x < 20:
    print("E")
