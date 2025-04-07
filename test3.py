while True:
    A = int(input("입력값: "))

    if A == 0:
        print("프로그램을 종료합니다.")
        break
    if A == 1:
        dog = r"""
          / \__
         (    @\___
         /         O
        /   (_____/
       /_____/
        """
        for _ in range(5):
            print(dog)

    elif A == 2:
        cat = r"""
         /\_/\
        ( o.o )  
         > ^ <
        """
        for _ in range(5):
            print(cat)

    elif A == 3:
        rabbit = r"""
        (\_/)
        ( •_•)
        / >🍎
        """
        for _ in range(5):
            print(rabbit)

    else:
        print("1, 2, 3 중 하나를 입력하거나 0으로 종료하시오.")