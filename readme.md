# Pipe Puzzle Solver

This project is a Python-based solver (search algorithm) for pipe puzzles. The solver takes a grid of pipes and determines the correct configuration to connect all the pipes and let the water flow from the source to all the destinations.

## Features

- Solves pipe puzzles of 4*4 grid
- Supports different types of pipes (4 types)
- Provides a visual representation of the solution (connected pipes)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/trungdung1711/puzzle-pipes.git
    ```
2. Navigate to the project directory:
    ```sh
    cd ./puzzle-pipes
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your puzzle input file in the specified format in /data and also import them into main.py to create the state of a grid:
    ```sh
    cp data1.py dataxx.py
3. Choose different types of search algorithms or heuristic function (h(n) if informed search) and get the solution node (containing the goal state)
4. Run the solver:
    ```sh
    python main.py solve -d 6 -a 5 -e 5 -i true -s true
    python main.py --help or python main.py solve --help for more information
    ```
5. View the solution output by simple pygame and matplotlib

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License



## Contact

For any questions or suggestions, please open an issue or contact me at [dung.lebk2210573@hcmut.edu.vn](mailto:dung.lebk2210573@hcmut.edu.vn).
