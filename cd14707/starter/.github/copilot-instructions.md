Project: Flask Sudoku (starter)

Purpose: concise guidance for AI coding agents working on this small Flask + JS Sudoku app.

**Big Picture**
- **App server**: [app.py](app.py) is a tiny Flask app exposing two JSON endpoints and serving the UI.
- **Game logic**: [sudoku_logic.py](sudoku_logic.py) generates and checks puzzles (backtracking generator).
- **Client**: [templates/index.html](templates/index.html) + [static/main.js](static/main.js) render the board and call the API.

The app keeps a single in-memory game (global `CURRENT` in [app.py](app.py)). This is a single-process demo — state is not persisted and will be lost on restart. Avoid assuming multi-worker safety when changing state handling.

**Key files & patterns**
- [app.py](app.py): routes
  - `GET /new?clues=<n>` -> returns `{puzzle: [[...]]}` and sets `CURRENT['solution']`.
  - `POST /check` -> accepts JSON `{board: [[...]]}` and returns `{incorrect: [[r,c], ...]}` or `{'error': ...}`.
  - `CURRENT` is the ephemeral store for the puzzle and solution.
- [sudoku_logic.py](sudoku_logic.py): core helpers
  - constants: `SIZE = 9`, `EMPTY = 0`.
  - `generate_puzzle(clues=35)` -> `(puzzle, solution)` where both are 9x9 lists of ints; `0` means empty.
  - `fill_board` uses randomized backtracking; `remove_cells` mutates the board to create clues.
  - `deep_copy` is used to snapshot the solution before removal.
- [static/main.js](static/main.js): client expectations
  - Expects puzzle JSON as nested lists of integers, using `0` for empty cells.
  - Renders inputs where prefilled cells are `disabled` and get `prefilled` class; incorrect cells get `incorrect` class.

**Data shapes and conventions (explicit)**
- Puzzle/board: a 9x9 nested list/array of integers, 1-9 for filled cells, `0` for empty.
- Frontend input handling: single-character inputs, sanitized to digits `1-9` on input (see `main.js`).

**Dev / Run / Debug workflows**
- Install deps: `pip install -r requirements.txt` (single dependency: Flask>=2.0 from `requirements.txt`).
- Run locally: `python app.py` — the app calls `app.run(debug=True)` so it starts in debug mode and logs to stdout.
- Browser UI: open `http://127.0.0.1:5000/` after starting the server.
- Reproducibility: puzzle generation uses `random`. Tests or deterministic seeds are not present; set `random.seed(...)` in `sudoku_logic.py` for deterministic behavior during debugging.

**Common change patterns and gotchas**
- If you change the response shape of `/new` or `/check`, update `static/main.js` accordingly — it tightly couples to the current JSON shapes.
- `CURRENT` is process-local. To support concurrent users or background workers, replace the in-memory store with per-session storage or a small DB and avoid relying on `CURRENT`.
- `remove_cells` mutates the board in place; callers should deep-copy if they need the original.
- The generator is randomized and may be slow for extreme `clues` values; avoid tight loops in tests that repeatedly call `generate_puzzle` without seeding.

**Minimal examples**
- Example: fetch a new puzzle (client uses this): `GET /new` -> `{puzzle: [[0,5, ...], ...]}` (see [app.py](app.py#L11-L23)).
- Example: check board payload (client sends): `POST /check` JSON body `{ "board": [[...], ...] }` and receives `{ "incorrect": [[0,1], [8,8]] }`.

If anything here is unclear or you want more examples (tests, CI config, or making generation deterministic), tell me which area to expand and I'll update this file.
