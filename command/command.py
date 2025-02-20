# package but allow us to access to module/function/class at the package level
import click
import search as Search
import data as Data
from util import Stack
from util import output
from util import Panel
from util import Align


@click.group()
def cli():
    pass


@cli.command()
@click.option('-d', '--data',       default = 1,            required = True,    type = click.IntRange(1, 17),     help = 'The data used to run the search algorithm, in /data')
@click.option('-a', '--algorithm',  default = 1,            required = True,    type = click.IntRange(1, 5) ,     help = 'Search algorithm including BrFS[1], DFS[2], DLS[3], IDS[4], BFS[5]')
@click.option('-e', '--ef',                                 required = False,   type = click.IntRange(1, 8) ,     help = 'Evalution function, in /search')
@click.option('-d', '--depth',                              required = False,   type = int,                       help = 'The depth limit to search when using [DLS]')
@click.option('-l', '--limit',                              required = False,   type = int,                       help = 'The limit to search when using [IDS]')
@click.option('-i', '--interactive',default = False,        required = False,   type = bool,                      help = 'Show interactive [UI]')
@click.option('-s', '--statistic',  default = False,        required = False,   type = bool,                      help = 'Show [statistic]')
def solve(data : 'int', algorithm : 'int', ef : 'int', depth : 'int', limit : 'int', interactive : 'bool', statistic : 'bool'):
    # todo: initialize the problem, data and algorithm used
    problem = Search.PipePuzzleProblem(Data.data[data]())
    algo = Search.search_algorithm[algorithm]
    solution_node = None

    # todo: call the algorithm and get solution_node + time + memory
    start = Align.center("[bold cyan]:fire: SEARCH ALGORITHM START :fire:[/bold cyan]")
    output.print(Panel(start, title=":rocket: Running...", border_style="bold yellow"))

    if algorithm == 1:
        # Case BrFS
        output.print("[bold blue]:mag:Breath-First Search (BFS) is running...[/bold blue]")
        solution_node = algo(problem)

    elif algorithm == 2:
        # Case DFS
        output.print("[bold blue]:mag:Depth-First Search (DFS) is running...[/bold blue]")
        solution_node = algo(problem)

    elif algorithm == 3 and depth is not None:
        # Case DLS
        output.print("[bold blue]:mag:Depth-Limit search (DLS) is running...[/bold blue]")
        solution_node = algo(problem, depth)

    elif algorithm == 4 and limit is not None:
        # Case IDS
        output.print("[bold blue]:mag:Iterative Deepening search (IDS) is running...[/bold blue]")
        solution_node = algo(problem, limit)

    elif algorithm == 5 and ef is not None:
        # Case BFS
        output.print("[bold blue]:mag:Best-First search (BFS) is running...[/bold blue]")
        evaluation_function = Search.evaluation_function[ef]
        solution_node = algo(problem, evaluation_function)

    else:
        raise SyntaxError('Invalid options')

    if solution_node == Search.Result.CUTOFF:
        output.print('DLS: [red]Unable to find solution at current depth:exclamation:[/red]')

    elif solution_node == Search.Result.FAILURE:
        output.print('IFS: [red]Unable to find solution in range of limit:exclamation:[/red]')

    elif solution_node is None:
        output.print('Searching failed: [red]There might be no solution :x:[/red]')

    else:
        # solution found
        done = Align.center("[bold magenta]:white_check_mark: SEARCH ALGORITHM COMPLETE :white_check_mark:[/bold magenta]")
        output.print(Panel(done, title=":dart: Done!", border_style="bold green"))
        actions = Stack()
        actions_ui = Stack()
        traverse = solution_node

        while traverse.get_parent() is not None:
            actions.push(traverse.get_action())
            actions_ui.push(traverse.get_action())
            traverse = traverse.get_parent()
        
        while actions.size() > 0:
            location = actions.pop()
            output.print(f'Click the pipe at location [yellow]({location[0]}, {location[1]})[/yellow]')

    if interactive == True:
        # todo: showing UI
        pass


    # - Show time and space information by UI
    if statistic == True:
        # todo: get the time and memory to create statistic
        pass

    end = Align.center(":bust_in_silhouette: [green]Trung Dung[/green] | :id: [yellow]2210573[/yellow] | :school: [blue]HCMUT[/blue]")
    output.print(Panel(end, title=":heart: Thank you :heart:", border_style="yellow"))