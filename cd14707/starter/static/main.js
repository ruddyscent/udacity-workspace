// Client-side rendering and interaction for the Flask-backed Sudoku
const SIZE = 9;
let puzzle = [];
let timerInterval = null;
let elapsedSeconds = 0;
let hintsUsed = 0;

const DIFFICULTY_TO_CLUES = {
  easy: 45,
  medium: 35,
  hard: 25
};

function createBoardElement() {
  const boardDiv = document.getElementById('sudoku-board');
  boardDiv.innerHTML = '';
  for (let i = 0; i < SIZE; i++) {
    const rowDiv = document.createElement('div');
    rowDiv.className = 'sudoku-row';
    for (let j = 0; j < SIZE; j++) {
      const input = document.createElement('input');
      input.type = 'text';
      input.maxLength = 1;
      // Assign base cell class and a 3x3-box parity class to allow
      // alternating 3x3 block colors without layout shifts.
      const boxRow = Math.floor(i / 3);
      const boxCol = Math.floor(j / 3);
      const boxParity = (boxRow + boxCol) % 2 === 0 ? 'box-a' : 'box-b';
      input.className = 'sudoku-cell ' + boxParity;
      input.dataset.row = i;
      input.dataset.col = j;
      input.addEventListener('input', (e) => {
        const val = e.target.value.replace(/[^1-9]/g, '');
        e.target.value = val;
        // Immediate feedback: check for conflicts
        checkConflicts();
      });
      rowDiv.appendChild(input);
    }
    boardDiv.appendChild(rowDiv);
  }
}

function renderPuzzle(puz) {
  puzzle = puz;
  createBoardElement();
  const boardDiv = document.getElementById('sudoku-board');
  const inputs = boardDiv.getElementsByTagName('input');
  for (let i = 0; i < SIZE; i++) {
    for (let j = 0; j < SIZE; j++) {
      const idx = i * SIZE + j;
      const val = puzzle[i][j];
      const inp = inputs[idx];
      if (val !== 0) {
        inp.value = val;
        inp.disabled = true;
        inp.classList.add('prefilled');
      } else {
        inp.value = '';
        inp.disabled = false;
      }
    }
  }
}

async function newGame() {
  // Read difficulty and map to number of clues
  const diff = document.getElementById('difficulty').value;
  const clues = DIFFICULTY_TO_CLUES[diff] || 35;
  const res = await fetch('/new?clues=' + clues);
  const data = await res.json();
  renderPuzzle(data.puzzle);
  document.getElementById('message').innerText = '';
  // Reset timer and hints
  resetTimer();
  startTimer();
  hintsUsed = 0;
  document.getElementById('hints-used').innerText = 'Hints: 0';
}

async function checkSolution() {
  const boardDiv = document.getElementById('sudoku-board');
  const inputs = boardDiv.getElementsByTagName('input');
  const board = [];
  for (let i = 0; i < SIZE; i++) {
    board[i] = [];
    for (let j = 0; j < SIZE; j++) {
      const idx = i * SIZE + j;
      const val = inputs[idx].value;
      board[i][j] = val ? parseInt(val, 10) : 0;
    }
  }
  const res = await fetch('/check', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({board})
  });
  const data = await res.json();
  const msg = document.getElementById('message');
  if (data.error) {
    msg.style.color = '#d32f2f';
    msg.innerText = data.error;
    return;
  }
  const incorrect = new Set(data.incorrect.map(x => x[0]*SIZE + x[1]));
  for (let idx = 0; idx < inputs.length; idx++) {
    const inp = inputs[idx];
    if (inp.disabled) continue;
    // preserve box-a/box-b classes and only toggle the incorrect marker
    inp.classList.remove('incorrect', 'conflict');
    if (incorrect.has(idx)) {
      inp.classList.add('incorrect');
    }
  }
  if (incorrect.size === 0) {
    stopTimer();
    msg.style.color = '#388e3c';
    msg.innerText = 'Congratulations! You solved it!';
    // Ask for name and record score
    const name = prompt('Enter your name for the scoreboard (leave empty to skip)');
    if (name) {
      const difficulty = document.getElementById('difficulty').value;
      const record = {
        name: name,
        time: elapsedSeconds,
        level: difficulty,
        hints: hintsUsed,
        when: Date.now()
      };
      addTopRecord(record);
      renderTop10();
    }
  } else {
    msg.style.color = '#d32f2f';
    msg.innerText = 'Some cells are incorrect.';
  }
}


async function requestHint() {
  const boardDiv = document.getElementById('sudoku-board');
  const inputs = boardDiv.getElementsByTagName('input');
  const board = [];
  for (let i = 0; i < SIZE; i++) {
    board[i] = [];
    for (let j = 0; j < SIZE; j++) {
      const idx = i * SIZE + j;
      const val = inputs[idx].value;
      board[i][j] = val ? parseInt(val, 10) : 0;
    }
  }
  const res = await fetch('/hint', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({board})
  });
  const data = await res.json();
  if (data.hint) {
    const [r, c, val] = data.hint;
    const idx = r * SIZE + c;
    const inp = document.getElementById('sudoku-board').getElementsByTagName('input')[idx];
    inp.value = val;
    inp.disabled = true;
    inp.classList.add('prefilled', 'hinted');
    hintsUsed += 1;
    document.getElementById('hints-used').innerText = 'Hints: ' + hintsUsed;
  } else if (data.error) {
    const msg = document.getElementById('message');
    msg.style.color = '#d32f2f';
    msg.innerText = data.error;
  }
}


