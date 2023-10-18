/**
 * @file entity.h
 * @brief Contains the declaration of the Entity class.
 */

#ifndef ENTITY_H
#define ENTITY_H

/**
 * @brief The Entity class represents a game entity.
 * 
 * This class provides a base implementation for game entities. It defines a default constructor and a pure virtual function for updating the entity.
 */
class Entity {
    public:
    /**
     * @brief Default constructor for the Entity class.
     * 
     * This constructor initializes a new instance of the Entity class.
     */
    Entity() {}

    /**
     * @brief Virtual destructor for the Entity class.
     * 
     * This virtual destructor ensures that the destructor of any derived class is called when deleting an object of the Entity class.
     */
    virtual ~Entity() {}
    
    /**
     * @brief Updates the entity.
     * 
     * This pure virtual function is used to update the entity's state.
     * 
     */
    virtual void Update() = 0;
};

#endif // ENTITY_H