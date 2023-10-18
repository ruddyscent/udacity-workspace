#ifndef CONTROLLER_H
#define CONTROLLER_H

#include "snake.h"

class Controller {
 public:

/*
**Function Name:** `Controller::ChangeDirection`

**Function Signature:** `void Controller::ChangeDirection(Snake &snake, Snake::Direction input, Snake::Direction opposite) const`

**Function Description:**

This function is a member function of the `Controller` class that changes the direction of the `Snake` object passed as a parameter based on the input direction and the opposite direction. If the current direction of the snake is not opposite to the input direction or the size of the snake is 1, the direction of the snake is changed to the input direction.

**Parameters:**

- `snake`: A reference to a `Snake` object that represents the snake to change the direction of.
- `input`: A `Snake::Direction` value that represents the input direction to change the snake's direction to.
- `opposite`: A `Snake::Direction` value that represents the opposite direction to the input direction.

**Return Value:**

This function does not return a value.

**Example Usage:**

```cpp
Snake snake;
Controller controller;
controller.ChangeDirection(snake, Snake::Direction::kUp, Snake::Direction::kDown);
```

In this example, the direction of the `snake` object is changed to `Snake::Direction::kUp` if the current direction is not `Snake::Direction::kDown` or the size of the snake is 1.
*/
  void HandleInput(bool &running, Snake &snake) const;

 private:

/*
**Function Name:** `Controller::HandleInput`

**Function Signature:** `void Controller::HandleInput(bool &running, Snake &snake) const`

**Function Description:**

This function is a member function of the `Controller` class that handles the input events for the game. It takes a reference to a boolean variable `running` and a reference to a `Snake` object as parameters. If the input event is `SDL_QUIT`, the `running` variable is set to `false`. If the input event is `SDL_KEYDOWN`, the direction of the `Snake` object is changed based on the key pressed.

**Parameters:**

- `running`: A reference to a boolean variable that represents whether the game is running or not.
- `snake`: A reference to a `Snake` object that represents the snake to change the direction of.

**Return Value:**

This function does not return a value.

**Example Usage:**

```cpp
bool running = true;
Snake snake;
Controller controller;
while (running) {
  controller.HandleInput(running, snake);
  // ...
}
```

In this example, the `HandleInput` function is called in a loop to handle the input events for the game. If the `running` variable is set to `false`, the loop will exit and the game will stop.
*/
  void ChangeDirection(Snake &snake, Snake::Direction input,
                       Snake::Direction opposite) const;
};

#endif