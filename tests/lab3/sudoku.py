import pathlib
import typing as tp

import random
import time

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    a = []
    for i in range(n):
        a.append(values[:n])
        values = values[n:]
    return a


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    a = []
    for i in grid:
        a.append(i[pos[1]])
    return a

def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    x0 = (pos[0] // 3) * 3
    x1 = x0 + 3
    y0 = (pos[1] // 3) * 3
    y1 = y0 + 3
    a = []
    for i in grid[x0:x1]:
        a += i[y0:y1]
    return a


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for index, row in enumerate(grid):
        if "." in row:
            return index, row.index(".")
    return None

all_values = {str(x) for x in range(1,10)}

def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    row = get_row(grid, pos)
    col = get_col(grid, pos)
    block_values = set(get_block(grid, pos))

    free_values = all_values - block_values
    possible_values = set()

    for value in free_values:
        if value in row or value in col:
            continue
        possible_values.add(value)
    return possible_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    def get_solution( inGrid: tp.List[tp.List[str]],) -> tp.Optional[tp.List[tp.List[str]]]:
        empty_pos = find_empty_positions(inGrid)
        if empty_pos is None:
            return inGrid

        possible_values = find_possible_values(inGrid, empty_pos)
        if not possible_values:
            return None

        row_empty_pos, col_empty_pos = empty_pos
        for value in possible_values:
            inGrid[row_empty_pos][col_empty_pos] = value
            if get_solution(inGrid) is not None:
                return inGrid

            inGrid[row_empty_pos][col_empty_pos] = "."
        return None
    return get_solution(grid)


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
    for row_index in range(9):
        for col_index in range(9):
            row_values = get_row(solution, (row_index, col_index))
            col_values = get_col(solution, (row_index, col_index))
            block_values = get_block(solution, (row_index, col_index))

            all_sets = set(row_values) and set(col_values) and set(block_values)

            is_solution = (
                len(row_values) == len(set(row_values)),
                len(col_values) == len(set(col_values)),
                len(block_values) == len(set(block_values)),
                not (all_sets - all_values),)

            if not all(is_solution):
                return False
    return True



def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    empty_sudoku = [["." for _ in range(9)] for _ in range(9)]
    if N == 0:
        return empty_sudoku

    sudoku = solve(grid=empty_sudoku)
    if sudoku is None:
        return empty_sudoku

    field_square_size = 9 * 9
    if N > field_square_size:
        return sudoku

    free_position_count = field_square_size - N
    while free_position_count != 0:
        row_index_position, col_index_position = (
            random.randint(0, 8),
            random.randint(0, 8),
        )

        if sudoku[row_index_position][col_index_position] == ".":
            continue

        sudoku[row_index_position][col_index_position] = "."
        free_position_count -= 1

    return sudoku

def run_solve(puzzle: tp.List[tp.List[str]]) -> None:
    start = time.time()
    solution = solve(puzzle)
    end = time.time()
    if solution is not None:
        print(f"{end-start}")
        display(solution)
    else:
        print(f"Puzzle {puzzle} can't be solved")
        
if __name__ == "__main__":
    import os
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(f"{os.getcwd()}/src/lab3/{fname}")
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)