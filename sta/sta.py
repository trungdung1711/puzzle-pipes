import matplotlib.pyplot as plt
import numpy as np
from util import Panel
from util import output
from util import Align


def bar_chart(time: float, memory_usage: list, nodes: int, steps: int):
    labels = ['Execution time (s)', 'Memory usage (MB)', 'Solution steps (steps)']
    values = [time, max(memory_usage), steps]

    fig, ax_left = plt.subplots(figsize=(9, 5))
    fig.canvas.manager.set_window_title('algorithm statistics')

    color1 = ['blue', 'purple', 'green']
    bars1 = ax_left.bar(labels, values, color=color1, alpha=0.7, label='Metrics')

    ax_left.set_ylabel('Time (s) / Memory (MB) / Steps', color='red')
    ax_left.set_ylim(0, max(values) * 1.2)

    ax_right = ax_left.twinx()
    bars2 = ax_right.bar(['Max Frontier Nodes'], [nodes], color='orange', alpha=0.7, label='Frontier Nodes (nodes)')

    ax_right.set_ylabel('Max Frontier Nodes', color='red')
    ax_right.set_ylim(0, nodes * 1.2)

    # label
    for bar, value in zip(bars1, values):
        ax_left.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, f'{value:.2f}', ha='center', fontsize=12, color='black')

    for bar, value in zip(bars2, [nodes]):
        ax_right.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, f'{value}', ha='center', fontsize=12, color='black')

    plt.title('Statistics of Search Algorithm')
    fig.tight_layout()
    plt.show()


def radar_chart(time : 'float', memory_usage : 'list', nodes : 'int', steps : 'int'):
    labels = ['time', 'memory', 'steps']
    values = [time, max(memory_usage), steps]

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    fig.canvas.manager.set_window_title('algorithm statistics')
    ax.fill(angles, values, color='red', alpha=0.25)
    ax.plot(angles, values, color='red', linewidth=2)  
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    plt.title('Algorithm Performance Overview')
    plt.show()


def extensive_memory_usage(memory_usage : 'list'):
    # Basic statistics
    min_mem = min(memory_usage)
    max_mem = max(memory_usage)
    avg_mem = np.mean(memory_usage)

    mem = Align.center(f"""[bold cyan]:bar_chart: min:[/bold cyan] [green]{min_mem}s[/green]\n[bold magenta]:bar_chart: max:[/bold magenta] [yellow]{max_mem}[/yellow]\n[bold green]:bar_chart: avg:[/bold green] [cyan]{avg_mem}[/cyan]""",vertical="middle")
    output.print(Panel(mem, title=":pencil: Memory analysis :pencil:", border_style="blue"))

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.canvas.manager.set_window_title("memory usage analysis")

    ax.plot(memory_usage, marker='o', linestyle='-', color='red', label='Memory usage')
    ax.axhline(y=avg_mem, color='blue', linestyle='--', label=f'Avg: {avg_mem:.2f} MB')
    
    ax.set_xlabel("Time Stamps")
    ax.set_ylabel("Memory (MB)")
    ax.set_title("Memory Usage Over Time")
    ax.legend()
    ax.grid(True)

    plt.show()