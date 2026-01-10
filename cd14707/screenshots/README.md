# Screenshots – GitHub Copilot Usage Evidence

This folder contains screenshots documenting how GitHub Copilot was used **responsibly and effectively** across key milestones of the Sudoku project.

Each screenshot is labeled descriptively and paired with an explanation of:
- The prompt given to Copilot
- Copilot’s suggestion
- How the suggestion was reviewed, accepted, modified, or rejected
- How the final result satisfies the project rubric

---

## 1. Setting Up the Testing Framework

**Screenshot:** `settign-up-framework.png`

**Description:**
I used GitHub Copilot to assist in setting up the initial testing framework with `pytest`. Copilot suggested a basic test structure, including how to initialize the Flask test client and validate API responses.

I reviewed the generated code and adjusted import paths to ensure the project root was correctly added to `sys.path`, resolving module import errors that Copilot’s initial suggestion did not handle.

This demonstrates responsible use by validating and correcting Copilot-generated test setup code.

---

## 2. Ensuring the Sudoku Board Has One Unique Solution

**Screenshot:** `one-unique-solution.png`

**Description:**
I asked Copilot to help implement logic for generating a Sudoku puzzle with a unique solution. Copilot initially suggested returning the first generated puzzle after removing cells.

After reviewing this approach, I identified that it did not guarantee uniqueness. I modified the logic to retry puzzle generation multiple times and fall back only after a defined number of attempts.

This step shows critical evaluation of Copilot’s suggestion and a correction to meet the project’s single-solution requirement.

---

## 3. Checking Top-10 Scores and Using localStorage

**Screenshot:** `checking-for-a-top-top-10-list.png`

**Description:**
Copilot was used to help design logic for managing a Top-10 scoreboard using `localStorage`. The suggestion included storing results as a JSON array and sorting them by completion time.

I reviewed the code, ensured only the top 10 records were retained, and verified correct serialization using `localStorage.setItem()` and `getItem()`.

This confirms correct usage of browser storage APIs and aligns with the project requirement.

---

## 4. Styling the 3×3 Sudoku Grid with Alternating Colors

**Screenshot:** `subgrid-color-alternation_result.png`

**Description:**
I prompted Copilot to help modify the CSS so that each 3×3 Sudoku sub-grid alternates in background color without causing layout shifts.

Copilot initially suggested row-based styling, which did not clearly distinguish 3×3 blocks. I rejected this approach and revised the CSS to apply styles based on 3×3 sub-grid positioning.

The final result:
- Clearly differentiates each 3×3 square
- Introduces no layout shifts
- Works consistently across themes

This directly satisfies the rubric requirement for alternating sub-grid colors.

---

## 5. Light and Dark Mode Accessibility

**Screenshots:**
- `dark-mode.png`
- `dark-mode-web.png`

**Description:**
Copilot assisted in refactoring CSS variables for light and dark themes. I reviewed the suggested color values and adjusted contrast levels to ensure text, buttons, and grid cells remain clearly visible in both modes.

This step confirms accessibility and visual clarity across themes.

---

## 6. Responsive Layout and Difficulty Selection

**Screenshots:**
- `difficulty-selector.png`
- `difficulty-selector-web.png`

**Description:**
Copilot was used to help structure responsive layout behavior for controls such as the difficulty selector. I verified that font sizes, spacing, and layout adapt cleanly between desktop and smaller screens without breaking the UI.

---

## 7. Copilot Instruction Refinement

**Screenshot:** `copilot-instructions_refined.png`

**Description:**
This screenshot documents updates made to the Copilot instruction file to guide consistent coding style, architecture boundaries, and responsible AI usage throughout the project.

It demonstrates intentional control over Copilot’s behavior rather than blind acceptance of generated output.

---

## References

- GitHub Copilot – Best Practices  
  https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot

- MDN Web Docs – CSS Grid Layout  
  https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout