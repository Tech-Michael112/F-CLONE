import random
import time
from rich.console import Console
import os

console = Console()
flag_file = 'User_ID.flag'
def generate_binary_line(length):
    return ''.join(random.choice('01') for _ in range(length))
colors = ["bold green", "bold cyan", "bold magenta", "bold yellow", "bold red", "bold blue"]




def binary_animation(lines=20, line_length=50, duration=5):
    console.clear()
    end_time = time.time() + duration
    while time.time() < end_time:
        for _ in range(lines): 



            color = random.choice(colors)
          #  console.print(binary_line, style=color)



            binary_line = generate_binary_line(line_length)
            console.print(binary_line, style=color)
        time.sleep(0.1) 
        console.clear()

    console.print("\n\n[bold green]Welcome to the Hacker's Den[/bold green]\n", justify="center")
    console.print("[green]Access Granted...[/green]\n", justify="center")
    time.sleep(2)  
def appreciation_message():
    os.system('clear')
    console.print("\n[bold green]Thank you for being a part of this journey![/bold green]", justify="center")
    console.print(f"[bold green]We've reached 100 members![/bold green]", justify="center")
    console.print("[bold green]Your support means everything.[/bold green]", justify="center")
    console.print("\n\n[green]Let's continue to grow together.[/green]", justify="center")
    x=input(" press enter to continue -- ")
    import c
def check_animation_shown():
    if os.path.exists(flag_file):
        with open(flag_file, 'r') as f:
            return f.read().strip() == 'True'
    return False

def mark_animation_as_shown():
    with open(flag_file, 'w') as f:
        f.write('True')
def main():
    if not check_animation_shown():
        binary_animation()
        appreciation_message()
        mark_animation_as_shown()
    else:
        console.print("\n[green]Welcome back![/green]\n", justify="center")
        import c 
    
main()
