/**
 * @file game.h
 * @brief Contains the declaration of the Game class.
 */

#ifndef GAME_H
#define GAME_H

#include <random>
#include <SDL.h>
#include "controller.h"
#include "renderer.h"
#include "snake.h"

/**
 * @class Game
 * @brief Represents the game logic and state.
 */
class Game {
 public:

  /**
   * @brief Constructs a Game object with the specified grid width and height.
   * 
   * @param grid_width The width of the game grid.
   * @param grid_height The height of the game grid.
   */
  Game(std::size_t grid_width, std::size_t grid_height);

  /**
   * Runs the game loop.
   * 
   * @param controller The controller object used to handle user input.
   * @param renderer The renderer object used to render the game.
   * @param target_frame_duration The target duration of each frame in milliseconds.
   */
  void Run(Controller const &controller, Renderer &renderer,
           std::size_t target_frame_duration);
  
  /**
   * Returns the current score of the game.
   *
   * @return The current score of the game.
   */
  int GetScore() const;

  /**
   * @brief Returns the size of the game.
   * 
   * @return int The size of the game.
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

  /**
   * @brief Places a new food item on the game grid.
   * 
   */
  void PlaceFood();

  /**
   * @brief Updates the state of the game.
   * 
   */
  void Update();
};

#endif