#include "globals.h"
#include "Box.h"
#include "Grid.h"
#include <vector>

int main() {
    Input instructions = readFile(file_path_example);

    //commands is a string with the commands
    std::string commands = instructions.getCommands();
    std::cout << commands << std::endl;

    //grid is a grid object that takes in a 2d vector
    std::vector<std::vector<char>> map = instructions.getGrid();
    Grid grid(&map);

    for (size_t i = 0; i < grid.rows(); ++i) {
        for (size_t j = 0; j < grid.cols(); ++j) {
            char element = grid()[i][j];
            if (element == '@') {
                grid.addRobot(grid()[i], element);
            }
            if (element == '#') {
                grid.addBox(grid()[i], element);
            }
        }
    }

        //grid now has a robot and the boxes (if I implemented the functions correctly.

        int length = commands.length();
        for (int i = 0; i < length; i++) {
            grid.runCommand(commands.at(i));
        }
    return 0;
}

