import os
import sys
import random
from typing import Any, List

from flask.testing import FlaskClient

# Ensure repository root is on sys.path for imports (test runner working dir).
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app as flask_app


def test_new_endpoint_and_check_correct() -> None:
    """Request a new puzzle and verify the stored solution is accepted as correct.

    Uses Flask's test client to call `/new` and `/check` endpoints.
    """
    client: FlaskClient = flask_app.app.test_client()
    random.seed(0)  # deterministic puzzle for test

    res = client.get('/new')
    assert res.status_code == 200
    data: Any = res.get_json()
    assert 'puzzle' in data
    puzzle = data['puzzle']
    assert len(puzzle) == 9 and len(puzzle[0]) == 9

    # Use the server's stored solution to verify `/check` returns no incorrect cells
    solution: List[List[int]] = flask_app.CURRENT['solution']  # type: ignore[assignment]
    res2 = client.post('/check', json={'board': solution})
    assert res2.status_code == 200
    data2: Any = res2.get_json()
    assert 'incorrect' in data2
    assert data2['incorrect'] == []


def test_check_with_incorrect_cells_and_no_game() -> None:
    """Submit a board with at least one incorrect cell, then verify behavior when no game exists."""
    client: FlaskClient = flask_app.app.test_client()
    random.seed(2)
    client.get('/new')

    solution: List[List[int]] = flask_app.CURRENT['solution']  # type: ignore[assignment]
    # Make a shallow copy of rows and corrupt a single cell
    board: List[List[int]] = [row[:] for row in solution]
    board[0][0] = 1 if board[0][0] != 1 else 2

    res = client.post('/check', json={'board': board})
    data: Any = res.get_json()
    assert len(data['incorrect']) >= 1

    # Simulate no game in progress and assert `/check` responds with 400
    flask_app.CURRENT['solution'] = None
    res_no = client.post('/check', json={'board': board})
    assert res_no.status_code == 400
    data_no: Any = res_no.get_json()
    assert 'error' in data_no


def test_hint_endpoint_and_clues_count() -> None:
    """Test that `/hint` returns a valid hint and `/new?clues=` returns expected prefilled count."""
    client = flask_app.app.test_client()
    random.seed(4)
    # Create a new game with default clues
    res = client.get('/new')
    assert res.status_code == 200
    data = res.get_json()
    puzzle = data['puzzle']
    solution = flask_app.CURRENT['solution']

    # Request a hint using the current puzzle board (empty cells are 0)
    res_hint = client.post('/hint', json={'board': puzzle})
    assert res_hint.status_code == 200
    hint_data = res_hint.get_json()
    assert 'hint' in hint_data
    r, c, val = hint_data['hint']
    # Hint should match the stored solution and correspond to an empty cell in puzzle
    assert solution[r][c] == val
    assert puzzle[r][c] == 0

    # Simulate no game in progress
    flask_app.CURRENT['solution'] = None
    res_no = client.post('/hint', json={'board': puzzle})
    assert res_no.status_code == 400
    data_no = res_no.get_json()
    assert 'error' in data_no

    # Test that specifying clues returns that many filled cells
    res2 = client.get('/new?clues=40')
    assert res2.status_code == 200
    data2 = res2.get_json()
    puzzle40 = data2['puzzle']
    nonzeros = sum(1 for i in range(9) for j in range(9) if puzzle40[i][j] != 0)
    assert nonzeros == 40

def test_difficulty_levels() -> None:
    """Test that different difficulty levels return appropriate number of clues."""
    client = flask_app.app.test_client()
    
    difficulty_clues = {
        45: 'easy',    # Easy should have 45 clues
        35: 'medium',  # Medium should have 35 clues
        25: 'hard'     # Hard should have 25 clues
    }
    
    for expected_clues, difficulty in difficulty_clues.items():
        random.seed(10)
        res = client.get(f'/new?clues={expected_clues}')
        assert res.status_code == 200
        data = res.get_json()
        puzzle = data['puzzle']
        
        # Count non-zero cells (prefilled clues)
        actual_clues = sum(1 for i in range(9) for j in range(9) if puzzle[i][j] != 0)
        assert actual_clues == expected_clues, f"{difficulty} difficulty should have {expected_clues} clues, got {actual_clues}"


def test_check_returns_all_incorrect_cells() -> None:
    """Test that `/check` returns positions of all incorrect cells, not just the first one."""
    client = flask_app.app.test_client()
    random.seed(7)
    client.get('/new')
    
    solution = flask_app.CURRENT['solution']
    board = [row[:] for row in solution]
    
    # Corrupt multiple cells in different positions
    corrupted_positions = []
    if board[0][0] != 1:
        board[0][0] = 1
        corrupted_positions.append([0, 0])
    else:
        board[0][0] = 2
        corrupted_positions.append([0, 0])
    
    if board[4][4] != 5:
        board[4][4] = 5
        corrupted_positions.append([4, 4])
    else:
        board[4][4] = 1
        corrupted_positions.append([4, 4])
    
    if board[8][8] != 9:
        board[8][8] = 9
        corrupted_positions.append([8, 8])
    else:
        board[8][8] = 1
        corrupted_positions.append([8, 8])
    
    res = client.post('/check', json={'board': board})
    data = res.get_json()
    
    # Should return all incorrect cells
    assert len(data['incorrect']) >= 3, "Should detect multiple incorrect cells"
    incorrect_set = set(tuple(pos) for pos in data['incorrect'])
    
    for pos in corrupted_positions:
        assert tuple(pos) in incorrect_set, f"Position {pos} should be marked as incorrect"


def test_hint_provides_different_cells() -> None:
    """Test that requesting multiple hints provides different cells."""
    client = flask_app.app.test_client()
    random.seed(11)
    
    res = client.get('/new?clues=30')
    assert res.status_code == 200
    puzzle_data = res.get_json()
    puzzle = puzzle_data['puzzle']
    
    # Request multiple hints
    hints_received = []
    board = [row[:] for row in puzzle]
    
    for _ in range(3):
        res_hint = client.post('/hint', json={'board': board})
        if res_hint.status_code == 200:
            hint_data = res_hint.get_json()
            if 'hint' in hint_data:
                r, c, val = hint_data['hint']
                hints_received.append((r, c))
                # Apply hint to board for next request
                board[r][c] = val
    
    # Should have received hints for different cells
    assert len(hints_received) == len(set(hints_received)), "Hints should provide different cells"


def test_empty_board_returns_error() -> None:
    """Test that submitting a completely empty board is handled gracefully."""
    client = flask_app.app.test_client()
    random.seed(12)
    client.get('/new')
    
    empty_board = [[0 for _ in range(9)] for _ in range(9)]
    
    res = client.post('/check', json={'board': empty_board})
    assert res.status_code == 200
    data = res.get_json()
    
    # Should indicate multiple incorrect cells (all empty cells)
    assert 'incorrect' in data
    assert len(data['incorrect']) > 0