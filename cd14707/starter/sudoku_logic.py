import copy
import random
from typing import List, Tuple

SIZE: int = 9
EMPTY: int = 0
Board = List[List[int]]


def deep_copy(board: Board) -> Board:
    """Return a deep copy of a board.

    Board is represented as a list of rows, each a list of ints (1-9 or 0 for empty).
    """
    return copy.deepcopy(board)


def create_empty_board() -> Board:
    """Create an empty SIZE x SIZE board filled with EMPTY."""
    return [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]


def is_safe(board: Board, row: int, col: int, num: int) -> bool:
    """Return True if placing `num` at (row, col) doesn't violate Sudoku rules.

    Checks row, column, and the 3x3 box for duplicates.
    """
    # Check row and column
    for x in range(SIZE):
        if board[row][x] == num or board[x][col] == num:
            return False
    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def fill_board(board: Board) -> bool:
    """Fill the board in-place using randomized backtracking.

    Returns True when the board is fully filled (valid solution); otherwise False.
    """
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == EMPTY:
                possible = list(range(1, SIZE + 1))
                random.shuffle(possible)
                for candidate in possible:
                    if is_safe(board, row, col, candidate):
                        board[row][col] = candidate
                        if fill_board(board):
                            return True
                        board[row][col] = EMPTY
                # No candidate worked, backtrack
                return False
    # No empty cells left -> board is complete
    return True


def remove_cells(board: Board, clues: int) -> None:
    """Remove cells from `board` in-place until `clues` filled cells remain.

    `clues` is the number of filled cells that should remain (not the number to remove).
    """
    attempts = SIZE * SIZE - clues
    while attempts > 0:
        row = random.randrange(SIZE)
        col = random.randrange(SIZE)
        if board[row][col] != EMPTY:
            board[row][col] = EMPTY
            attempts -= 1


def generate_puzzle(clues: int = 35, ensure_unique: bool = True, max_tries: int = 10) -> Tuple[Board, Board]:
    """Generate a new Sudoku puzzle.

    Returns a tuple `(puzzle, solution)`. `puzzle` contains `EMPTY` (0) for blanks.

    If `ensure_unique` is True the generator will retry up to `max_tries`
    attempts to produce a puzzle with a single unique solution. If it fails
    the last generated puzzle is returned (which may have multiple solutions).
    """
    if not ensure_unique:
        board = create_empty_board()
        fill_board(board)
        solution = deep_copy(board)
        remove_cells(board, clues)
        puzzle = deep_copy(board)
        return puzzle, solution

    # Attempt to produce a puzzle with a single unique solution.
    tries = 0
    while True:
        tries += 1
        board = create_empty_board()
        fill_board(board)
        solution = deep_copy(board)
        remove_cells(board, clues)
        puzzle = deep_copy(board)

        # Check uniqueness: count solutions up to (limit=2) to detect multiples
        count = count_solutions(deep_copy(puzzle), limit=2)
        if count == 1:
            return puzzle, solution
        if tries >= max_tries:
            # Give up and return the last generated puzzle (may have multiple solutions)
            return puzzle, solution


def count_solutions(board: Board, limit: int = 2) -> int:
    """Count number of solutions for `board` up to `limit`.

    Uses backtracking and stops early when the count reaches `limit`.
    """
    def _find_empty(bd: Board):
        for r in range(SIZE):
            for c in range(SIZE):
                if bd[r][c] == EMPTY:
                    return r, c
        return None

    def _search(bd: Board, acc: List[int]) -> None:
        if acc[0] >= limit:
            return
        empty = _find_empty(bd)
        if not empty:
            acc[0] += 1
            return
        r, c = empty
        for num in range(1, SIZE + 1):
            if is_safe(bd, r, c, num):
                bd[r][c] = num
                _search(bd, acc)
                bd[r][c] = EMPTY
                if acc[0] >= limit:
                    return

    accumulator = [0]
    _search(board, accumulator)
    return accumulator[0]
