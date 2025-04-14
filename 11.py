from rich import print
from rich.panel import Panel
from rich.console import Console 
console = Console()              

def print_menu():
    console.print("[bold yellow]그림 출력 프로그램[/bold yellow]")
    console.print("[cyan]================[/cyan]")
    console.print("1. 미도리야 그림")
    console.print("2. 다른 그림")
    console.print("3. 또 다른 그림")
    console.print("4. 기타")
    console.print("[red]0을 입력하면 종료[/red]")
    console.print("[cyan]================[/cyan]")

    # 메뉴에서 선택된 숫자를 입력받음
    choice = input("원하는 번호를 입력하세요: ")
    if choice == '0':
        console.print("[bold red]프로그램 종료[/bold red]")
        return
    elif choice in ['1', '2', '3', '4']:
        print_picture(choice)
    else:
        console.print("[bold red]잘못된 입력입니다.[/bold red]")

def print_picture(number):
    if number == '1':
        midoriya = r"""
        [green]
    ⣏⡹⣬⣍⣣⣭⣙⣬⣍⢧⣻⣟⣿⡿⣿⢿⣿⢿⡿⣿⢿⡿⣿⢿⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⢢⠑⡦⣌⠱⣌⡙⡚⡔⢪⢿⣾⣽⡿⣽⣻⣿⣿⣿⣽⣯⣿⡽⣯⢿⣽⣻⣽⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠶⣩⠛⡜⣛⠲⠳⡱⢎⡓⢾⣯⢿⣽⢿⣳⢿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⡑⢆⡛⡔⢣⣋⡷⣵⣾⣞⡿⣽⣻⢯⡿⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣛⣞⠲⣙⢓⠻⣙⢛⢳⣯⣟⡷⣯⢿⣽⣳⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⢖⠻⣿⣶⢯⡶⣼⢾⣯⢿⣽⣻⣽⣻⢾⣽⣻⢾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⢮⠓⡞⢯⡿⣽⢯⣟⡾⣿⣾⣷⣯⣟⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠦⡹⠜⠦⡛⠿⣻⣾⣽⣷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⡷⣧⢟⡶⡽⣶⣣⣿⡽⣞⣷⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣙⢬⡩⣜⣡⢣⣿⣳⣟⡿⣾⡽⣿⣿⣿⣿⣿⣿⣿⣿⢏⠖⡀⢿⣿⣿⣿⣿⢏⠏⢹⣿⢏⢻⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣍⢦⣑⣆⣦⣿⣟⣷⢯⣟⣷⣻⡽⣯⣟⣿⣿⣿⣿⢏⠖⡀⢿⣿⣿⣿⣿⣧⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣬⣦⣭⣜⣤⣧⣞⣯⢿⣞⣷⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⢣⣍⣛⢯⣿⣾⡽⣞⣯⣿⣾⣿⣿⣿⣿⣿⣿⡿⣿⠓⡄⠰⠋⢼⠋⡔⢠⡾⠑⠈⢡⣥⣉⠐⠙⢦⠀⠌⡀⣿⠟⣿⣿⠏⣐⢶
    ⠱⡌⡍⢎⠴⣉⠭⣩⢹⣿⣿⢿⣿⣿⣿⣿⣿⣷⢬⡟⠳⣆⠁⢂⠐⠠⠘⠅⠀⠂⢸⣿⣋⠀⠄⠘⡆⠐⠠⠁⢌⡿⢋⠰⣏⢷
    ⡓⢬⡙⡬⣙⢌⡣⣅⢻⡷⡼⢯⣿⣿⣿⣿⣿⣿⣿⢿⠄⠐⣿⡇⠠⠈⠄⡁⢂⠀⠐⠀⠹⠋⢀⠠⢘⠄⡁⢂⠁⢂⠐⠠⡶⣩⠶
    ⠟⣣⢙⡱⣉⢎⡱⣉⠻⢏⢿⣿⣿⢿⣿⣿⣿⢿⣿⣿⣏⠦⡄⢔⡄⠈⠄⠂⠄⡁⠂⠄⡐⠠⢁⠂⠔⢠⠁⢂⠁⠂⡄⠙⣶⠿⣽
        [/green]
        """
        lines = midoriya.splitlines()
        height = len(lines)
        width = max(len(line) for line in lines)
        console.print(Panel(midoriya, title="midoriya", border_style="bold green", width=width+4, height=height+4))

# 프로그램 실행
while True:
    print_menu()

