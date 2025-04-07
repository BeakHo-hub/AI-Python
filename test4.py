def hello():
    print("hello world")
#함수 호출 실행
hello()

def hello_name(name):
    print(f"안녕 {name}야")

name = input("이름을 입력:")
hello_name(name)

def cal(n1, n2, op):
    r=0
    if op =="+": #1, 2, 
       r= n1+n2
    elif op =="-":
       r+ n1 - m2
    else:  
        print("잘못입력")
    return r
r= cal(2, 1, "+")
print(f"두 수를 더한 값(r)")
cal(2, 1, "+")
print(f"두 수를 뺀 값(r)")
cal(2, 1, "-")