#ifndef GAME_H
#define GAME_H

#include <random>
#include <SDL.h>
#include "controller.h"
#include "renderer.h"
#include "snake.h"

class Game {
 public:

/*
**Function Name:** `Game::Game`

**Function Signature:** `Game::Game(std::size_t grid_width, std::size_t grid_height)`

**Function Description:**

This is the constructor of the `Game` class that initializes a new `Game` object with the given `grid_width` and `grid_height` parameters. It creates a new `Snake` object and initializes the random number generator for placing the food.

**Parameters:**

- `grid_width`: A `std::size_t` value that represents the width of the game grid.
- `grid_height`: A `std::size_t` value that represents the height of the game grid.

**Return Value:**

This function does not return a value.

**Example Usage:**

```cpp
Game game(20, 20);
```

In this example, a new `Game` object is created with a grid size of 20x20.
*/
  Game(std::size_t grid_width, std::size_t grid_height);

/*
**Function Name:** `Game::Run`

**Function Signature:** `void Game::Run(Controller const &controller, Renderer &renderer, std::size_t target_frame_duration)`

**Function Description:**

This function runs the game loop and updates the game state on each iteration. It takes a `Controller` object, a `Renderer` object, and a `std::size_t` value as parameters. The `Controller` object is used to handle the input events, the `Renderer` object is used to render the game, and the `target_frame_duration` value is used to control the frame rate of the game.

On each iteration of the game loop, the `Controller` object is used to handle the input events, the `Snake` object is updated based on the current direction, the collision detection is performed to check if the snake has collided with the wall or itself, and the food is checked to see if the snake has eaten it. If the snake has eaten the food, a new food is placed randomly on the game grid and the score is updated.

The game loop continues until the snake collides with the wall or itself, at which point the game is over and the score is displayed.

**Parameters:**

- `controller`: A constant reference to a `Controller` object that is used to handle the input events for the game.
- `renderer`: A reference to a `Renderer` object that is used to render the game.
- `target_frame_duration`: A `std::size_t` value that represents the target frame duration for the game loop.

**Return Value:**

This function does not return a value.

**Example Usage:**

```cpp
Controller controller;
Renderer renderer;
Game game(20, 20);
game.Run(controller, renderer, 1000 / 60);
```

In this example, a `Controller` object, a `Renderer` object, and a `Game` object are created, and the `Run` function is called to start the game loop with a target frame rate of 60 frames per second.
*/
  void Run(Controller const &controller, Renderer &renderer,
           std::size_t target_frame_duration);

/*
**Function Name:** `Game::GetScore`

**Function Signature:** `int Game::GetScore() const`

**Function Description:**

This function is a member function of the `Game` class that returns the current score of the game.

**Parameters:**

This function does not take any parameters.

**Return Value:**

This function returns an integer value that represents the current score of the game.

**Example Usage:**

```cpp
Game game(20, 20);
int score = game.GetScore();
```

In this example, a new `Game` object is created, and the `GetScore` function is called to get the current score of the game.
*/
  int GetScore() const;

/*
**Function Name:** `Game::GetSize`

**Function Signature:** `int Game::GetSize() const`

**Function Description:**

This function is a member function of the `Game` class that returns the current size of the snake.

**Parameters:**

This function does not take any parameters.

**Return Value:**

This function returns an integer value that represents the current size of the snake.

**Example Usage:**

```cpp
Game game(20, 20);
int size = game.GetSize();
```

In this example, a new `Game` object is created, and the `GetSize` function is called to get the current size of the snake.
*/
  int GetSize() const;

 private:
  Snake snake;
  SDL_Point food;

  std::random_device dev;
  std::mt19937 engine;
  std::uniform_int_distribution<int> random_w;
  std::uniform_int_distribution<int> random_h;

  int score{0};

/*
**Function Name:** `Game::PlaceFood`

**Function Signature:** `void Game::PlaceFood()`

**Function Description:**

This is a member function of the `Game` class that places a new food item at a random location on the game grid. It generates random `x` and `y` coordinates within the bounds of the game grid and checks if the location is not already occupied by the snake. If the location is valid, it sets the `food` member variable to the new location.

**Parameters:**

This function does not take any parameters.

**Return Value:**

This function does not return a value.

**Example Usage:**

```cpp
Game game(20, 20);
game.PlaceFood();
```

In this example, a new `Game` object is created, and the `PlaceFood` function is called to place a new food item on the game grid.
*/
  void PlaceFood();

/*
**Function Name:** `Game::Update`

**Function Signature:** `void Game::Update()`

**Function Description:**

This is a member function of the `Game` class that updates the state of the game. It first updates the position of the snake using the `Update` function of the `Snake` class. It then checks if the snake has collided with the game boundaries or with itself. If the snake has collided, the game is over, and the score is reset to zero. If the snake has collided with the food, the score is increased, and a new food item is placed on the game grid using the `PlaceFood` function.

**Parameters:**

This function does not take any parameters.

**Return Value:**

This function does not return a value.

**Example Usage:**

```cpp
Game game(20, 20);
game.Update();
```

In this example, a new `Game` object is created, and the `Update` function is called to update the state of the game.
*/
  void Update();
};

#endif