# 아스키 코드 그림 출력하기

# 만약에 1을 입력하면 1번 캐릭터 출력
# 만약에 2를 입력하면 2번 캐릭터 출력
# 3을 입력하면 3번 캐릭터 푸렭
# 잘못 입력하면 잘못 입력했다고 출력
print("그림 출력 프로그램")
print("================")
print("1")
print("2")
print("3")
print("4")
print("0을 입력하면 종료")
print("================")
while True:
    A = input("원하는 그림 번호 입력 (0 입력 시 종료): ")
    if A == '0':
        print("프로그램을 종료합니다.")
        break
    if A == '1':
        midoriya = r"""
    ⣏⡹⣬⣍⣣⣭⣙⣬⣍⢧⣻⣟⣿⡿⣿⢿⣿⢿⡿⣿⢿⡿⣿⢿⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⢢⠑⡦⣌⠱⣌⡙⡚⡔⢪⢿⣾⣽⡿⣽⣻⣿⣿⣿⣽⣯⣿⡽⣯⢿⣽⣻⣽⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠶⣩⠛⡜⣛⠲⠳⡱⢎⡓⢾⣯⢿⣽⢿⣳⢿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⡑⢆⡛⡔⢣⣋⡷⣵⣾⣞⡿⣽⣻⢯⡿⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣛⣞⠲⣙⢓⠻⣙⢛⢳⣯⣟⡷⣯⢿⣽⣳⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⢖⠻⣿⣶⢯⡶⣼⢾⣯⢿⣽⣻⣽⣻⢾⣽⣻⢾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⢮⠓⡞⢯⡿⣽⢯⣟⡾⣿⣾⣷⣯⣟⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠦⡹⠜⠦⡛⠿⣻⣾⣽⣷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⡷⣧⢟⡶⡽⣶⣣⣿⡽⣞⣷⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣙⢬⡩⣜⣡⢣⣿⣳⣟⡿⣾⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⡹⣿⣿⣿⣿⣿⣧⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣍⢦⣑⣆⣦⣿⣟⣷⢯⣟⣷⣻⡽⣯⣟⣿⣿⣿⣿⣿⢏⠖⡀⢿⣿⣿⣿⣿⢏⠏⢹⣿⢏⢻⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣬⣦⣭⣜⣤⣧⣞⣯⢿⣞⣷⣯⣿⣿⣿⣿⣿⣿⣿⣿⠮⠐⡀⣿⢿⣿⡿⠏⡈⣰⡼⠷⠾⠶⣽⣟⠹⢊⠙⢻⣿⣿⣿⣿⣿⡿⠟
    ⢣⣍⣛⢯⣿⣾⡽⣞⣯⣿⣾⣿⣿⣿⣿⣿⣿⣿⡿⣿⠓⡄⠰⠋⢼⠋⡔⢠⡾⠑⠈⢡⣥⣉⠐⠙⢦⠀⠌⡀⣿⠟⣿⣿⠏⣐⢶
    ⠱⡌⡍⢎⠴⣉⠭⣩⢹⣿⣿⢿⣿⣿⣿⣿⣿⣿⣷⢬⡟⠳⣆⠁⢂⠐⠠⠘⠅⠀⠂⢸⣿⣋⠀⠄⠘⡆⠐⠠⠁⢌⡿⢋⠰⣏⢷
    ⡓⢬⡙⡬⣙⢌⡣⣅⢻⡷⡼⢯⣿⣿⣿⣿⣿⣿⣿⢿⠄⠐⣿⡇⠠⠈⠄⡁⢂⠀⠐⠀⠹⠋⢀⠠⢘⠄⡁⢂⠁⢂⠐⠠⡶⣩⠶
    ⠟⣣⢙⡱⣉⢎⡱⣉⠻⢏⢿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢆⠀⠘⠷⢀⠁⢂⠐⡀⠂⠤⣈⡀⣄⠢⠔⡁⢂⠐⠠⠈⠄⡈⠐⠳⢉⣴
    ⡘⢤⢋⠴⣉⢎⡱⢩⡙⣼⡾⣿⢯⣻⣿⣿⣿⢿⣿⣿⣏⠦⡄⢔⡄⠈⠄⠂⠄⡁⠂⠄⡐⠠⢁⠂⠔⢠⠁⢂⠁⠂⡄⠙⣶⠿⣽
    ⡙⣍⢚⡹⡘⢎⡱⢋⡝⣡⢛⣧⢿⣻⢿⣹⢯⡾⣽⣻⣞⡇⠰⠈⠄⠡⢈⠐⠠⢀⠁⠂⠄⡁⠂⠌⡐⠠⠈⠄⡈⡴⢈⠐⣯⣟⣳
    ⢒⡚⣒⠓⡍⣆⢓⡋⢖⡡⢾⣹⢯⣳⢯⣛⡾⣵⡻⢶⣻⡄⠡⠈⠄⣁⣂⠬⠴⠂⠚⢊⣉⡭⢟⠂⠄⠡⢈⢰⡜⢁⣂⣼⣷⣿⣿
    ⢃⡛⡜⢛⡜⡙⢎⡙⢎⡙⢯⣏⡷⢯⣻⣭⢟⡾⡽⣏⣷⢻⣆⣁⠂⠌⠳⠾⣖⠻⣍⣏⠶⠙⠠⢈⣄⣡⣶⣯⣴⣿⣿⣿⣿⣿⣿
    ⠾⡵⣞⢷⡺⢵⢫⠞⣎⠳⢫⡾⡽⢯⣳⡽⡾⣝⣷⣛⡾⣛⡾⡽⣾⣤⣁⠂⠌⡉⠌⡈⠄⡁⢂⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⡸⣔⡬⣆⣱⢊⢦⡙⢆⠻⣹⢷⡻⣏⣷⢻⡽⡽⡶⢯⡽⣏⣷⣻⡵⣏⣟⣿⣶⣦⣔⣤⣲⣼⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⡡⡍⡜⡩⢍⡋⢇⡛⢭⠳⣹⠾⣽⡽⣚⣯⢷⣻⡽⢯⣷⢻⡼⣧⢿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣉⠳⢨⠱⣩⢜⣡⣚⣤⡳⣼⡻⢧⡿⡽⣞⡽⣶⢻⣻⡼⢯⣷⣛⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡄⢻⡳⣏⣏⣽⣯⣽⣉⣾⣍⣹
        """
        for i in range(5):
            print(midoriya)

    elif A =='2':
        midoriya2 = r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠈⠹⣶⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣷⣤⣠⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⡻⠛⠳⠆⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣾⣿⣿⣶⣾⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣽⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⢿⣹⣿⣿⣿⣿⣯⣹⣿⣿⣿⣿⣿⣿⣿⣿⣷⡶⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣿⣿⣿⢿⣿⣿⢿⠉⠛⢿⢛⠘⣿⣿⡟⠻⡛⢉⢹⣿⣿⢯⣿⣿⡛⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⣿⣿⢿⣿⢆⡈⠌⡁⢂⠌⣥⠈⢃⠉⡐⢀⠾⣻⢟⣾⣿⣿⣛⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢋⣾⣿⣿⣦⣧⢈⠄⡉⢁⠋⡘⢉⠡⢈⠡⢉⠆⡱⣶⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⡖⣾⣿⣿⣿⣿⣿⣆⠈⡐⢀⠂⡰⣄⡢⡄⢆⡔⢢⣽⢛⢟⡛⢯⡙⡿⢩⣿⣷⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢞⠴⡣⢜⡻⢛⠿⣿⠿⠒⠤⢚⡱⢡⠒⡡⠏⡔⢣⡘⡌⣦⡹⢦⠳⢾⣿⣿⣿⣿⣿⣿⣿⡿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡈⣶⡑⡎⠴⣉⠖⡨⢇⠩⢒⡡⢜⣡⢞⣴⣳⣾⣷⣾⣿⢇⡱⢪⡱⢏⣏⣿⣿⣟⡿⣿⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⡝⢳⣟⡽⣳⣬⣖⣡⢎⣱⢢⣗⢯⣞⡻⣼⣹⣿⣗⡻⡟⢮⢛⢣⡱⡞⢞⣿⣿⣿⣽⢯⣟⣯⡿⣦⣴⣤⣀⠀⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡝⣌⠣⣌⡙⡳⢓⠞⣙⠫⡍⡛⣌⢓⡞⢳⣃⠛⣇⢋⠖⡩⢂⠵⡒⡭⡜⣬⣛⣿⣿⣯⡿⣯⡷⣟⣿⣽⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⢺⣽⡾⣿⡤⢝⡰⣉⠞⡤⢓⠴⡱⣌⠣⡜⢥⣎⢻⡘⢮⡒⣥⣫⢶⣽⣞⢿⡽⣯⣿⣿⣿⣿⣳⡿⣯⠗⠀⠀⠉⠉⢻⡶⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣹⠾⣵⢯⣿⡷⣧⢧⣿⡰⣉⡞⡱⢌⠳⡘⢦⡙⢧⣙⠶⣫⠕⣯⣟⠾⣼⣯⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡭⣿⣝⣾⣳⢏⡻⣍⣿⠿⣙⢳⣧⣭⢆⡙⢦⡙⢦⢩⠲⣡⢛⡼⣯⣻⣽⣿⣿⣿⣿⣿⣏⢿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣟⣷⣻⠾⣝⠮⡵⣎⠻⣅⢣⠎⣝⠻⣷⡌⣣⠎⣕⡊⢧⢱⢊⣽⣷⣻⣿⣿⣿⣿⣿⣿⡇⡚⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """
        for i in range(5):
            print(midoriya2)

    elif A == '3':
        midoriya3 = r"""
    ⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⡿⣽⢯⣟⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣽⡿⣽⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣾⣿⣷⣿⣯⣿⢿⡾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣽⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡿⣿⢿⣿⢿⣻⡽⣯⣟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢿⣿⣾⡿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣯⡿⣽⣻⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣽⢿⣽⣿⣿⣿
    ⣿⣿⣿⣿⣿⢿⣹⣿⣽⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⣿⣿⣻⣿⣿
    ⣿⣿⣿⣿⣿⣻⣟⣷⣟⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣯⣷⣿⢿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣻⣾⣿⣿⣿⣿⣿⣿⠿⣻⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⡿⣯⣿⢷⣿⣿⣿
    ⣿⣿⣿⣿⣿⣳⠿⢷⣿⡏⣿⣿⣿⡿⠳⣮⣵⣦⣽⣿⣿⣿⣿⣿⡛⢦⣿⣿⣏⡞⣷⣿⣳⢿⣯⣿⣾⣿
    ⣿⣿⣿⣿⣿⣯⣷⣿⣿⣟⢿⡹⣿⠀⠁⣿⣧⢘⣿⡿⠟⡉⢾⣯⠅⡢⢿⠟⣫⣸⣟⠼⣯⣟⣷⡿⣿⣿
    ⣿⣿⣿⣿⣿⢾⣽⣿⣿⣿⣯⣥⣏⠢⡡⠄⠤⠑⡈⢴⡀⠐⠆⠄⡐⡠⢊⣎⣵⣿⣿⣛⣷⣻⣯⣿⣿⣿
    ⣿⡿⣿⢿⢿⣿⡯⣞⣷⣿⣿⣿⣿⡄⠅⡈⠄⠡⠐⡈⠡⢈⠐⠠⢁⠤⣱⣿⢿⡿⢹⡉⢿⣩⣿⣿⣿⣿
    ⡿⣿⣭⣟⡞⣶⢻⣽⣿⣿⣿⣿⣿⠿⣦⡐⡈⠄⢓⡐⣃⠂⠌⣰⠴⡚⡍⡒⢦⡹⣡⢚⣴⣿⣿⣿⣿⣿
    ⣿⣿⣾⣭⠟⣈⣋⣫⣽⣿⡡⠞⣄⠦⣌⣿⣷⣬⣷⢯⣰⢿⠾⣉⡖⡵⢊⡝⢢⣱⡬⢻⣯⣿⣿⣿⣿⣿
    ⣿⣿⣓⠊⠄⡉⣩⠶⠛⣡⣴⡾⠎⠚⡝⠳⣾⣱⡯⢿⣹⣞⢷⣋⢴⣡⣷⣾⣏⢷⣹⡸⠗⡼⣿⣿⣿⣿
    ⠉⠄⠠⢉⠑⠚⢅⣢⠝⠛⠡⣐⣬⣖⡩⣧⣘⡷⣛⢯⢷⢯⣿⣿⢿⠻⠿⣛⠬⢏⠶⡱⢛⡒⢿⣿⣿⣿
    ⠀⠌⡐⠠⢈⠐⠠⠐⠬⡴⠛⢋⣉⡤⠴⣈⡿⣼⡽⣟⣛⢫⣍⣒⣌⣣⠵⣬⢳⠼⡒⢥⢃⢞⣦⢯⣹⣿
    ⣶⢦⣄⠁⠂⠌⠠⢁⠂⡑⠞⠛⢛⡙⡈⣷⡻⡝⡩⠍⣍⢣⢌⡱⢌⡡⣋⢔⠣⡜⣹⠶⡋⣿⣿⣿⣮⢻
    ⢍⡻⢞⣷⡌⠠⢁⠂⡐⢬⣹⣶⢿⣿⣇⡾⢱⠘⡔⣩⢶⢋⠦⡑⢎⣖⡳⠪⠙⡉⢁⠂⡁⣟⣦⣟⣨⣵
        """
        for i in range(5):
            print(midoriya3)

    elif A == '4':
        midoriya4 = r"""

    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣯⡝⡿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣾⣿⣿⣿⣿⡙⣿⣿⣿⣿⣿⡿⣩⢻⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣷⣝⡲⣍⠟⣿⣿⣿⢿⣿⣿⣿⡾⣿⣿⢣⠧⣹⣿⣿⣿⣻⠝⡲⢥⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣴⡩⢟⣯⡿⣿⣿⣿⢿⡇⡞⣱⣿⣿⢣⢿⣿⠹⣵⡿⠿⢿⡛⢏⣶⣿⣿⣿⣿
    ⣿⣿⣿⢻⢿⣿⣴⣭⣙⠿⣿⣿⡿⣾⣟⡿⣿⣿⣯⡷⣝⣿⣿⡟⡡⢞⣏⢳⣿⡱⣍⡦⣙⡜⣿⣿⣿⣿⣿
    ⣿⣿⣿⣇⢎⡹⢛⢿⣿⣿⣻⢾⣽⣳⢯⢿⣳⣟⡾⣽⢯⡷⣯⣱⢋⡜⢧⣹⢾⣽⣻⡒⠥⡾⣛⠝⣶⣿⣿
    ⣿⣿⡿⢿⣾⡄⢋⢾⣽⡷⣯⣟⡾⣯⣟⣞⡿⣾⡽⣯⢿⡽⣾⢽⠢⡜⣦⢽⣛⣾⣳⠿⡑⢢⢡⣿⣿⣿⣿
    ⣿⣿⣿⣧⢎⡙⠂⡜⡻⣿⣳⢯⣟⣷⣻⢾⣽⣳⠿⣽⢯⣟⡷⣏⣲⢿⣹⡾⡽⢶⡋⡔⠣⣐⢫⣿⣿⣿⣿
    ⣿⣽⣿⣿⣿⡴⡁⠄⠱⢎⠽⣛⣾⣳⢯⣟⡶⣯⢿⣽⣻⢾⡽⣾⢽⣞⢷⡻⠍⡳⠌⠠⠑⡈⣽⣿⣿⣿⣿
    ⣿⣿⣽⢯⢶⣵⡈⠄⠁⠮⣀⠙⢶⣯⢟⣾⣳⢽⣛⣮⢷⣯⢿⡽⡾⣽⠞⣁⠶⠉⡀⢁⢢⣼⢿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣎⢳⣯⣤⠁⠄⠈⠑⣮⣹⣟⡮⣟⡦⢿⣭⢿⡼⣯⣟⡽⣣⠞⠁⠂⡀⠐⣠⣟⢮⣿⣿⣿⣻⣿
    ⣿⣿⣿⣿⣿⣦⣅⠻⣦⣆⠈⠀⡙⠢⢋⠹⣶⢷⣻⢾⣯⣼⡷⠽⠎⠏⡀⢌⣰⣄⣷⣉⢾⣻⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣽⣷⣿⣏⠓⠖⠰⠢⢄⠢⠝⢫⣰⣆⢚⠵⢩⣐⣀⠦⡜⠩⣐⢿⣳⣯⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣷⣯⣟⢦⠈⡄⢁⠂⡐⠈⠌⣷⢫⠁⠂⠄⠠⡀⠡⡐⣡⢮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣬⣡⢊⠤⣁⢂⠸⡁⢌⡐⢌⠤⣡⣳⣼⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⢿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣞⣶⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣿
    ⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣷⣿⣿⢣
    ⣽⣏⣿⣿⣾⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣿⢿⡳⢯⡘
    ⡿⣶⣫⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡙⢮⣽⣳⣬
        """
        for i in range(5):
            print(midoriya4)
    else:
        print("잘못된 입력입니다. 1~4 또는 0을 입력하세요.")

