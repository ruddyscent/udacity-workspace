/**
 * @file snake.h
 * @brief Contains the declaration of the Snake class.
 */

#ifndef SNAKE_H
#define SNAKE_H

#include "entity.h"
#include <vector>
#include <SDL.h>

/**
 * @class Snake
 * @brief Represents the snake in the game.
 * 
 * The Snake class contains the state and behavior of the snake in the game.
 */
class Snake : public Entity {
 public:
  enum class Direction { kUp, kDown, kLeft, kRight };

  /**
   * @brief The constructor for the Snake class.
   * 
   * @param grid_width The width of the game grid.
   * @param grid_height The height of the game grid.
   */
  Snake(int grid_width, int grid_height)
      : grid_width(grid_width),
        grid_height(grid_height),
        head_x(grid_width / 2),
        head_y(grid_height / 2) {}

  /**
   * @brief Updates the state of the snake.
   * 
   */
  void Update();

  /**
   * @brief Increases the size of the snake's body by one unit.
   * 
   */
  void GrowBody();

  /**
   * @brief Checks if the given coordinates correspond to a cell occupied by the snake.
   * 
   * @param x The x-coordinate of the cell to check.
   * @param y The y-coordinate of the cell to check.
   * @return true if the cell is occupied by the snake, false otherwise.
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

  /**
   * @brief Updates the position of the snake's head.
   * 
   */
  void UpdateHead();
 
  /**
   * @brief Updates the position of the snake's body.
   * 
   * @param current_cell The current position of the snake's head.
   * @param prev_cell The previous position of the snake's head.
   */
  void UpdateBody(SDL_Point &current_cell, SDL_Point &prev_cell);

  bool growing{false};
  int grid_width;
  int grid_height;
};

#endif