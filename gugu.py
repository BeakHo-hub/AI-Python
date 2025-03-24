def gugudan(n):
    if n < 2 or n > 9:
        print("2부터 9까지의 숫자를 입력해라!")
        return
    
    print(f"=== {n}단 ===")
    for i in range(1, 10):
        print(f"{n} x {i} = {n * i}")

num = int(input("출력할 구구단의 숫자를 입력하라: "))
gugudan(num)
