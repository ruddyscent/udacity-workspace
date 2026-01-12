from flask import Flask, render_template, jsonify, request, Response
from typing import Dict, Optional, Any, List
import sudoku_logic

app = Flask(__name__)

# Board is a 9x9 nested list of ints; 0 represents an empty cell.
Board = List[List[int]]

# Keep a simple in-memory store for current puzzle and solution.
# This is process-local and not safe for multi-worker deployments.
CURRENT: Dict[str, Optional[Board]] = {
    'puzzle': None,
    'solution': None
}


@app.route('/')
def index() -> str:
    # Render the client UI
    return render_template('index.html')


@app.route('/new')
def new_game() -> Response:
    # `clues` indicates how many filled cells the returned puzzle should contain
    clues = int(request.args.get('clues', 35))
    puzzle, solution = sudoku_logic.generate_puzzle(clues)
    CURRENT['puzzle'] = puzzle
    CURRENT['solution'] = solution
    return jsonify({'puzzle': puzzle})


@app.route('/check', methods=['POST'])
def check_solution() -> Response:
    # Expect JSON body: { "board": [[...], ...] }
    data: Any = request.json
    board: Optional[Board] = data.get('board') if data else None
    solution: Optional[Board] = CURRENT.get('solution')
    if solution is None:
        return jsonify({'error': 'No game in progress'}), 400
    if board is None:
        return jsonify({'error': 'Missing board'}), 400
    # Compare submitted board against stored solution and report incorrect cells
    incorrect: List[List[int]] = []
    for i in range(sudoku_logic.SIZE):
        for j in range(sudoku_logic.SIZE):
            if board[i][j] != solution[i][j]:
                incorrect.append([i, j])
    return jsonify({'incorrect': incorrect})


@app.route('/hint', methods=['POST'])
def hint() -> Response:
    """Provide a single hint for the submitted board.

    Expects JSON { "board": [[...], ...] } and returns
    { "hint": [row, col, value] } indicating a cell where the
    submitted `board` differs from the stored solution. Returns
    400 if no game in progress or board missing.
    """
    data: Any = request.json
    board: Optional[Board] = data.get('board') if data else None
    solution: Optional[Board] = CURRENT.get('solution')
    if solution is None:
        return jsonify({'error': 'No game in progress'}), 400
    if board is None:
        return jsonify({'error': 'Missing board'}), 400
    for i in range(sudoku_logic.SIZE):
        for j in range(sudoku_logic.SIZE):
            if board[i][j] != solution[i][j]:
                return jsonify({'hint': [i, j, solution[i][j]]})
    return jsonify({'error': 'No hint available'}), 400


if __name__ == '__main__':
    app.run(debug=True)