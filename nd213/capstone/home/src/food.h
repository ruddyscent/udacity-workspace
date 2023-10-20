#ifndef FOOD_H
#define FOOD_H

#include "entity.h"

class Food : public Entity {
    public:
    Food() {}
    Food(int grid_width, int grid_height) : grid_width(grid_width), grid_height(grid_height) {}

    void Update();

    int x;
    int y;

    private:
    int grid_width;
    int grid_height;
};

#endif // FOOD_H
