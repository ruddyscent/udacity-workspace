#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

#include "controller.h"
#include "game.h"
#include "renderer.h"

using namespace std;

/**
 * Splits a string into tokens based on a delimiter character.
 * 
 * @param str The string to split.
 * @param delim The delimiter character to split the string on. Defaults to ' '.
 * @return A vector of strings representing the tokens.
 */
vector<string> split(const string &str, char delim = ' ')
{
  vector<string> tokens;
  string token;
  istringstream tokenStream(str);
  while (getline(tokenStream, token, delim))
  {
    if (token.empty())
      continue;
    tokens.push_back(token);
  }
  return tokens;
}

int main(int argc, char *argv[])
{
  // Check for valid usage
  if (argc != 2)
  {
    cerr << "Usage: " << argv[0] << " CONFIG_FILE\n";
    return EXIT_FAILURE;
  }

  ifstream input_file(argv[1], ios::in);
  if (!input_file.is_open())
  {
    cerr << "Could not open input file '" << argv[1] << "'!\n";
    return EXIT_FAILURE;
  }

  size_t kFramesPerSecond{60};
  size_t kMsPerFrame{1000 / kFramesPerSecond};
  size_t kScreenWidth{640};
  size_t kScreenHeight{640};
  size_t kGridWidth{32};
  size_t kGridHeight{32};

  // Parse the input file
  string buffer;
  while (getline(input_file, buffer))
  {
    vector<string> splitted = split(buffer, ' ');
    if (splitted.size() != 2)
    {
      cerr << "Invalid input file format: " << buffer << "\n";
      return EXIT_FAILURE;
    }
    else if (splitted[0] == "FramesPerSecond")
      kFramesPerSecond = stoi(splitted[1]);
    else if (splitted[0] == "ScreenWidth")
      kScreenWidth = stoi(splitted[1]);
    else if (splitted[0] == "ScreenHeight")
      kScreenHeight = stoi(splitted[1]);
    else if (splitted[0] == "GridWidth")
      kGridWidth = stoi(splitted[1]);
    else if (splitted[0] == "GridHeight")
      kGridHeight = stoi(splitted[1]);
    else
    {
      cerr << "Invalid keyword: " << buffer << "\n";
      return EXIT_FAILURE;
    }
  }

  Renderer renderer(kScreenWidth, kScreenHeight, kGridWidth, kGridHeight);
  Controller controller;
  Game game(kGridWidth, kGridHeight);
  game.Run(controller, renderer, kMsPerFrame);
  cout << "Game has terminated successfully!\n";
  cout << "Score: " << game.GetScore() << "\n";
  cout << "Size: " << game.GetSize() << "\n";
  return 0;
}