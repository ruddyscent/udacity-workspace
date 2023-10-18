#ifndef RENDERER_H
#define RENDERER_H

#include <vector>
#include <SDL.h>
#include "snake.h"

class Renderer {
 public:
 /*
**Function Name:** `Renderer::Renderer`

**Function Signature:** `Renderer::Renderer(const std::size_t screen_width, const std::size_t screen_height, const std::size_t grid_width, const std::size_t grid_height)`

**Function Description:**

This is the constructor of the `Renderer` class that initializes a new `Renderer` object with the given `screen_width`, `screen_height`, `grid_width`, and `grid_height` parameters. It creates a new SDL window and renderer objects and sets the background color of the renderer to black.

**Parameters:**

- `screen_width`: A `std::size_t` value that represents the width of the game screen.
- `screen_height`: A `std::size_t` value that represents the height of the game screen.
- `grid_width`: A `std::size_t` value that represents the width of the game grid.
- `grid_height`: A `std::size_t` value that represents the height of the game grid.

**Return Value:**

This function does not return a value.

**Example Usage:**

```cpp
Renderer renderer(640, 480, 20, 20);
```

In this example, a new `Renderer` object is created with a screen size of 640x480 and a grid size of 20x20.
 */
  Renderer(const std::size_t screen_width, const std::size_t screen_height,
           const std::size_t grid_width, const std::size_t grid_height);

/*
**Function Name:** `Renderer::~Renderer`

**Function Signature:** `Renderer::~Renderer()`

**Function Description:**

This is the destructor of the `Renderer` class that frees the SDL window and renderer objects.

**Parameters:**

This function does not take any parameters.

**Return Value:**

This function does not return a value.

**Example Usage:**

```cpp
Renderer renderer(640, 480, 20, 20);
// Use the renderer object
...
// Destroy the renderer object
renderer.~Renderer();
```

In this example, a new `Renderer` object is created, used, and then destroyed using the destructor.
*/
  ~Renderer();

/*
**Function Name:** `Renderer::Render`

**Function Signature:** `void Renderer::Render(Snake const snake, SDL_Point const &food)`

**Function Description:**

This function is a member function of the `Renderer` class that renders the current state of the game to the SDL window. It takes a `Snake` object and an `SDL_Point` object representing the position of the food as parameters. It first clears the renderer with the background color, then renders the snake and food to the renderer, and finally presents the renderer to the SDL window.

**Parameters:**

- `snake`: A constant reference to a `Snake` object that represents the current state of the snake in the game.
- `food`: A constant reference to an `SDL_Point` object that represents the position of the food in the game.

**Return Value:**

This function does not return a value.

**Example Usage:**

```cpp
Renderer renderer(640, 480, 20, 20);
Snake snake(20, 20);
SDL_Point food = {10, 10};
renderer.Render(snake, food);
```

In this example, a new `Renderer` object, a `Snake` object, and an `SDL_Point` object representing the position of the food are created, and the `Render` function is called to render the current state of the game to the SDL window.
*/
  void Render(Snake const snake, SDL_Point const &food);

/*
**Function Name:** `Renderer::UpdateWindowTitle`

**Function Signature:** `void Renderer::UpdateWindowTitle(int score, int fps)`

**Function Description:**

This function is a member function of the `Renderer` class that updates the title of the SDL window with the current score and frame rate of the game.

**Parameters:**

- `score`: An integer value that represents the current score of the game.
- `fps`: An integer value that represents the current frame rate of the game.

**Return Value:**

This function does not return a value.

**Example Usage:**

```cpp
Renderer renderer(640, 480, 20, 20);
int score = 0;
int fps = 60;
renderer.UpdateWindowTitle(score, fps);
```

In this example, a new `Renderer` object is created, and the `UpdateWindowTitle` function is called to update the title of the SDL window with the current score and frame rate of the game.
*/
  void UpdateWindowTitle(int score, int fps);

 private:
  SDL_Window *sdl_window;
  SDL_Renderer *sdl_renderer;

  const std::size_t screen_width;
  const std::size_t screen_height;
  const std::size_t grid_width;
  const std::size_t grid_height;
};

#endif