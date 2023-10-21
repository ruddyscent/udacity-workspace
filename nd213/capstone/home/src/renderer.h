/**
 * @file renderer.h
 * @brief Contains the declaration of the Renderer class.
 */

#ifndef RENDERER_H
#define RENDERER_H

#include <vector>
#include <SDL2/SDL.h>
#include "snake.h"

/**
 * @brief The Renderer class is responsible for rendering the game on the screen.
 * 
 */
class Renderer {
 public:
  
  /**
   * @brief Constructs a Renderer object with the given screen and grid dimensions.
   * 
   * @param screen_width The width of the screen in pixels.
   * @param screen_height The height of the screen in pixels.
   * @param grid_width The width of the grid in cells.
   * @param grid_height The height of the grid in cells.
   */
  Renderer(const std::size_t screen_width, const std::size_t screen_height,
           const std::size_t grid_width, const std::size_t grid_height);

  /**
   * @brief Destructor for the Renderer class.
   * 
   */
  ~Renderer();

  /**
   * @brief Renders the snake and food on the screen.
   * 
   * @param snake The Snake object to be rendered.
   * @param food The food object to be rendered.
   */
  void Render(Snake const &snake, SDL_Point const &food, SDL_Point const &poison);

  /**
   * @brief Updates the window title with the current score and fps.
   * 
   * @param score The current score.
   * @param fps The current fps.
   */
  void UpdateWindowTitle(int score, int fps);

 private:
  SDL_Window *sdl_window; /* The SDL window. */
  SDL_Renderer *sdl_renderer; /* The SDL renderer. */

  const std::size_t screen_width; /* The width of the screen in pixels. */
  const std::size_t screen_height; /* The height of the screen in pixels. */
  const std::size_t grid_width; /* The width of the grid in cells. */
  const std::size_t grid_height; /* The height of the grid in cells. */
};

#endif