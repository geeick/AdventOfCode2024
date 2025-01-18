#include "globals.h"
#include "Box.h"
#include "Grid.h"
#include "Robot.h"
#include <vector>

int translateCommand(char command);
bool moveObject(char dir, int row, int col);

Input instructions = readFile(file_path_example);

std::string commands = instructions.getCommands(); //commands is a string with the commands
std::vector<std::vector<char>> map = instructions.getGrid(); //grid is a grid object that takes in a 2d vector


int main() {
    for (int cmd = 0; cmd < commands.size(); cmd++) {
        char command = commands[cmd];
        for (int i = 0; i < map.size(); i++) {
            for (int j = 0; j < map[0].size(); j++) {
                if (map[i][j] == '@') {
                    moveObject(command, i, j);
                }
            }
        }
    }


    return 0;
}

bool moveObject(char dir, int row, int col) {
        int command = translateCommand(dir);

        switch (command) {
            default: break;
            case 1:
                if (row > 0 && map[row -1][col] == '#') {
                    return moveObject(dir, row - 1, col);
                }
                if (row <= 0){
                    return false;

                map[row-1][col] = '@';
                map[row][col] = '.';
            case 2:
                map[i][j] = '#';
            case 3:
                map[i][j] = '@';
            case 4:
                map[i][j] = '#';
        }
    }

int translateCommand(char command) {
    if (command == '^')
        return 1;
    if (command == '>')
        return 2;
    if (command == 'v')
        return 3;
    if (command == '<')
        return 4;

    return 0;
}


}

