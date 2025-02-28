# package but allow us to access to module/function/class at the package level
import click
import search as Search
import data as Data
from util import *
import time
from memory_profiler import memory_usage
from search import search
from search import PPP
from state import PipeTouch


@click.group()
def cli():
    pass


# python main.py solve -d 13 -a 5 -e 5 -i true -s true
@cli.command()
@click.option('-st', '--state',      default = 1,            required = True,    type = click.IntRange(1,2)  ,     help = 'The state representation of the game')
@click.option('-d',  '--data',       default = 1,            required = True,    type = click.IntRange(1, 100),     help = 'The data used to run the search algorithm, in /data')
@click.option('-a',  '--algorithm',  default = 1,            required = True,    type = click.IntRange(1, 7) ,     help = 'Search algorithm including BrFS[1], DFS[2], DLS[3], IDS[4], BFS[5]')
@click.option('-e', '--ef',                                 required = False,   type = click.IntRange(1, 11) ,     help = 'Evalution function, in /search')
@click.option('-dp', '--depth',                             required = False,   type = int,                       help = 'The depth limit to search when using [DLS]')
@click.option('-l', '--limit',                              required = False,   type = int,                       help = 'The limit to search when using [IDS]')
@click.option('-i', '--interactive',default = False,        required = False,   type = bool,                      help = 'Show interactive [UI]')
@click.option('-s', '--statistic',  default = False,        required = False,   type = bool,                      help = 'Show [statistic]')
def solve(state :int, data : 'int', algorithm : 'int', ef : 'int', depth : 'int', limit : 'int', interactive : 'bool', statistic : 'bool'):
    # todo: different state
    if state == 1:
        problem = Search.PipePuzzleProblem(Data.data[data]())
        algo = Search.search_algorithm[algorithm]
    else:
        problem = Search.PPP(PipeTouch(Data.data[data]()))
        algo = Search.search_algorithm[algorithm]
    # todo: initialize the problem, data and algorithm used
    solution_node = None
    mem = None

    # todo: call the algorithm and get solution_node + time + memory
    start = Align.center("[bold cyan]:fire: SEARCH ALGORITHM START :fire:[/bold cyan]")
    output.print(Panel(start, title=":rocket: Running...", border_style="bold yellow"))

    start_time = time.time()

    if algorithm == 1:
        # Case BrFS
        output.print("[bold blue]:mag:Breath-First Search (BFS) is running...[/bold blue]")
        # solution_node = algo(problem)
        mem, solution_node = memory_usage(lambda: algo(problem), retval=True, interval=0.1)

    elif algorithm == 2:
        # Case DFS
        output.print("[bold blue]:mag:Depth-First Search (DFS) is running...[/bold blue]")
        # solution_node = algo(problem)
        mem, solution_node = memory_usage(lambda: algo(problem), retval=True)

    elif algorithm == 3 and depth is not None:
        # Case DLS
        output.print("[bold blue]:mag:Depth-Limit search (DLS) is running...[/bold blue]")
        # solution_node = algo(problem, depth)
        mem, solution_node = memory_usage(lambda: algo(problem, depth), retval=True)

    elif algorithm == 4 and limit is not None:
        # Case IDS
        output.print("[bold blue]:mag:Iterative Deepening search (IDS) is running...[/bold blue]")
        # solution_node = algo(problem, limit)
        mem, solution_node = memory_usage(lambda: algo(problem, limit), retval=True)

    elif algorithm == 5 and ef is not None:
        # Case BFS
        output.print("[bold blue]:mag:Best-First search (BFS) is running...[/bold blue]")
        evaluation_function = Search.evaluation_function[ef]
        # solution_node = algo(problem, evaluation_function)
        mem, solution_node = memory_usage(lambda: algo(problem, evaluation_function), retval=True)
    
    elif algorithm == 6:
        # Case BrFS for state v2
        output.print("[bold blue]:mag:Breadth-First search <v2> (BFS) is running...[/bold blue]")
        mem, solution_node = memory_usage(lambda: algo(problem), retval=True)


    elif algorithm == 7:
        # Case DFS
        output.print("[bold blue]:mag:Depth-First Search <v2> (DFS) is running...[/bold blue]")
        # solution_node = algo(problem)
        mem, solution_node = memory_usage(lambda: algo(problem), retval=True)

    elif algorithm == 8 and depth is not None:
        # Case DLS
        output.print("[bold blue]:mag:Depth-Limit search (DLS) is running...[/bold blue]")
        # solution_node = algo(problem, depth)
        mem, solution_node = memory_usage(lambda: algo(problem, depth), retval=True)

    else:
        raise SyntaxError('Invalid options')

    end_time = time.time()
    running_time = end_time - start_time
    steps = None

    if solution_node == Search.Result.CUTOFF:
        output.print('DLS: [red]Unable to find solution at current depth:exclamation:[/red]')
        return

    elif solution_node == Search.Result.FAILURE:
        output.print('IFS: [red]Unable to find solution in range of limit:exclamation:[/red]')
        return

    elif solution_node is None:
        output.print('Searching failed: [red]There might be no solution :x:[/red]')
        return

    else:
        # solution found
        done = Align.center("[bold magenta]:white_check_mark: SEARCH ALGORITHM COMPLETED :white_check_mark:[/bold magenta]")
        output.print(Panel(done, title=":dart: Done!", border_style="bold green"))
        actions = Stack()
        actions_ui = Stack()
        traverse = solution_node

        while traverse.get_parent() is not None:
            actions.push(traverse.get_action())
            actions_ui.push(traverse.get_action())
            traverse = traverse.get_parent()
        
        steps = actions_ui.size()

        while actions.size() > 0:
            location = actions.pop()
            output.print(f'Click the pipe at location [yellow]({location[0]}, {location[1]})[/yellow]')

    if interactive is True:
        # todo: showing UI
        import game
        game.ui(Data.data[data](), actions_ui)


    # - Show time and space information by UI
    if statistic is True:
        from sta import bar_chart
        from sta import radar_chart
        from sta import extensive_memory_usage
        # todo: get the time and memory to create statistic
        info = Align.center(f"""[white]:book: Data:[/white] [yellow]{data}[/yellow]\n[bold cyan]:hourglass: Time:[/bold cyan] [green]{running_time}s[/green]\n[bold magenta]:brain: Memory:[/bold magenta] [yellow]{max(mem)}[/yellow]\n[bold green]:walking: Steps:[/bold green] [cyan]{steps}[/cyan]\n[bold blue]:package: Frontier Size:[/bold blue] [red]{search.frontier_size} nodes[/red]""",vertical="middle")
        output.print(Panel(info, title=":pencil: Statistics :pencil:", border_style="red"))

        bar_chart(running_time, mem, search.frontier_size, steps)
        radar_chart(running_time, mem, search.frontier_size, steps)
        extensive_memory_usage(mem)

    end = Align.center(":bust_in_silhouette: [green]trungdung1711[/green] | :id: [yellow]2210573[/yellow] | :school: [blue]HCMUT[/blue]")
    output.print(Panel(end, title=":heart: Thank you :heart:", border_style="yellow"))