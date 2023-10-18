namespace Snake
{
    template<class T>
    struct Point
    {
        T x;
        T y;
    };

    struct SDLContext
    {
        SDLContext(std::size_t window_width, std::size_t window_height);
        ~SDLContext();

        SDL_Window * window = nullptr;
        SDL_Renderer * renderer = nullptr;
    };

    SDLContext::SDLContext()
    {
        // ... SDL init
    }

    SDLContext::~SDLContext()
    {
        // ... SDL shutdown
    }

    struct Board
    {
        Board(std::size_t width, std::size_t height);

        enum class Block { head, body, food, empty };

        std::size_t width;
        std::size_t height;

        std::vector<std::vector<Block>> grid;
    };

    Board::Board()
    {
        // ... init grid to "empty"
    }

    struct Food
    {
        Point<std::size_t> position = Point{ 0, 0 };
    };

    struct Snake
    {
        void Grow(int amount);
        void UpdatePosition(Board& board);

        enum class Move { up, down, left, right };

        Move last_dir = Move::up;
        Move dir = Move::up;

        Point<std::size_t> headPosition;
        std::vector<Point<std::size_t>> body;

        int size = 1;
        float speed = 0.5f;
        int growing = 0;
    };

    class Game
    {
        Game(std::size_t gridWidth, std::size_t gridHeight);

        int GetScore() const;
        int GetSize() const;

        void Update();

    private:

        void ReplaceFood();

        Board board;
        Food food;
        Snake snake;

        int score = 0;
        bool alive = true;
    };

    Game::Game(std::size_t gridWidth, std::size_t gridHeight):
        Board(gridWidth, gridHeight)
    {
        ReplaceFood();
    }

    void PollEvents(SDLContext&, bool& quit)
    {
        // ...
    }

    void Render(SDLContext&, Game const& game)
    {
        // ...
    }

    void UpdateWindowTitle(SDLContext&, Game const& game)
    {
        // ...
    }

    void Run(SDLContext& context, Game& game, int frame_rate)
    {
        Uint32 before, second = SDL_GetTicks(), after;
        int frame_time, frames = 0;

        while (true)
        {
            before = SDL_GetTicks();

            bool quit = false;
            PollEvents(sdlContext, quit);

            if (quit)
                break;

            game.Update();

            Render(sdlContext, game);

            frames++;
            after = SDL_GetTicks();
            frame_time = after - before;

            if (after - second >= 1000)
            {
                UpdateWindowTitle(sdlContext, game.GetScore(), frames);

                frames = 0;
                second = after;
            }

            if (frame_rate > frame_time)
            {
                SDL_Delay(frame_rate - frame_time);
            }
        }
    }

} // Snake


#include <SDL.h>

#include <iostream>
#include <cstddef>

int main(int argc, char * argv[])
{
    using namespace Snake;

    const std::size_t window_width = 640;
    const std::size_t window_height = 640;
    SDLContext sdlContext(window_width, window_height);

    const std::size_t grid_width = 32;
    const std::size_t grid_height = 32;
    Game game(grid_width, grid_height);

    const int frame_rate = 1000 / 60;
    Run(sdlContext, game, frame_rate);

    std::cout << "Game has terminated successfully, score: " << game.GetScore()
        << ", size: " << game.GetSize() << std::endl;

    return 0;
}