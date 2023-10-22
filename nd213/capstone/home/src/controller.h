/**
 * @file controller.h
 * @brief Defines the Controller class and its member functions.
 */

#ifndef CONTROLLER_H
#define CONTROLLER_H

#include "snake.h"

/**
 * @brief The Controller class handles user input to control the snake's movement.
 */
class Controller {
 public:

  /**
   * @brief Handles user input to control the snake's movement.
   * 
   * @param running A boolean reference indicating whether the game is running or not.
   * @param snake A reference to the Snake object that needs to be controlled.
   */
  void HandleInput(bool &running, Snake &snake) const;

 private:

  /**
   * @brief Changes the direction of the snake.
   * 
   * @param snake A reference to the Snake object that needs to be controlled.
   * @param input The direction to change to.
   * @param opposite The opposite direction of the current direction.
   */
  void ChangeDirection(Snake &snake, Snake::Direction input,
                       Snake::Direction opposite) const;
};

#endif