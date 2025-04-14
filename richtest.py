# rich 설치가 안 돼 있다면 먼저 설치: pip install rich

from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

console = Console()

# 🎨 1. 컬러 출력
print("[bold red]해병대[/bold red]는 [green]강하다[/green]!")

# 📋 2. 로그 출력
console.log("이것은 로그 메시지다.")

# 📊 3. 테이블 출력
table = Table(title="해병대원 명단")

table.add_column("이름", style="cyan", no_wrap=True)
table.add_column("계급", style="magenta")
table.add_column("기수", justify="right", style="green")

table.add_row("김지원", "병장", "1293")
table.add_row("이승민", "병장", "1278")

console.print(table)

# 📈 4. 진행 바
for step in track(range(10), description="진행 중..."):
    time.sleep(0.2)

from rich import print

print("[red]적색 텍스트[/red]")
print("[green]녹색 텍스트[/green]")
print("[blue]파란색 텍스트[/blue]")
print("[yellow]노란색 텍스트[/yellow]")
print("[magenta]자홍색 텍스트[/magenta]")
print("[cyan]청록색 텍스트[/cyan]")
print("[white]흰색 텍스트[/white]")
