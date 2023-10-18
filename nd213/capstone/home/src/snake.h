#ifndef SNAKE_H
#define SNAKE_H

#include <vector>
#include <SDL.h>

class Snake {
 public:
  enum class Direction { kUp, kDown, kLeft, kRight };

/*
**Function Name:** `Snake::Snake`

**Function Signature:** `Snake::Snake(int grid_width, int grid_height)`

**Function Description:**

This is the constructor of the `Snake` class that initializes a new `Snake` object with the given `grid_width` and `grid_height` parameters. It creates a new `SDL_Point` object for the head of the snake and initializes the body of the snake with three `SDL_Point` objects representing the initial position of the snake.

**Parameters:**

- `grid_width`: An integer value that represents the width of the game grid.
- `grid_height`: An integer value that represents the height of the game grid.

**Return Value:**

This function does not return a value.

**Example Usage:**

```cpp
Snake snake(20, 20);
```

In this example, a new `Snake` object is created with a grid size of 20x20.
*/
  Snake(int grid_width, int grid_height)
      : grid_width(grid_width),
        grid_height(grid_height),
        head_x(grid_width / 2),
        head_y(grid_height / 2) {}

/*
**Function Name:** `Snake::Update`

**Function Signature:** `void Snake::Update()`

**Function Description:**

This function is a member function of the `Snake` class that updates the position of the snake based on its current direction and speed. It moves the head of the snake in the direction of the current direction and adds a new `SDL_Point` object to the front of the snake's body to represent the new position of the head. If the snake has not grown, the last `SDL_Point` object in the body is removed to represent the movement of the tail.

**Parameters:**

This function does not take any parameters.

**Return Value:**

This function does not return a value.

**Example Usage:**

```cpp
Snake snake(20, 20);
snake.Update();
```

In this example, a new `Snake` object is created, and the `Update` function is called to update the position of the snake.
*/
  void Update();

/*
**Function Name:** `Snake::GrowBody`

**Function Signature:** `void Snake::GrowBody()`

**Function Description:**

This function is a member function of the `Snake` class that increases the size of the snake by adding a new `SDL_Point` object to the front of the snake's body to represent the new position of the head.

**Parameters:**

This function does not take any parameters.

**Return Value:**

This function does not return a value.

**Example Usage:**

```cpp
Snake snake(20, 20);
snake.GrowBody();
```

In this example, a new `Snake` object is created, and the `GrowBody` function is called to increase the size of the snake.
*/
  void GrowBody();

/*
**Function Name:** `Snake::SnakeCell`

**Function Signature:** `bool Snake::SnakeCell(int x, int y)`

**Function Description:**

This function is a member function of the `Snake` class that checks if the given `x` and `y` coordinates are part of the snake's body.

**Parameters:**

- `x`: An integer value that represents the x-coordinate to check.
- `y`: An integer value that represents the y-coordinate to check.

**Return Value:**

This function returns a boolean value that represents whether the given coordinates are part of the snake's body (`true`) or not (`false`).

**Example Usage:**

```cpp
Snake snake(20, 20);
bool is_snake_cell = snake.SnakeCell(10, 10);
```

In this example, a new `Snake` object is created, and the `SnakeCell` function is called to check if the coordinates (10, 10) are part of the snake's body. The result is stored in the `is_snake_cell` variable.
*/
  bool SnakeCell(int x, int y);

  Direction direction = Direction::kUp;

  float speed{0.1f};
  int size{1};
  bool alive{true};
  float head_x;
  float head_y;
  std::vector<SDL_Point> body;

 private:
  void UpdateHead();
  void UpdateBody(SDL_Point &current_cell, SDL_Point &prev_cell);

  bool growing{false};
  int grid_width;
  int grid_height;
};

#endif