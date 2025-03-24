#숫자 두개를 입력받아서
# +, -, *, / 를 출력하는 프로그램을 만들어보자
A = int(input("첫 번째 숫자 입력: ")) 
B = int(input("두 번째 숫자 입력: "))

print(f"{A} + {B} = {A + B}")  # 숫자와 연산자를 함께 출력
print(f"{A} * {B} = {A * B}")
print(f"{A} - {B} = {A - B}")

if B != 0:  # 0으로 나누는 오류 방지
    print(f"{A} / {B} = {A / B}")
else:
    print("0으로 나눌 수 없습니다.")
    