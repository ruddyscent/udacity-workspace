import os
import sys
import random
from typing import Any

# Ensure repository root is on sys.path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sudoku_logic


def test_generate_puzzle_and_solution_shape() -> None:
    random.seed(0)
    puzzle, solution = sudoku_logic.generate_puzzle(clues=35)
    assert len(puzzle) == sudoku_logic.SIZE
    assert len(solution) == sudoku_logic.SIZE
    for i in range(sudoku_logic.SIZE):
        assert len(puzzle[i]) == sudoku_logic.SIZE
        assert len(solution[i]) == sudoku_logic.SIZE
        for j in range(sudoku_logic.SIZE):
            assert 0 <= puzzle[i][j] <= sudoku_logic.SIZE
            assert 1 <= solution[i][j] <= sudoku_logic.SIZE


def test_puzzle_consistent_with_solution() -> None:
    random.seed(1)
    puzzle, solution = sudoku_logic.generate_puzzle(clues=35)
    for i in range(sudoku_logic.SIZE):
        for j in range(sudoku_logic.SIZE):
            if puzzle[i][j] != 0:
                assert puzzle[i][j] == solution[i][j]


def test_generated_puzzle_has_unique_solution() -> None:
    # Generate several puzzles with different seeds and ensure uniqueness
    for seed in (2, 3, 5):
        random.seed(seed)
        # Ask generator to retry more aggressively to obtain a unique puzzle.
        puzzle, solution = sudoku_logic.generate_puzzle(clues=35, ensure_unique=True, max_tries=200)
        count = sudoku_logic.count_solutions(sudoku_logic.deep_copy(puzzle), limit=3)
        assert count == 1, f"Puzzle produced by seed {seed} has {count} solutions"

def test_is_safe_validates_sudoku_rules() -> None:
    """Test that is_safe correctly validates row, column, and box constraints."""
    board = sudoku_logic.create_empty_board()
    
    # Place a number in the center
    board[4][4] = 5
    
    # Should not allow same number in same row
    assert not sudoku_logic.is_safe(board, 4, 0, 5)
    
    # Should not allow same number in same column
    assert not sudoku_logic.is_safe(board, 0, 4, 5)
    
    # Should not allow same number in same 3x3 box
    assert not sudoku_logic.is_safe(board, 3, 3, 5)
    
    # Should allow different number in same row
    assert sudoku_logic.is_safe(board, 4, 0, 1)
    
    # Should allow same number in different row/col/box
    assert sudoku_logic.is_safe(board, 0, 0, 5)


def test_count_solutions_early_exit() -> None:
    """Test that count_solutions stops early when limit is reached."""
    # Create a puzzle with multiple solutions (very few clues)
    random.seed(8)
    board = sudoku_logic.create_empty_board()
    sudoku_logic.fill_board(board)
    
    # Remove many cells to create multiple solutions
    for i in range(9):
        for j in range(9):
            if i > 1 or j > 1:  # Keep only top-left corner filled
                board[i][j] = 0
    
    # Count with low limit should return the limit
    count = sudoku_logic.count_solutions(sudoku_logic.deep_copy(board), limit=2)
    assert count >= 2, "Board with few clues should have multiple solutions"


def test_deep_copy_creates_independent_board() -> None:
    """Test that deep_copy creates a truly independent copy."""
    original = [[1, 2, 3] for _ in range(9)]
    copy = sudoku_logic.deep_copy(original)
    
    # Modify the copy
    copy[0][0] = 9
    
    # Original should remain unchanged
    assert original[0][0] == 1
    assert copy[0][0] == 9


def test_create_empty_board() -> None:
    """Test that create_empty_board returns a 9x9 board of zeros."""
    board = sudoku_logic.create_empty_board()
    
    assert len(board) == 9
    for row in board:
        assert len(row) == 9
        assert all(cell == 0 for cell in row)


def test_generate_puzzle_with_different_clue_counts() -> None:
    """Test puzzle generation with various clue counts."""
    for clues in [25, 30, 35, 40, 45]:
        random.seed(20 + clues)
        puzzle, solution = sudoku_logic.generate_puzzle(clues=clues, ensure_unique=False, max_tries=5)
        
        # Count prefilled cells
        filled = sum(1 for i in range(9) for j in range(9) if puzzle[i][j] != 0)
        assert filled == clues, f"Should have exactly {clues} clues"
        
        # Verify puzzle is consistent with solution
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != 0:
                    assert puzzle[i][j] == solution[i][j]


def test_fill_board_creates_valid_solution() -> None:
    """Test that fill_board produces a valid complete Sudoku solution."""
    random.seed(15)
    board = sudoku_logic.create_empty_board()
    result = sudoku_logic.fill_board(board)
    
    assert result is True, "fill_board should successfully complete the board"
    
    # Check all cells are filled
    for i in range(9):
        for j in range(9):
            assert 1 <= board[i][j] <= 9, f"Cell [{i}][{j}] should contain 1-9"
    
    # Verify no duplicates in rows
    for i in range(9):
        row_values = set(board[i])
        assert len(row_values) == 9, f"Row {i} should have 9 unique values"
    
    # Verify no duplicates in columns
    for j in range(9):
        col_values = set(board[i][j] for i in range(9))
        assert len(col_values) == 9, f"Column {j} should have 9 unique values"
    
    # Verify no duplicates in 3x3 boxes
    for box_row in range(3):
        for box_col in range(3):
            box_values = []
            for i in range(box_row * 3, box_row * 3 + 3):
                for j in range(box_col * 3, box_col * 3 + 3):
                    box_values.append(board[i][j])
            assert len(set(box_values)) == 9, f"Box [{box_row}][{box_col}] should have 9 unique values"