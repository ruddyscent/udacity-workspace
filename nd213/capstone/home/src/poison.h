#ifndef POISON_H
#define POISON_H

#include "entity.h"

class Poison : public Entity {
    public:
    Poison() {}
    Poison(int grid_width, int grid_height) : grid_width(grid_width), grid_height(grid_height) {}

    void Update();

    int x;
    int y;

    private:
    int grid_width;
    int grid_height;
};

#endif // POISON_H