function startTimer() {
  stopTimer();
  elapsedSeconds = 0;
  timerInterval = setInterval(() => {
    elapsedSeconds += 1;
    document.getElementById('timer').innerText = 'Time: ' + formatTime(elapsedSeconds);
  }, 1000);
}

function stopTimer() {
  if (timerInterval) {
    clearInterval(timerInterval);
    timerInterval = null;
  }
}

function resetTimer() {
  stopTimer();
  elapsedSeconds = 0;
  document.getElementById('timer').innerText = 'Time: 00:00';
}

function formatTime(sec) {
  const m = Math.floor(sec / 60).toString().padStart(2, '0');
  const s = (sec % 60).toString().padStart(2, '0');
  return m + ':' + s;
}

// Check for conflicts (Sudoku rule violations)
function checkConflicts() {
  const boardDiv = document.getElementById('sudoku-board');
  const inputs = boardDiv.getElementsByTagName('input');
  
  // Build current board state
  const board = [];
  for (let i = 0; i < SIZE; i++) {
    board[i] = [];
    for (let j = 0; j < SIZE; j++) {
      const idx = i * SIZE + j;
      const val = inputs[idx].value;
      board[i][j] = val ? parseInt(val, 10) : 0;
    }
  }
  
  // Check each cell for conflicts
  for (let idx = 0; idx < inputs.length; idx++) {
    const inp = inputs[idx];
    if (inp.disabled || !inp.value) {
      inp.classList.remove('conflict');
      continue;
    }
    
    const row = parseInt(inp.dataset.row);
    const col = parseInt(inp.dataset.col);
    const num = board[row][col];
    
    let hasConflict = false;
    
    // Check row for duplicates
    for (let c = 0; c < SIZE; c++) {
      if (c !== col && board[row][c] === num) {
        hasConflict = true;
        break;
      }
    }
    
    // Check column for duplicates
    if (!hasConflict) {
      for (let r = 0; r < SIZE; r++) {
        if (r !== row && board[r][col] === num) {
          hasConflict = true;
          break;
        }
      }
    }
    
    // Check 3x3 box for duplicates
    if (!hasConflict) {
      const boxRow = Math.floor(row / 3) * 3;
      const boxCol = Math.floor(col / 3) * 3;
      for (let r = boxRow; r < boxRow + 3; r++) {
        for (let c = boxCol; c < boxCol + 3; c++) {
          if ((r !== row || c !== col) && board[r][c] === num) {
            hasConflict = true;
            break;
          }
        }
        if (hasConflict) break;
      }
    }
    
    if (hasConflict) {
      inp.classList.add('conflict');
    } else {
      inp.classList.remove('conflict');
    }
  }
}

// Top-10 scoreboard in localStorage
function loadTop10() {
  const raw = localStorage.getItem('sudoku_top10');
  return raw ? JSON.parse(raw) : [];
}

function saveTop10(arr) {
  localStorage.setItem('sudoku_top10', JSON.stringify(arr));
}

function addTopRecord(rec) {
  const arr = loadTop10();
  arr.push(rec);
  arr.sort((a,b) => a.time - b.time);
  const top = arr.slice(0, 10);
  saveTop10(top);
}

function renderTop10() {
  const container = document.getElementById('scoreboard');
  const arr = loadTop10();
  if (arr.length === 0) {
    container.innerHTML = '<p>No records yet.</p>';
    return;
  }
  let html = '<table class="scoreboard-table"><tr><th>#</th><th>Name</th><th>Time</th><th>Level</th><th>Hints</th></tr>';
  arr.forEach((r, i) => {
    html += `<tr><td>${i+1}</td><td>${escapeHtml(r.name)}</td><td>${formatTime(r.time)}</td><td>${r.level}</td><td>${r.hints}</td></tr>`;
  });
  html += '</table>';
  container.innerHTML = html;
}

function escapeHtml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

// Wire buttons
window.addEventListener('load', () => {
  document.getElementById('new-game').addEventListener('click', newGame);
  document.getElementById('check-solution').addEventListener('click', checkSolution);
  document.getElementById('hint').addEventListener('click', requestHint);
  // initialize
  newGame();
  renderTop10();
  // Theme initialization
  initTheme();
  const themeSelect = document.getElementById('theme-select');
  if (themeSelect) {
    themeSelect.addEventListener('change', (e) => {
      setThemePreference(e.target.value);
    });
  }
});

function initTheme() {
  const saved = localStorage.getItem('sudoku_theme') || 'system';
  const select = document.getElementById('theme-select');
  if (select) select.value = saved;
  applyTheme(saved);
  if (saved === 'system' && window.matchMedia) {
    const mq = window.matchMedia('(prefers-color-scheme: dark)');
    mq.addEventListener && mq.addEventListener('change', () => applyTheme('system'));
  }
}

function setThemePreference(pref) {
  localStorage.setItem('sudoku_theme', pref);
  applyTheme(pref);
}

function applyTheme(pref) {
  let theme = pref;
  if (pref === 'system') {
    const dark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    theme = dark ? 'dark' : 'light';
  }
  if (theme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
  }
}